def build_capacity(player_count, number, max_capacity):
    percent = player_count / (number * max_capacity)
    if percent == 0:
        return '[□□□□□] 无人'
    elif 0 < percent <= 0.2:
        return '[■□□□□] 舒适'
    elif 0.2 < percent <= 0.4:
        return '[■■□□□] 良好'
    elif 0.4 < percent <= 0.6:
        return '[■■■□□] 一般'
    elif 0.6 < percent <= 0.8:
        return '[■■■■□] 较拥挤'
    elif percent > 0.8:
        return '[■■■■■] 十分拥挤'


def build_msg(info):
    return f'''[{info['name']} ({info['uniqueName']})]
当前人数：{info['playerCount']}人
拥挤度：{build_capacity(info['playerCount'], info['number'], info['maxCapacity'])}
更新时间：{info['updateTime']}

'''
