import aiohttp
import re
import json

from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Event, Bot, Message, MessageSegment


# 检查直播状态

live_check = on_command('live_check ', aliases={'直播状态'})

@live_check.handle()
async def _(bot: Bot, event: Event, state: T_State):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.live.bilibili.com/xlive/web-room/v1/index/getRoomBaseInfo?room_ids=27936313&req_biz=video", headers={'Cache-Control': 'no-cache'}) as res:
            if res.status:
                msg = []
                r = json.loads(await res.text())
                if r['code'] == 0:
                    room = r['data']['by_room_ids']['27936313']
                    if room['live_status'] == 1:
                        msg.append(MessageSegment("text", {
                            "text": f"牛仔城直播已启动"
                        }))
                        msg.append(MessageSegment("image", {
                            "file": f"{room['cover']}"
                        }))
                        msg.append(MessageSegment("text", {
                            "text": f"{room['title']}\n直播间地址：{room['live_url']}"
                        }))
                    else:
                        msg.append(MessageSegment("text", {
                            "text": f"牛仔城直播未启动"
                        }))
                else:
                    msg.append(MessageSegment("text", {
                        "text", f"BILIBILI API请求失败"
                    }))
                await live_check.send(Message(msg))
            else:
                await live_check.send(Message([
                    MessageSegment("text", {
                        "text": f"BILIBILI API请求失败"
                    })
                ]))
