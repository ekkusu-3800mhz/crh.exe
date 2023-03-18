import re

from nonebot import on_command, on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Event, Bot, Message, MessageSegment

from src.libraries.service import get_all, set_player
from src.libraries.msg_builder import build_msg


# 获取所有机厅排队人数

all_stats = on_command('all_stats ', aliases={'机厅几卡'})

@all_stats.handle()
async def _(bot: Bot, event: Event, state: T_State):
    result = await get_all()
    msg = []
    if not result['data']['error']:
        for info in result['data']['cabinetList']:
            msg.append(MessageSegment("text", {
                "text": build_msg(info),
            }))
    else:
        msg.append(MessageSegment("text", {
            "text": result['data']['error'],
        }))
    await all_stats.send(Message(msg))


# 设置指定机台的排队人数

player_cal = on_regex(r"^(.+)(\d+)卡$")

@player_cal.handle()
async def _(bot: Bot, event: Event, state: T_State):
    # 解构QQ消息正文，提取机台名称和排队人数
    regex = "^(.+)(\d+)卡$"
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
