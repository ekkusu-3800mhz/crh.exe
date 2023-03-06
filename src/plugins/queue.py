import re

from nonebot import on_command, on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Event, Bot, Message, MessageSegment

from src.libraries.service import get_all, set_player
from src.libraries.msg_builder import build_msg

all_stats = on_command('all_stats ', aliases={'牛几卡'})

@all_stats.handle()
async def _(bot: Bot, event: Event, state: T_State):
    result = get_all()
    await all_stats.send(Message([
        MessageSegment("text", {
            "text": build_msg(result)
        })
    ]))


player_cal = on_regex(r"^(.+)机(\d+)卡$")

@player_cal.handle()
async def _(bot: Bot, event: Event, state: T_State):
    regex = "^(.+)机(\d+)卡$"
    res = re.match(regex, str(event.get_message()).lower()).groups()
    command = res[0]
    number = res[1]
    result = set_player(command, int(number))
    if not result['error']:
        msg = MessageSegment("text", {
            "text": build_msg(result['data'])
        })
    else:
        msg = MessageSegment("text", {
            "text": result['error']
        })
    await player_cal.send(Message([msg]))
