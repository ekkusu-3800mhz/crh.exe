from nonebot import on_command, on_notice
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Message, Event, Bot, MessageSegment
from nonebot.exception import IgnoredException
from nonebot.message import event_preprocessor


@event_preprocessor
async def preprocessor(bot, event, state):
    if hasattr(event, 'message_type') and event.message_type == "private" and event.sub_type != "friend":
        raise IgnoredException("not reply group temp message")


# 发送帮助信息
        
help = on_command('帮助')

@help.handle()
async def _(bot: Bot, event: Event, state: T_State):
    help_str = '''CRH.EXE implements mai-bot

本排卡插件可更新清远全域舞萌DX/中二节奏NEW的排队人数，可用指令如下：
· 舞萌几卡：查询全域舞萌DX机台的排队情况。
· 中二几卡：查询全域中二节奏NEW机台的排队情况。
· <店铺机台><人数>卡：设置指定店铺，指定机台的当前人数。
参考名称：牛(舞萌|中二)(左|右)机、万达、城广、大润发等。

本bot还提供清远牛仔城舞萌直播间状态查询，输入“直播状态”即可查看开播情况。
'''
    await help.send(Message([
        MessageSegment("text", {
            "text": f"{help_str}"
        })
    ]))


async def _group_poke(bot: Bot, event: Event) -> bool:
    value = (event.notice_type == "notify" and event.sub_type == "poke" and event.target_id == int(bot.self_id))
    return value


poke = on_notice(rule=_group_poke, priority=10, block=True)

@poke.handle()
async def _(bot: Bot, event: Event, state: T_State):
    if event.__getattribute__('group_id') is None:
        event.__delattr__('group_id')
    await poke.send(Message([
        MessageSegment("poke",  {
           "qq": f"{event.sender_id}"
       })
    ]))

