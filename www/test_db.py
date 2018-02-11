'''
连接池打开后要记得关闭
在orm.py中加入摧毁池的函数#22行
数据库中emil是唯一，每执行一次记得修改
'''
import orm,asyncio
from models import User,Blog,Comment
@asyncio.coroutine
async def test(loop,**kw):
    await orm.create_pool(loop=loop,user='www-data', password='www-data', db='awesome')
    u = User(name=kw.get('name'), email=kw.get('email'), passwd=kw.get('passwd'), image=kw.get('image'))
    await u.save()
    await orm.destory_pool()
data=dict(name='gaf', email='2@qq.com', passwd='1312345', image='about:blank')
loop=asyncio.get_event_loop()
loop.run_until_complete(test(loop,**data))
loop.close()