import file
import App
import interfase

number = 2


def add():
    note = interfase.create_note(number)
    array = file.read()
    for notes in array:
        if App.Data.get_id(note) == App.Data.get_id(notes):
            App.Data.set_id(note)
    array.append(note)
    file.write(array, 'a')
    print('Заметка успешно добавлена')


def show(text):
    global date
    logic = True
    array = file.read()
    if text == 'date':
        date = input('Введите дату dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(App.Data.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + App.Data.get_id(notes))
        if text == 'date':
            logic = False
            if date in App.Data.get_date(notes):
                print(App.Data.map_note(notes))
    if logic == True:
        print('У вас пока нет ни одной заметки')


def id_edit_del_show(text):
    id = input('Введите id заметки: ')
    array = file.read()
    logic = True
    for notes in array:
        if id == App.Data.get_id(notes):
            logic = False
            if text == 'edit':
                note = interfase.create_note(number)
                App.Data.set_title(notes, note.get_title())
                App.Data.set_body(notes, note.get_body())
                App.Data.set_date(notes)
                print('Заметка успешно изменена')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена')
            if text == 'show':
                print(App.Data.map_note(notes))
    if logic == True:
        print('Заметка по указанному id отсутствует, проверьте правильность id!')
    file.write(array, 'a')
