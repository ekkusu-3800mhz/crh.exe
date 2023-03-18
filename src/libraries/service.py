from dotenv import load_dotenv
import aiohttp
import os
import time
import json


# 加载配置信息

load_dotenv()


# 定义API请求地址构建函数

def api_url(point: str) -> str:
    base = os.environ.get('API_BASE_URL')
    return str(base + "/" + point)


# 获取所有机厅排队情况

async def get_all():
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url('bot/queue_info')) as res:
            if res.status:
                return json.loads(await res.text())
            else:
                return {
                    "status": 500,
                    "data": {
                        "error": "HTTP request failed",
                    },
                }


# 设置指定机厅的人数

async def set_player(command, number):
    payload = {
        "unique_name": command,
        "player_count": number,
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(api_url('bot/queue_update'), data=payload) as res:
            if res.status:
                return json.loads(await res.text())
            else:
                return {
                    "status": 500,
                    "data": {
                        "error": "HTTP request failed",
                    },
                }
