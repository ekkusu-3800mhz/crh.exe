import src.libraries.data as Data
import time


def get_all():
    return Data.get_data()


def set_player(command, number):
    origin = Data.get_data()
    data = {
        'count': number,
        'updateTime': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    }
    if command == '左' or command == '右':
        if command == '左':
            origin['cabinets']['left'] = data
        elif command == '右':
            origin['cabinets']['right'] = data
        Data.set_data(origin['cabinets'])
        return {
            'error': None,
            'data': Data.get_data()
        }
    else:
        return {
            'error': '请输入正确的指令。指令格式请输入“帮助”查看。'
        }
