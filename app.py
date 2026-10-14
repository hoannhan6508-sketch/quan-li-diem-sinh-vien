# 7. TẠO WEB APP QUẢN LÝ ĐIỂM SINH VIÊN

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cấu hình trang web
st.set_page_config(
    page_title="Quản lý điểm sinh viên",
    layout="wide"
)

# Tiêu đề trang web
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# Tạo dữ liệu 10 sinh viên
data = {
    "Ho_ten": [
        "Nguyen Van An",
        "Tran Thi Binh",
        "Le Van Cuong",
        "Pham Thi Dung",
        "Hoang Van Huy",
        "Vo Thi Lan",
        "Dang Van Minh",
        "Bui Thi Ngoc",
        "Do Van Phuc",
        "Ngo Thi Trang"
    ],
    "Chuyen_can": [9, 8, 7, 10, 6, 8, 9, 7, 5, 10],
    "Giua_ky": [8, 7, 6, 9, 5, 8, 9, 6, 4, 10],
    "Cuoi_ky": [9, 8, 7, 9, 4, 8, 10, 6, 3, 9]
}

df = pd.DataFrame(data)

# Tính điểm tổng kết
df["Tong_ket"] = (
    df["Chuyen_can"] * 0.2
    + df["Giua_ky"] * 0.3
    + df["Cuoi_ky"] * 0.5
).round(2)

# Xếp loại sinh viên
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# Hiển thị bảng điểm
st.header("1. Bảng điểm sinh viên")
st.dataframe(df, use_container_width=True)

# Thống kê
st.header("2. Thống kê điểm sinh viên")

diem_tb = df["Tong_ket"].mean()
cao_nhat = df["Tong_ket"].max()
thap_nhat = df["Tong_ket"].min()
so_dat = (df["Tong_ket"] >= 5).sum()

st.write("Điểm trung bình của lớp:", round(diem_tb, 2))

st.write(
    "Sinh viên có điểm cao nhất:",
    ", ".join(df.loc[df["Tong_ket"] == cao_nhat, "Ho_ten"]),
    "-", cao_nhat
)

st.write(
    "Sinh viên có điểm thấp nhất:",
    ", ".join(df.loc[df["Tong_ket"] == thap_nhat, "Ho_ten"]),
    "-", thap_nhat
)

st.write("Số sinh viên đạt:", so_dat)

# Chọn sinh viên
st.header("3. Xem thông tin sinh viên")

ten = st.selectbox(
    "Chọn một sinh viên:",
    df["Ho_ten"]
)

sv = df[df["Ho_ten"] == ten].iloc[0]

st.write("Điểm chuyên cần:", sv["Chuyen_can"])
st.write("Điểm giữa kỳ:", sv["Giua_ky"])
st.write("Điểm cuối kỳ:", sv["Cuoi_ky"])
st.write("Điểm tổng kết:", sv["Tong_ket"])
st.write("Xếp loại:", sv["Xep_loai"])

# Vẽ biểu đồ
st.header("4. Biểu đồ điểm tổng kết")

fig, ax = plt.subplots(figsize=(12, 6))

ax.bar(
    df["Ho_ten"],
    df["Tong_ket"],
    color="skyblue",
    edgecolor="black"
)

ax.set_title("BIEU DO DIEM TONG KET CUA 10 SINH VIEN")
ax.set_xlabel("Ho ten sinh vien")
ax.set_ylabel("Diem tong ket")
ax.set_ylim(0, 10)

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

st.pyplot(fig)

# Thông tin người thực hiện
st.markdown("---")
st.caption("Người thực hiện: Đinh Phan Hoàn Nhân | MSSV: 35")
