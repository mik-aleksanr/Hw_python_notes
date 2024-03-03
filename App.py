from datetime import datetime
import uuid


class Data:
    def __init__(self, id=str(uuid.uuid1())[0:3],  title="текст", body="текст", date=str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def get_id(data):
        return data.id

    def get_title(data):
        return data.title

    def get_body(data):
        return data.body

    def get_date(data):
        return data.date

    def set_id(data):
        data.id = str(uuid.uuid1())[0:3]

    def set_title(data, title):
        data.title = title

    def set_body(data, body):
        data.body = body

    def set_date(data):
        data.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def to_string(data):
        return data.id + ';' + data.title + ';' + data.body + ';' + data.date

    def map_note(data):
        return '\nID: ' + data.id + '\n' + 'Название: ' + data.title + '\n' + 'Описание: ' + data.body + '\n' + 'Дата публикации: ' + data.date