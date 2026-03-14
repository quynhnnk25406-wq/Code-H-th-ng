import os
import json
from datetime import datetime

DATA_DIR = "data"
FEEDBACK_FILE = os.path.join(DATA_DIR, "feedback.json")

# ĐỌC FILE JSON

def doc_file_json(ten_file):
    if not os.path.exists(ten_file):
        return []

    try:
        with open(ten_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

# GHI FILE JSON

def ghi_file_json(ten_file, data):

    os.makedirs(os.path.dirname(ten_file), exist_ok=True)

    with open(ten_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)



# KHÁCH GỬI GÓP Ý

def gui_gop_y(user_id, noi_dung):

    ds = doc_file_json(FEEDBACK_FILE)

    new_id = max([item.get("id", 0) for item in ds], default=0) + 1

    gop_y = {
        "id": new_id,
        "khach": {
            "user_id": user_id,
            "noi_dung": noi_dung.strip(),
            "thoi_gian": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        "admin_reply": None
    }

    ds.append(gop_y)

    ghi_file_json(FEEDBACK_FILE, ds)

    print("✔ Gửi góp ý thành công!")



# ADMIN PHẢN HỒI

def admin_reply(id_gop_y, noi_dung):

    ds = doc_file_json(FEEDBACK_FILE)

    for item in ds:

        if item["id"] == id_gop_y:

            item["admin_reply"] = {
                "noi_dung": noi_dung.strip(),
                "thoi_gian": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            ghi_file_json(FEEDBACK_FILE, ds)

            print("✔ Admin đã phản hồi khách.")
            return

    print(" Không tìm thấy ID góp ý.")


# HIỂN THỊ GÓP Ý

def hien_thi():

    ds = doc_file_json(FEEDBACK_FILE)

    if not ds:
        print("Chưa có góp ý nào.")
        return

    print("\n========== DANH SÁCH GÓP Ý ==========")

    for item in ds:

        print(f"\nID: {item['id']}")

        khach = item["khach"]

        print("Khách:", khach["user_id"])
        print("Nội dung:", khach["noi_dung"])
        print("Thời gian:", khach["thoi_gian"])

        if item["admin_reply"]:

            admin = item["admin_reply"]

            print("Admin trả lời:", admin["noi_dung"])
            print("Thời gian:", admin["thoi_gian"])

        else:

            print("Admin: Chưa phản hồi")

        print("-" * 40)



# CHẠY THỬ
def main():

    while True:

        print("\n========== HỆ THỐNG GÓP Ý ==========")
        print("1. Khách gửi góp ý")
        print("2. Xem danh sách góp ý")
        print("3. Admin phản hồi")
        print("4. Thoát")

        chon = input("Chọn chức năng: ")

        # GỬI GÓP Ý
        if chon == "1":

            user_id = input("Nhập mã khách: ")
            noi_dung = input("Nhập nội dung góp ý: ")

            if not noi_dung.strip():
                print(" Nội dung không được để trống.")
                continue

            gui_gop_y(user_id, noi_dung)

        # XEM DANH SÁCH
        elif chon == "2":

            hien_thi()

        # ADMIN PHẢN HỒI
        elif chon == "3":

            try:
                id_gop_y = int(input("Nhập ID góp ý cần trả lời: "))
            except:
                print("ID phải là số.")
                continue

            noi_dung = input("Nhập nội dung phản hồi: ")

            if not noi_dung.strip():
                print("Nội dung phản hồi không được để trống.")
                continue

            admin_reply(id_gop_y, noi_dung)

        # THOÁT
        elif chon == "4":

            print("Thoát chương trình.")
            break

        else:

            print("Chọn sai chức năng.")

# CHẠY CHƯƠNG TRÌNH

if __name__ == "__main__":
    main()
