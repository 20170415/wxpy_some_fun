from wxpy import *
import time
import random
import datetime
import os
import subprocess
import qm

bot = Bot(qr_path='image.png')
bot.enable_puid('wxpy_puid.pkl')
all_friends = bot.friends()
myself = bot.self

@bot.register(Friend, TEXT)
def deal_msg(msg):
	text = msg.text.split('###')
	if len(text) != 2:
		return
	if text[0] == 'clear':
		print (msg.sender.puid + msg.text)
		subprocess.Popen('python wechat_clear.py', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		time.sleep(2)
		msg.sender.send_image('image')
	elif text[0] == 'name':
		print (msg.sender.puid + msg.text)
		parm = text[1].split(':')
		if len(parm) != 2:
			return
		qm.qm(parm[0], parm[1])
		time.sleep(3)
		image_name = parm[1] + '.jpg'
		print ('send image start')
		try:
			msg.sender.send_image(image_name)
		except Exception as e:
			print (e)
		print ('send image ok')
		time.sleep(2)
		
bot.join()
