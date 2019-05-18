#encoding=utf-8
from wxpy import *
import time
import random
import datetime
import os
import logging

bot = Bot(qr_path='image')

all_friends = bot.friends()
myself = bot.self

name_b = myself.name.encode('utf-8')
name = name_b.decode('utf-8')
logger = logging.getLogger(name + '.log')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(name_b, encoding='utf-8')
fh.setLevel(logging.DEBUG)
# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

logger.info('----------------BEGIN----------------')

logger.info(u"检测到你联系人共计: "+ str(len(all_friends)) + u" 人")
bot.file_helper.send('准备开始检测僵尸粉！')
bot.file_helper.send('你联系人共有:' + str(len(all_friends)) + '人')
index = 1;
for user in all_friends:
    time.sleep(random.randint(0,9))
    try:
        if user != myself:
            #import pdb;pdb.set_trace()
            logger.info(u"["+str(index)+"/"+str(len(all_friends))+"] "+ user.name)
            user.send('hello జ్ఞా ')
    except ResponseError as e:
        logger.info(str(e.err_code) + e.err_msg) 
    index += 1
    if (index % 10) == 0:
        bot.file_helper.send('正在检测第 ' + str(index) + '个')

logger.info("检测已执行完毕请到手机微信app中处理")
bot.file_helper.send('检测已执行完毕,感谢')
logger.info('----------------END----------------')   
