from nonebot import on_notice
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot,Message,GroupIncreaseNoticeEvent,GroupDecreaseNoticeEvent,NoticeEvent
from random import randint, choice

# 处理群成员变动
group_member_event=on_notice()
@group_member_event.handle()
async def _(bot:Bot,event:GroupIncreaseNoticeEvent,state:T_State) :#-> None:
    msg = choice(
        [
            f'欢迎光临，客人{event.user_id}',
            f'[CQ:at,qq={event.user_id}]\n欢迎光临，这里有数不尽的乐趣'
        ]
    )
    await group_member_event.finish(msg)

@group_member_event.handle()
async def _(bot:Bot,event:GroupDecreaseNoticeEvent,state:T_State) :#-> None:
    await group_member_event.finish(f"{event.user_id} 离开了我们...")