
import json

def get_nested_value(data: dict, path: str):
    keys = path.split(".")
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key)
        else:
            return None
    return data

def normalize_value(val):
    if isinstance(val, list):
        if all(isinstance(v, dict) for v in val):
            # Dùng ; để tách từng file đính kèm
            return "; ".join([v.get("moTaTep") or v.get("duongDanTep", "") for v in val])
        return "; ".join(map(str, val))  # Tách list thường bằng ;
    if isinstance(val, dict):
        return json.dumps(val, ensure_ascii=False)
    if isinstance(val, bool):
        return "Có" if val else "Không"
    if val is None or val == "":
        return "Không rõ"
    return str(val)

def enrich_item_with_fulltext(item: dict, field_mapping: dict):
    fields = []
    for key, label in field_mapping.items():
        raw = get_nested_value(item, key)
        value = normalize_value(raw)
        fields.append(f"{label}: {value}")
    item["fulltext"] = "; ".join(fields)  # 👉 Sử dụng dấu ; để tách rõ từng nhãn
    return item
