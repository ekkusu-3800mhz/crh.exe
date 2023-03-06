def build_capacity(number, max_capacity):
    percent = number / max_capacity
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

def build_msg(data):
    item = f'''[疯狂牛仔城左机（1P/2P）]
当前人数：{data['cabinets']['left']['count']}人
拥挤度：{build_capacity(data['cabinets']['left']['count'], data['maxCapacity'])}
更新时间：{data['cabinets']['left']['updateTime']}

[疯狂牛仔城右机（3P/4P）]
当前人数：{data['cabinets']['right']['count']}人
拥挤度：{build_capacity(data['cabinets']['right']['count'], data['maxCapacity'])}
更新时间：{data['cabinets']['right']['updateTime']}
'''
    return item