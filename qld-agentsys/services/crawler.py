import requests
import time
from typing import Any, Dict, List

from config.settings import (
    DAV_API_URL_THUOC,
    DAV_API_URL_NGUYENLIEU,
    DAV_API_URL_TADUOC,
    DAV_API_URL_NGUYENLIEU_BYSDKTHUOC,
    DAV_API_HEADERS
)
from services.processor import enrich_item_with_fulltext
from config.key_mapping import (
    thuoc_mapping,
    nguyenlieu_mapping,
    taduoc_mapping
)

def crawl_thuoc_items(limit=100, batch_size=10):
    """Crawl dữ liệu thuốc"""
    results = []
    for skip in range(0, limit, batch_size):
        payload = {
            "SoDangKyThuoc": {},
            "KichHoat": True,
            "skipCount": skip,
            "maxResultCount": batch_size,
            "sorting": None
        }

        try:
            res = requests.post(DAV_API_URL_THUOC, json=payload, headers=DAV_API_HEADERS)
            res.raise_for_status()
            items = res.json().get("result", {}).get("items", [])
            enriched = [enrich_item_with_fulltext(i, thuoc_mapping) for i in items]
            for item in enriched:
                item["loai"] = "thuoc"
            results.extend(enriched)
            time.sleep(0.3)
        except Exception as e:
            print(f"❌ Lỗi khi crawl thuốc tại skip={skip}: {e}")

    return results


def crawl_nguyenlieu_items(limit=100, batch_size=10):
    """Crawl dữ liệu nguyên liệu làm thuốc"""
    results = []
    for skip in range(0, limit, batch_size):
        payload = {
            "isActive": True,
            "ngayHetHanSoDangKyTu": None,
            "ngayHetHanSoDangKyToi": None,
            "ngayKyCongVanTu": None,
            "ngayKyCongVanToi": None,
            "skipCount": skip,
            "maxResultCount": batch_size,
            "sorting": None
        }

        try:
            res = requests.post(DAV_API_URL_NGUYENLIEU, json=payload, headers=DAV_API_HEADERS)
            res.raise_for_status()
            items = res.json().get("result", {}).get("items", [])
            enriched = [enrich_item_with_fulltext(i, nguyenlieu_mapping) for i in items]
            for item in enriched:
                item["loai"] = "nguyenlieu"
            results.extend(enriched)
            time.sleep(0.3)
        except Exception as e:
            print(f"❌ Lỗi khi crawl nguyên liệu tại skip={skip}: {e}")

    return results


def crawl_taduoc_items(limit=100, batch_size=10):
    """Crawl dữ liệu tá dược, vỏ nang"""
    results = []
    for skip in range(0, limit, batch_size):
        payload = {
            "keyword": None,
            "filterByIsActive": True,
            "skipCount": skip,
            "maxResultCount": batch_size,
            "sorting": None
        }

        try:
            res = requests.post(DAV_API_URL_TADUOC, json=payload, headers=DAV_API_HEADERS)
            res.raise_for_status()
            items = res.json().get("result", {}).get("items", [])
            enriched = [enrich_item_with_fulltext(i, taduoc_mapping) for i in items]
            for item in enriched:
                item["loai"] = "taduoc"
            results.extend(enriched)
            time.sleep(0.3)
        except Exception as e:
            print(f"❌ Lỗi khi crawl tá dược tại skip={skip}: {e}")

    return results


PHAN_LOAI_TXT = {0: "Dược phẩm", 1: "Tá dược", 2: "Vỏ nang"}

def _mk_fulltext(obj: Dict[str, Any], mapping: Dict[str, str]) -> str:
    """Ghép key:value thành chuỗi, bỏ None và metadata. Hỗ trợ key lồng nhau như 'a.b.c'."""
    def get_nested_value(data: dict, key: str):
        for part in key.split('.'):
            if isinstance(data, dict):
                data = data.get(part)
            else:
                return None
        return data

    parts = []
    for k, label in mapping.items():
        val = get_nested_value(obj, k)
        if val not in (None, "", [], {}):
            parts.append(f"{label}: {val}")
    return "; ".join(parts)



def _fetch_nguyen_lieu(so_dang_ky: str, limit=100) -> List[Dict[str, Any]]:
    """Gọi DAV_API_URL_NGUYENLIEU_BYSDKTHUOC"""
    try:
        res = requests.get(
            f"{DAV_API_URL_NGUYENLIEU_BYSDKTHUOC}?soDangKy={so_dang_ky}",
            headers=DAV_API_HEADERS,
            timeout=30,
        )
        res.raise_for_status()
        return res.json().get("result", [])
    except Exception as e:
        print("❌ Lỗi gọi nguyên liệu theo SĐK:", e)
        return []

def crawl_thuoc_detail_items(limit=100, batch_size=10, first_skip =0) -> List[Dict[str, Any]]:
    """
    Crawl thuốc, truy vấn API nguyên liệu -> ghép 'nguyenLieuLamThuoc',
    build fulltext & embedding (embedding chưa tạo ở đây – giao lại cho MongoDB._prepare_and_insert)
    """
    results = []
    for skip in range(first_skip, limit + first_skip, batch_size):
        payload = {
            "SoDangKyThuoc": {},
            "KichHoat": True,
            "skipCount": skip,
            "maxResultCount": batch_size,
            "sorting": None,
        }
        try:
            res = requests.post(DAV_API_URL_THUOC, json=payload, headers=DAV_API_HEADERS)
            res.raise_for_status()
            items = res.json().get("result", {}).get("items", [])

            for raw in items:
                # enrich thuốc
                thuoc = enrich_item_with_fulltext(raw, thuoc_mapping)

                # ---------- nguyên liệu ----------
                sdk = raw.get("soDangKy") or raw.get("soDangKyThuoc")
                nl_items = _fetch_nguyen_lieu(sdk)
                for nl in nl_items:
                    # human‑friendly phân loại
                    nl["phanLoaiText"] = PHAN_LOAI_TXT.get(nl.get("phanLoai"), "Khác")
                thuoc["nguyenLieuLamThuoc"] = nl_items

                # ---------- build fulltext ----------
                # 1) thông tin thuốc
                txt = _mk_fulltext(thuoc, thuoc_mapping)

                # 2) thêm danh sách nguyên liệu (nếu có)
                if nl_items:
                    lines = [
                        f"- {n.get('phanLoaiText')}: {n.get('tenNguyenLieu')}"
                        for n in nl_items
                    ]
                    txt += "\nCác nguyên liệu làm thuốc:\n" + "\n".join(lines)

                thuoc["fulltext"] = txt
                thuoc["loai"] = "thuoc"  # gắn loại để phân biệt collection

                results.append(thuoc)

            time.sleep(0.3)
        except Exception as e:
            print(f"❌ Lỗi crawl detail thuốc tại skip={skip}: {e}")

    return results