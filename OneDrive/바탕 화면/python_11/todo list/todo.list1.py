
FILE_NAME = "todo.txt"


def read_list():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_list(todo_list):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for item in todo_list:
            file.write(item + "\n")


def add_item():
    item = input("추가할 할 일을 입력하세요: ")
    todo = read_list()
    todo.append(item)
    save_list(todo)
    print("추가 완료!\n")


def delete_item():
    todo = read_list()
    show_list(todo)
    if not todo:
        return
    try:
        num = int(input("삭제할 번호를 입력하세요: ")) - 1
        if 0 <= num < len(todo):
            deleted = todo.pop(num)
            save_list(todo)
            print(f"'{deleted}' 삭제 완료!\n")
        else:
            print("잘못된 번호입니다.\n")
    except ValueError:
        print("숫자를 입력하세요.\n")


def edit_item():
    todo = read_list()
    show_list(todo)
    if not todo:
        return
    try:
        num = int(input("수정할 번호를 입력하세요: ")) - 1
        if 0 <= num < len(todo):
            new_text = input("새로운 내용을 입력하세요: ")
            old = todo[num]
            todo[num] = new_text
            save_list(todo)
            print(f"'{old}' → '{new_text}' 수정 완료!\n")
        else:
            print("잘못된 번호입니다.\n")
    except ValueError:
        print("숫자를 입력하세요.\n")


def show_list(todo):
    if not todo:
        print("할 일이 없습니다.\n")
    else:
        print("\n현재 할 일 목록:")
        for i, item in enumerate(todo, 1):
            print(f"{i}. {item}")
        print()


def main():
    while True:
        print("===== TODO 리스트 =====")
        print("1. 목록 보기")
        print("2. 할 일 추가")
        print("3. 할 일 삭제")
        print("4. 할 일 수정")
        print("5. 종료")
        choice = input("번호 선택: ")

        if choice == "1":
            show_list(read_list())
        elif choice == "2":
            add_item()
        elif choice == "3":
            delete_item()
        elif choice == "4":
            edit_item()
        elif choice == "5":
            print("프로그램 종료!")
            break
        else:
            print("잘못된 입력입니다.\n")


main()
