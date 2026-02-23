import csv


def read_menu():
    menu = []
    with open("menu.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            menu.append(row)
    return menu


def write_menu(menu):
    with open("menu.csv", "w", newline="", encoding="utf-8") as file:
        fieldnames = ["id", "name", "price", "category"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for item in menu:
            writer.writerow(item)


# Hiển thị danh sách món
def display_menu(menu):
    print("\n===== DANH SÁCH MÓN ĂN =====")
    for item in menu:
        print(item["id"], "-", item["name"], "-", item["price"], "đ", "-", item["category"])


# THÊM MÓN ĂN
def add_food(menu):
    food_id = input("Nhập ID món: ")

    # kiểm tra trùng ID
    for item in menu:
        if item["id"] == food_id:
            print("ID đã tồn tại!")
            return menu

    name = input("Nhập tên món: ")
    price = input("Nhập giá: ")
    category = input("Nhập loại: ")

    new_food = {
        "id": food_id,
        "name": name,
        "price": price,
        "category": category
    }

    menu.append(new_food)
    print("Thêm món thành công!")

    return menu


# Sửa món ăn theo ID
def update_food(menu, food_id):
    found = False
    for item in menu:
        if item["id"] == food_id:
            print("Đã tìm thấy món:", item["name"])
            item["name"] = input("Nhập tên mới: ")
            item["price"] = input("Nhập giá mới: ")
            item["category"] = input("Nhập loại mới: ")
            break
        else:
            print("Không tìm thấy món!")

    return menu


# Xóa món ăn theo ID
def delete_food(menu, food_id):
    new_menu = [item for item in menu if item["id"] != food_id]

    if len(new_menu) == len(menu):
        print("Không tìm thấy món để xóa!")
    else:
        print("Xóa thành công!")

    return new_menu
