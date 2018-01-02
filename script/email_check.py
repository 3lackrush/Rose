#!/usr/bin/env python
#--*-- coding:utf-8 --*--
#__author__ == 'Kios'

import re
from termcolor import colored

class spider():

	def run(self, url, html):
		try:
			real_email_list = []
			pattern = re.compile(r'([\w-]+@[\w-]+\.[\w-]+)+')
			email_list = re.findall(pattern, html)
			avoid_pic = ['png','jpeg','ico','bmp','PNG','JPEG','ICO','BMP']
			for _email in email_list:
				if _email.split(".")[-1] in avoid_pic:
					pass
				else:
					real_email_list.append(_email)
		except Exception as e:
			pass

		if(real_email_list):
			print(colored("  [+] Email Address Found! ","red"), real_email_list)
			return True
			
		return False
