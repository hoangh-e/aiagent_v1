"""
Tên thuốc
├── Hoạt chất chính
├── Tá dược 1
│   └── Nguyên liệu gốc
└── Vỏ nang
    └── Thành phần
"""


taduoc_mapping = {
    "tenTaDuocVoNang": "Tên tá dược / vỏ nang",
    "tenThuoc": "Tên thuốc chứa tá dược",
    "soDangKyLuuHanh": "Số đăng ký lưu hành",
    "tenCoSoSanXuat": "Tên cơ sở sản xuất",
    "diaChiCoSoSanXuat": "Địa chỉ cơ sở sản xuất",
    "nuocSanXuat": "Nước sản xuất",
    "tieuChuanChatLuong": "Tiêu chuẩn chất lượng",
    "nguoiDuyetCongBo": "Người duyệt công bố",
    "ngayHetHieuLucSDK": "Ngày hết hiệu lực SĐK",
    "creationTime": "Ngày tạo bản ghi"
    
    # Metadata
    # "vaiTroXuLyId": ...,
    # "hoSoId": ...,
    # "hoSoXuLyId": ...,
    # "nguoiDuyetCongBoId": ...,
    # "coSoSXId": ...,
    # "isActive": ...,
    # "phanLoai": ...,
    # "isDeleted": ...,
    # "deleterUserId": ...,
    # "deletionTime": ...,
    # "lastModificationTime": ...,
    # "lastModifierUserId": ...,
    # "creatorUserId": ...,
    # "id": ...
}

thuoc_mapping = {
    # Thông tin chính
    "tenThuoc": "Tên thuốc",
    "soDangKy": "Số đăng ký",
    "soDangKyCu": "Số đăng ký cũ",
    "dotCap": "Đợt cấp",
    "phanLoaiThuocEnum": "Phân loại thuốc",
    "hoatChatChinh": "Hoạt chất chính",
    "tenHoatChatChinh": "Tên hoạt chất chính",
    "hamLuong": "Hàm lượng",
    "dangBaoChe": "Dạng bào chế",
    "dongGoi": "Đóng gói",
    "tieuChuan": "Tiêu chuẩn",
    "tuoiTho": "Tuổi thọ",
    "giaDangKy": "Giá đăng ký",
    "donViTinh": "Đơn vị tính",
    "hangSanXuat": "Hãng sản xuất",
    "coSoSanXuat": "Cơ sở sản xuất",
    "isHetHan": "Đã hết hạn",
    "isActive": "Đang hoạt động",
    "ghiChu": "Ghi chú",

    # Công ty đăng ký
    "congTyDangKy.tenCongTyDangKy": "Công ty đăng ký",
    "congTyDangKy.diaChiDangKy": "Địa chỉ đăng ký",
    "congTyDangKy.nuocDangKy": "Nước đăng ký",

    # Công ty sản xuất
    "congTySanXuat.tenCongTySanXuat": "Công ty sản xuất",
    "congTySanXuat.diaChiSanXuat": "Địa chỉ sản xuất",
    "congTySanXuat.nuocSanXuat": "Nước sản xuất",

    # Thông tin cấp phép
    "ngayCapSoDangKy": "Ngày cấp SĐK",
    "soQuyetDinh": "Số quyết định",
    "thongTinDangKyThuoc.ngayCapSoDangKy": "Ngày cấp SĐK (chi tiết)",
    "thongTinDangKyThuoc.ngayGiaHanSoDangKy": "Ngày gia hạn SĐK",
    "thongTinDangKyThuoc.ngayHetHanSoDangKy": "Ngày hết hạn SĐK",
    "thongTinDangKyThuoc.soQuyetDinh": "Số quyết định SĐK",
    "thongTinDangKyThuoc.dotCap": "Đợt cấp SĐK",

    # Thông tin thuốc cơ bản
    "thongTinThuocCoBan.hoatChatChinh": "Hoạt chất chính (cơ bản)",
    "thongTinThuocCoBan.hamLuong": "Hàm lượng (cơ bản)",
    "thongTinThuocCoBan.dangBaoChe": "Dạng bào chế (cơ bản)",
    "thongTinThuocCoBan.dongGoi": "Đóng gói (cơ bản)",
    "thongTinThuocCoBan.tieuChuan": "Tiêu chuẩn (cơ bản)",
    "thongTinThuocCoBan.tuoiTho": "Tuổi thọ (cơ bản)",
    "thongTinThuocCoBan.tenDuongDung": "Đường dùng",

    # Tài liệu
    "thongTinTaiLieu.urlHuongDanSuDung": "Tài liệu HDSD",
    "thongTinTaiLieu.urlNhan": "URL Nhãn",
    "thongTinTaiLieu.urlNhanVaHDSD": "URL Nhãn + HDSD",

    # Kiểm soát đặc biệt
    "thuocKiemSoatDacBiet.isHoSoACTD": "Có hồ sơ ACTD",
    "thuocKiemSoatDacBiet.isHoSoLamSang": "Có hồ sơ lâm sàng",
    "thuocKiemSoatDacBiet.soQuyetDinhCongVan": "Số công văn đặc biệt",

    # Vắc xin - sinh phẩm
    "vacXinSinhPham.phongBenh": "Phòng bệnh",

    # Thông tin thêm
    "nguonDuLieuEnum": "Nguồn dữ liệu",
    "trangThai": "Trạng thái",
    "lyDoSuaDoi": "Lý do sửa đổi",
    "maSoHoSoGiaHan": "Mã hồ sơ gia hạn",
    "ngayTiepNhanHSGiaHan": "Ngày tiếp nhận gia hạn",
    "urlGiayTiepNhanGiaHan": "URL giấy tiếp nhận gia hạn"

    # Metadata :
    # "messageError", "isCapNhatNHHSDK", "isLuongCapNhat", "ketQua", "maThuoc", "tenKhongDau"
    # "isDeleted", "creatorUserId", "creationTime", "lastModifierUserId", "lastModificationTime",
    # "deleterUserId", "deletionTime", "id", "isDuocPhep", "doanhNghiepId", "mstDoanhNghiep", "isXacNhanSoHuuDoanhNghiep",
    # "congTyDangKyId", "congTySanXuatId", "vacXinSinhPham.loaiVacXin",
    # "thongTinThuocCoBan.*Id", "thongTinThuocCoBan.maDuongDung", "thongTinThuocCoBan.dongGoiJson",
    # "thongTinTaiLieu.jsonTaiLieuTCCL", "thuocKiemSoatDacBiet.*", "thongTinDangKyThuoc.urlSoQuyetDinh",
    # "thongTinRutSoDangKy.urlCongVanRutSoDangKy"
}

nguyenlieu_mapping = {
    # Thông tin nguyên liệu
    "tenNguyenLieu": "Tên nguyên liệu",
    "tieuChuanChatLuongNguyenLieu": "Tiêu chuẩn chất lượng",
    "phanLoai": "Phân loại",
    "tenHoatChatChuan": "Tên hoạt chất chuẩn",
    "hcc_TenHoatChat": "Hoạt chất nhóm kiểm soát",
    "hcc_IsKiemSoatDacBiet": "Thuộc kiểm soát đặc biệt",

    # Thông tin thuốc sử dụng nguyên liệu
    "tenThuoc": "Tên thuốc sử dụng",
    "soDangKy": "Số đăng ký thuốc",
    "ngayHetHanSoDangKy": "Ngày hết hạn SĐK",
    "tenCoSoSanXuatThuoc": "Cơ sở sản xuất thuốc",

    # Thông tin nhà sản xuất nguyên liệu
    "tenCoSoSanXuatNguyenLieu": "Tên cơ sở sản xuất nguyên liệu",
    "diaChiCoSoSanXuatNguyenLieu": "Địa chỉ sản xuất nguyên liệu",
    "nuocSanXuatNguyenLieu": "Nước sản xuất nguyên liệu",

    # Công văn
    "soCongVan": "Số công văn",
    "tieuDeCongVan": "Tiêu đề công văn",
    "ngayKyCongVan": "Ngày ký công văn",

    # Trạng thái, quản lý
    "isPhaiCapPhepNhapKhau": "Yêu cầu cấp phép nhập khẩu",
    "isKhongCongVan": "Không có công văn",
    "lyDoKhongCongVan": "Lý do không có công văn",
    "trangThai": "Trạng thái",
    "isActive": "Đang hoạt động",
    "chuyenVienXacNhanPhuHop": "Chuyên viên xác nhận phù hợp"

    # Metadata:
    # "messageError", "lyDoSuaDoi", "hcc_DanhMucKiemSoatDacBiet", "hcc_DanhMucKiemSoatDacBietID"
    # "congBoNguyenLieuId", "isDaRutSoDangKy", "urlCongVanRutSoDangKy", "pId"
    # "ngayHetHanCongVan", "urlCongVan", "isCongBoLanDau", "maThuoc", "maHoSo"
    # "loaiNguyenLieuLamThuoc", "hoatChatChuanID", "loaiNguyenLieu"
    # "nuocSanXuatID", "coSoSanXuatNguyenLieuID", "coSoSanXuatThuocID"
    # "taiLieuDinhKemJson"
    # "isDeleted", "deleterUserId", "deletionTime", "lastModificationTime",
    # "lastModifierUserId", "creationTime", "creatorUserId", "id"
}

nguyen_lieu_lam_thuoc_mapping = {
    "tenNguyenLieu": "Tên nguyên liệu",
    "loaiNguyenLieuLamThuoc": "Loại nguyên liệu làm thuốc",
    "tenThuoc": "Tên thuốc chứa nguyên liệu",
    "soDangKy": "Số đăng ký",
    "ngayHetHanSoDangKy": "Ngày hết hạn số đăng ký",
    "tenCoSoSanXuatThuoc": "Tên cơ sở sản xuất thuốc",
    "tenCoSoSanXuatNguyenLieu": "Tên cơ sở sản xuất nguyên liệu",
    "diaChiCoSoSanXuatNguyenLieu": "Địa chỉ cơ sở sản xuất nguyên liệu",
    "nuocSanXuatNguyenLieu": "Nước sản xuất nguyên liệu",
    "tieuChuanChatLuongNguyenLieu": "Tiêu chuẩn chất lượng nguyên liệu",
    "isPhaiCapPhepNhapKhau": "Yêu cầu cấp phép nhập khẩu",
    "isCongBoLanDau": "Công bố lần đầu",
    "lyDoSuaDoi": "Lý do sửa đổi",
    "soCongVan": "Số công văn",
    "tieuDeCongVan": "Tiêu đề công văn",
    "ngayKyCongVan": "Ngày ký công văn",
    "ngayHetHanCongVan": "Ngày hết hạn công văn",
    "urlCongVan": "File công văn",
    "isKhongCongVan": "Không có công văn",
    "lyDoKhongCongVan": "Lý do không có công văn",
    "creationTime": "Ngày tạo bản ghi",
    "chuyenVienXacNhanPhuHop": "Chuyên viên xác nhận phù hợp",
    "maThuoc": "Mã thuốc",
    "maHoSo": "Mã hồ sơ",
    "trangThai": "Trạng thái",
    # Metadata / hệ thống :
        # "id": ...,
        # "congBoNguyenLieuId": ...,
        # "coSoSanXuatNguyenLieuID": ...,
        # "coSoSanXuatThuocID": ...,
        # "hoatChatChuanID": ...,
        # "nuocSanXuatID": ...,
        # "pId": ...,
        # "phanLoai": ...,
        # "maThuoc": ...,
        # "maHoSo": ...,
        # "trangThai": ...,
        # "taiLieuDinhKemJson": ...,
        # "isDeleted": ...,
        # "isActive": ...,
        # "creatorUserId": ...,
        # "creationTime": ...,
        # "lastModifierUserId": ...,
        # "lastModificationTime": ...,
        # "deleterUserId": ...,
        # "deletionTime": ...

}
