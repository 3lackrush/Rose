#!/usr/bin/env python
#--*-- coding:utf-8 --*--

#__author__ == 'Kios'

import os
import sys

class extraplugins(object):

	def __init__(self, plugin,disallow = []):
		self.dir_exploit = []
		self.disallow = ['__init__']
		self.disallow.extend(disallow)
		self.plugin = os.getcwd() + '/' + plugin
		sys.path.append(plugin)

	def list_plugin(self):

		def filter_func(file):
			if not file.endswith(".py"):
				return False
			for disfile in self.disallow:
				if disfile in file:
					return False
			return True
		dir_exploit = filter(filter_func, os.listdir(self.plugin))
		return list(dir_exploit)


	def work(self, url, html):
		for _plugin in self.list_plugin():
			try:
				m = __import__(_plugin.split('.')[0])
				spider = getattr(m, 'spider')
				p = spider()
				s = p.run(url, html)
			except Exception as e:
				print(e) 
