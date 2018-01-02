#!/usr/bin/env python
#--*-- coding:utf-8 --*--

import requests

class Downloader(object):

	def get(self, url):
		user_agent = {'User-agent': 'Mozilla/5.0'}
		r = requests.get(url,headers = user_agent, timeout=10)
		if r.status_code != 200:
			return None
		_str = r.text
		return _str

	def post(self, url, data):
		user_agent = {'User-agent': 'Mozilla/5.0'}
		r = requests.post(url, headers=user_agent, data)
		_str = r.text
		return _str

	def download(self, url, htmls):
		if url is None:
			return None

		_str = {}
		_str["url"] = url
		try:
			user_agent = {'User-agent': 'Mozilla/5.0'}
			r = requests.get(url, headers=user_agent, timeout=10)
			if r.status_code != 200:
				return None
			_str["html"] = r.text
		except Exception as e:
			return None

		htmls.append(_str)