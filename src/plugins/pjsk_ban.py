import re

from nonebot import on_command, on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Event, Bot


# 禁言调用PJSK表情包的用户

pjsk_ban = on_regex(r"^(pjsk|PJSK)$")

@pjsk_ban.handle()
async def _(bot: Bot, event: Event, state: T_State):
    regex = "^(pjsk|PJSK)$"
    res = re.match(regex, str(event.get_message()).lower()).groups()
    print(res)
    if res[0]:
        await bot.set_group_ban(
            group_id=event.group_id,
            user_id=event.user_id,
            duration=43200
        )
