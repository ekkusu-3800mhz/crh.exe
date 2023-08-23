import re

from nonebot import on_command, on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Event, Bot, Message, MessageSegment

from src.libraries.service import get_all_maimai, get_all_chunithm, set_player
from src.libraries.msg_builder import build_msg


# 获取所有机厅排队人数

all_stats_maimai = on_command('all_stats_maimai ', aliases={'舞萌几卡'})

@all_stats_maimai.handle()
async def _(bot: Bot, event: Event, state: T_State):
    result = await get_all_maimai()
    msg = []
    msg.append(MessageSegment("text", {
        "text": f"【全域舞萌DX排队情况】"
    }))
    if not result['data']['error']:
        for info in result['data']['cabinetList']:
            msg.append(MessageSegment("text", {
                "text": build_msg(info),
            }))
    else:
        msg.append(MessageSegment("text", {
            "text": result['data']['error'],
        }))
    await all_stats_maimai.send(Message(msg))


all_stats_chunithm = on_command('all_stats_chunithm ', aliases={'中二几卡'})

@all_stats_chunithm.handle()
async def _(bot: Bot, event: Event, state: T_State):
    result = await get_all_chunithm()
    msg = []
    msg.append(MessageSegment("text", {
        "text": f"【全域中二节奏NEW排队情况】"
    }))
    if not result['data']['error']:
        for info in result['data']['cabinetList']:
            msg.append(MessageSegment("text", {
                "text": build_msg(info),
            }))
    else:
        msg.append(MessageSegment("text", {
            "text": result['data']['error'],
        }))
    await all_stats_chunithm.send(Message(msg))


# 设置指定机台的排队人数

player_cal = on_regex(r"^([\u4e00-\u9fa5]+)(\d+)卡$")

@player_cal.handle()
async def _(bot: Bot, event: Event, state: T_State):
    # 解构QQ消息正文，提取机台名称和排队人数
    regex = "^([\u4e00-\u9fa5]+)(\d+)卡$"
    res = re.match(regex, str(event.get_message()).lower()).groups()
    command = res[0]
    number = int(res[1])
    # 设置该机台的排队人数
    result = await set_player(command, number)
    if not result['data']['error']:
        msg = MessageSegment("text", {
            "text": build_msg(result['data']['cabinetInfo']),
        })
    else:
        msg = MessageSegment("text", {
            "text": result['data']['error'],
        })
    await player_cal.send(Message([msg]))
