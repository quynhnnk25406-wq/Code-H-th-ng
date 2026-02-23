from func_menu import *

def main():
    menu = read_menu()

    while True:
        print("\n1. Xem danh sách")
        print("2. Thêm món")
        print("3. Sửa món")
        print("4. Xóa món")
        print("5. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == "1":
            display_menu(menu)

        elif choice == "2":
            menu = add_food(menu)
            write_menu(menu)

        elif choice == "3":
            food_id = input("Nhập ID món cần sửa: ")
            menu = update_food(menu, food_id)
            write_menu(menu)

        elif choice == "4":
            food_id = input("Nhập ID món cần xóa: ")
            menu = delete_food(menu, food_id)
            write_menu(menu)

        elif choice == "5":
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
