import  requests
#导入网页请求库
import json
#导入json数据格式
import time
from random import randint, choice
from nonebot import on_message,on_command
from nonebot.adapters.cqhttp import Bot, GroupMessageEvent,Message,MessageEvent
from nonebot.typing import T_State
from nonebot.rule import to_me

def tixing(sex):
    if  sex==0:
        return "成男"
    elif sex==1:
        return "成女"
    elif sex==2:
        return "少女"
def men(menpai):
    if menpai==0:
        return "真武"
    elif menpai==1:
        return "太白"
    elif menpai==2:
        return "神威"
    elif menpai==3:
        return "丐帮"
    elif menpai==4:
        return "唐门"
    elif menpai==5:
        return "五毒"
    elif menpai==6:
        return "少林"
    elif menpai==7:
        return "天香"
    elif menpai==8:
        return "神刀"
    elif menpai==9:
        return "移花"
    elif menpai==10:
        return "从龙" 
def server(sev):#用于将爬取到的服务器代号转换为服务器名字
    if sev==1546:
        return "青龙乱舞-吹雪"
    elif sev==522:
        return "青龙乱舞-孔雀翎"
    elif sev==266:
        return "青龙乱舞-长生剑"
    elif sev==276:
        return "大地飞鹰-凤凰集"
    elif sev==788:
        return "大地飞鹰-彼岸花"
    elif sev==1044:
        return "大地飞鹰-千秋月"
    elif sev==269:
        return "沧海云帆-青龙永夜"
    elif sev==1549:
        return "沧海云帆-锦鲤抄"
    elif sev==2317:
        return "沧海云帆-凤求凰"
    elif sev==317:
        return "欢乐英雄"
    elif sev==270:
        return "把酒邀月-云水在天"
    elif sev==526:
        return "把酒邀月-拈花一笑"
    elif sev==1038:
        return "把酒邀月-指月临风"
    elif sev==1294:
        return "把酒邀月-幽夜从龙"
    elif sev==1550:
        return "把酒邀月-玄甲玉京"
def kong(str):
    if str=='':
        return ''
    elif str!='':
        return '\n曾用名:'+str
def servers(sev):
    if sev=="吹雪":
        return 1546
    elif sev=="孔雀翎":
        return 522
    elif sev=="长生剑":
        return 266
    elif sev=="凤凰集":
        return 276
    elif sev=="彼岸花":
        return 788
    elif sev=="千秋月":
        return 1044
    elif sev=="青龙永夜":
        return 269
    elif sev=="锦鲤抄":
        return 1549
    elif sev=="凤求凰":
        return 2317
    elif sev=="欢乐英雄":
        return 317
    elif sev=="云水在天":
        return 270
    elif sev=="拈花一笑":
        return 526
    elif sev=="指月临风":
        return 1038
    elif sev=="幽夜从龙":
        return 1294
    elif sev=="玄甲玉京":
        return 1550

gongli=on_command('功力',to_me())
@gongli.handle()
async def _gongli(bot:Bot,event:MessageEvent,state:T_State):
    msg=str(event.message).split( )
    url='https://www.tdjingling.com/api/server/get_rank'
    #网页链接
    if len(msg)==1:
        tracking_number=msg[0]
        serviceID='0'
    elif len(msg)==2:
        tracking_number=msg[0]
        serviceID=servers(msg[1])
    params={
        #是requests的一个方法，把字符串逐个添加进去
        'q': 'rank',
        'currentPage': '1',#当前页页码
        'pageSize': '10',#每页显示数
        'serviceID': serviceID,#服务器ID
        'sortMethod': 'gongli',#当前查询项为功力
        'sortBy': 'desc',
        'searchKeyword': tracking_number,#查询
        'class': '0'    #门派
    }
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }

    res=requests.post(url=url,data=params,headers=headers)
    res=res.json()
    res=res['data']
    res=res['roleInfo']
    i=0
    for item in res:
        role_name=res[i]['role_name']
        service_id=server(res[i]['service_id'])
        menpai=men(res[i]['class'])
        sex=tixing(res[i]['sex'])
        used_name1=kong(res[i]['used_name1'])
        used_name2=kong(res[i]['used_name2'])
        create_name=res[i]['create_name']
        gongli=str(res[i]['gongli'])
        max_gongli=str(res[i]['max_gongli'])
        gang_name=res[i]['gang_name']
        alliance_name=res[i]['alliance_name']
        i=i+1
        await bot.send(event, f'昵称:'+role_name+'\n服务器:'+service_id+'\n门派:'+menpai+'\n体型:'+sex+used_name1+used_name2+'\n创角名:'+create_name+'\n功力:'+gongli+'\n最大功力:'+max_gongli+'\n帮派:'+gang_name+'\n联盟:'+alliance_name)
        time.sleep(1)