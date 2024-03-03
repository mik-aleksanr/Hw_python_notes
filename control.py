import metods as m
import interfase


def run():
    input_from_user = ''
    while input_from_user != 'exit':
        interfase.menu()
        input_from_user = input().strip()
        if input_from_user == 'all':
            m.show('all')
        if input_from_user == 'add':
            m.add()
        if input_from_user == 'dell':
            m.show('all')
            m.id_edit_del_show('del')
        if input_from_user == 'edit':
            m.show('all')
            m.id_edit_del_show('edit')
        if input_from_user == 'data':
            m.show('date')
        if input_from_user == 'id':
            m.show('id')
            m.id_edit_del_show('show')
        if input_from_user == 'exit':
            interfase.goodbuy()
            break
