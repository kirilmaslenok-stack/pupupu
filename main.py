"""Основной файл приложения Task Manager
version 0.0.7

Приложение умеет:
- показывать задачи;
- добавлять задачи;
- редактировать задачи;
- удалять задачи;
- загружать задачи из файла;
- сохранять задачи в файл.
"""

FILE_NAME = "tasks.txt"

#-------------------------Переменные для вызова---------------------------
def show_collection(task_collection):
    print("-" * 40)

    if not task_collection:
        print("Список задач пуст.")
    else:
        for number, task in enumerate(task_collection, start=1):
            print(f"{number}. {task}")

    print("-" * 40)


def check_confirm(select_task, task_list):

    if select_task.isdigit():
        number = int(select_task)

        if 1 <= number <= len(task_list):
            return 1
        return 2

    return 3


def edited_task(task_collection):
    if not task_collection:
        print("Список задач пуст.")
        return

    select_edit = input("Введите номер задачи: ")
    result = check_confirm(select_edit, task_collection)

    if result == 1:
        edit_name = input("Введите новое имя задачи: ").strip()

        if not edit_name:
            print("Название не может быть пустым!")
            return

        task_collection[int(select_edit) - 1] = edit_name
        print(f"Задача №{select_edit} успешно изменена.")

    elif result == 2:
        print(f"Задачи с номером {select_edit} нет в списке.")

    else:
        print("Введите именно номер задачи!")


def deleted_task(task_collection):
    if not task_collection:
        print("Список задач пуст.")
        return

    delete_number = input("Введите номер задачи для удаления: ")
    result = check_confirm(delete_number, task_collection)

    if result == 1:
        deleted = task_collection.pop(int(delete_number) - 1)
        print(f"Задача «{deleted}» успешно удалена.")

    elif result == 2:
        print(f"Задачи с номером {delete_number} нет в списке.")

    else:
        print("Введите именно номер задачи!")


def load_tasks(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            task_collection = [line.strip() for line in file if line.strip()]
        return task_collection
    except FileNotFoundError:
        return []


def save_tasks(task_collection, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        for task in task_collection:
            file.write(task + "\n")


def main():
    collection = load_tasks(FILE_NAME)

    print("Задачи загружены из файла:")
    show_collection(collection)

    is_running = True
#-------------------------------Меню-------------------------------------
    while is_running:
        print(
            "\nМеню\n"
            "1 - показать задачи\n"
            "2 - добавить задачу\n"
            "3 - редактировать задачу\n"
            "4 - удалить задачу\n"
            "5 - выйти\n"
        )

        choice_user = input("Введите ваш выбор (1, 2, 3, 4 или 5): ").strip()

        match choice_user:
            case "1":
                show_collection(collection)
                input("Нажмите ENTER, чтобы продолжить...")

            case "2":
                add_task = input("Введите имя задачи для добавления: ").strip()

                if not add_task:
                    print("Название не может быть пустым!")
                else:
                    collection.append(add_task)
                    print("Задача добавлена.")
                    save_tasks(collection, FILE_NAME)

            case "3":
                show_collection(collection)
                edited_task(collection)
                save_tasks(collection, FILE_NAME)

            case "4":
                show_collection(collection)
                deleted_task(collection)
                save_tasks(collection, FILE_NAME)

            case "5":
                save_tasks(collection, FILE_NAME)
                is_running = False
                print("Пока-пока!")

            case _:
                print("Такого пункта нет!")

    save_tasks(collection, FILE_NAME)


if __name__ == "__main__":
    main()
