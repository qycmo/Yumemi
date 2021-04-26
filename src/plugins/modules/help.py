import os
import json

from nonebot import on_message,on_command
from nonebot.adapters.cqhttp import Bot, MessageEvent
from nonebot.typing import T_State
from nonebot.rule import to_me

__doc__ = """
查询命令用法
权限组：所有人
用法：
  help
  help list
  help info (cmd)
"""
TOP_MANUAL='''
=====================
- YumemiBot使用说明 -
=====================
发送方括号[]内的关键词即可触发
[功力]只能@机器人和私聊生效
'''.strip()

help_list={
    '功力':'格式:角色名 角色所在区服',
}
helps=on_command("help",rule=to_me())
@helps.handle()
async def _helpbot(bot:Bot,event:MessageEvent,state:T_State):
    msg = str(event.message).split( )
    if len(msg)==0:
        msg = (
            "呀？找不到路了？\n"
            "help list 查看可用命令列表\n"
            "咱只能帮你这么多了qwq"
        )
        await helps.finish(msg)
    elif len(msg)>0:
        if msg[0]=='list':
            await bot.send(event, TOP_MANUAL)
        elif msg[0]=='info':
            if msg[1]=='功力':
                await helps.finish(help_list['功力'])
            else:
                await bot.send(event, '您查询的功能不存在')
        else:
            await bot.send(event, '您的输入有误')
    else:
        await helps.finish(event, '异常，请报告机器人管理者')