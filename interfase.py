import App


def create_note(number):
    title = check_len_text_input(
        input('Введите название (не менее 2 символов): '), number)
    body = check_len_text_input(
        input('Введите текст заметки (не менее 2 символов): '), number)
    return App.Data(title=title, body=body)


def menu():
    print("\nДля работы с приложением 'Заметки' используйте следующие команды:\n"
          "\nall - вывод всех существующих записей\nadd - добавление записи\ndell - удаление записи\nedit - редактирование записи\ndata - поиск записей по указанной дате\nid - поиск записей по id\nexit - выход из программы\n\nВведите команду: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'В нём должно содержаться не менее {n} символов\n')
        text = input('Повторите ввод: ')
    else:
        return text


def goodbuy():
    print("Приложение завершило свою работу")
