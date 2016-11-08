# -*- coding: UTF-8 -*-
import urllib2
import cookielib
import config
import urllib
import httplib2
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import poster
import json
import sys
import base64
import requests

reload(sys)
sys.setdefaultencoding('utf-8')

class HttpLibrary(object):
	"""Http Client"""

	global host
	# host = 'https://my.qiye.yixin.im'
	host = 'https://super.qiye.yixin.im'
	# host = 'http://10.164.96.78'
	global port
	port = "0"
	# port = "8184"
	global ticket_path
	ticket_path = "http://10.164.96.78:8184/app/system/getAppAuthTicketFromWeb"

	def __init__(self):
		pass

	def get_cookie(self,username,password):
		"""Get cookie from username and password.

		Examples:
        | Get Cookie | username | password |
        """
		print 'start to getcookie'
		cookie = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
		postdata = urllib.urlencode({'email':username,'password':password})
#		url = self.__checkport() + '/login/in' + '?' + postdata
		url = self.__checkport() + '/login/in'
		print 'HttpPost url is ' + url
		try:
#			response = opener.open(url)
			response = opener.open(url, postdata)      
		except urllib2.URLError as e:
			if hasattr(e,'reason'):
				print 'getcookie failed!'
				print 'reason is ' + e.reason
			elif hasattr(e,'code'):
				print 'getcookie failed!'
				print 'reson is ' + e.reason + ',error code is '
			else:
				print 'getcookie failed! the error is not URLError and HTTPError'
		else:
			content = response.read()
			print 'get cookie sussessful,getcookie response is ' + str(content).decode('utf-8')
			return response.info()['Set-Cookie']

	def get_admin_cookie(self,username,password):
		"""Get admin cookie from username and password.

		Examples:
        | Get Admin Cookie | username | password |
        """
		print 'start to getadmincookie'
		cookie = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
		postdata = urllib.urlencode({'account':username,'password':password})
		url = 'https://super.qiye.yixin.im' + '/checkLogin?'
		print 'HttpPost url is ' + url
		try:
			response = opener.open(url, postdata)
		except urllib2.URLError as e:
			if hasattr(e,'reason'):
				print 'getadmincookie failed!'
				print 'reason is ' + e.reason
			elif hasattr(e,'code'):
				print 'getadmincookie failed!'
				print 'reson is ' + e.reason + ',error code is '
			else:
				print 'getadmincookie failed! the error is not URLError and HTTPError'
		else:
			content = response.read()
			print 'get admin cookie sussessful,getcookie admin response is ' + str(content).decode('utf-8')
			return response.info()['Set-Cookie']


	def web_get(self,path,parameter,cookie):
		"""Issues a HTTP GET request,parameter should be a python dict,this method return a string object.

		Examples:
        | ${res} | WEB Get | /foo/bar.do | {'foo': '1','bar': '2'} | cookie |
		"""
		if parameter == 'None':
			url = self.__checkport() + path
		else:
			#url = self.__checkport() + path + '?' + str(self.__generate_url(parameter))
			url = self.__checkport() + path + '?' + str(self.__encodepara(parameter))
		print 'HttpGet request url is ' + url
		res = urllib2.Request(url)
		res.add_header('Accept','application/json')
		res.add_header('Content-Type','application/x-www-form-urlencoded')
		res.add_header('Cookie',cookie)
		try:
			response = urllib2.urlopen(res)
		except urllib2.URLError as e:
			if hasattr(e,'reason'):
				print 'send HttpGet failed!'
				print 'reason is ' + e.reason
			elif hasattr(e,'code'):
				print 'send HttpGet failed!'
				print 'reason is ' + e.reason + ',error code is ' + e.code
			else:
				print 'send HttpGet failed! the error is not URLError and HTTPError'
		else:
			info = self.__replace_null(response.read())
			print 'HttpGet response is ' + str(info)
			return info.decode('utf-8')


	def web_post(self,path,para,data,cookie,uid=''):
		"""Issues a HTTP POST request,parameter should be a python dict,data is post entity, this method return a string object.

		Examples:
        | ${res} | WEB POST | /foo/bar.do | {'foo': '1','bar': '2'} | {"foo": {"bar": [1,2,3]}} | cookie |

        | ${res} | WEB POST | /foo/bar.do | {'foo': '1','bar': '2'} | None | cookie |
		"""
		http = httplib2.Http()
		headers = {'Accept':'application/json','Content-Type':'application/x-www-form-urlencoded','Cookie': cookie, 'uid':uid}
		headers1 = {'Accept':'application/json','Content-Type':'application/json','Cookie': cookie, 'uid':uid}
		if para == 'None':
			if "http" in path:
				url = path
				print "chenyazhi test url:  ", url
			else:
				url = self.__checkport() + path
		else:
			#url = self.__checkport() + path + '?' + str(self.__generate_url(para))
			url = self.__checkport() + path + '?' + str(self.__encodepara(para))
		print 'HttpPost url is ' + url
		try:
			if data == 'None':
				http = httplib2.Http(".cache", disable_ssl_certificate_validation=True)
				response,content = http.request(url,'POST',headers = headers)
				res_content = self.__replace_null(content)
				print 'send HttpPost successful! content is ' + res_content
				return res_content.decode('utf-8')
			else:
				if type(eval(data)) == dict:
					http = httplib2.Http(".cache", disable_ssl_certificate_validation=True)
					response,content = http.request(url,'POST',headers = headers1,body = json.dumps(eval(data)))
					res_content = self.__replace_null(content)
					print 'send HttpPost successful! content is ' + res_content
					return res_content.decode('utf-8')
				else:
					print 'please confirm data type,data is not json'
		except Exception, e:
			raise e
		
	def __generate_url(self,parameter):
		"""generate url from parameter"""
		parameter = eval(parameter)
		para = ''
		for key in parameter.keys():
			para = str(para) + key + '=' + parameter.get(key) + '&'
		url = para[:-1]
		return url

	def web_delete(self,path,parameter,data,cookie):
		"""Issues a HTTP DELETE request,parameter should be a python dict,data is delete entity, this method return a string object.

		Examples:
        | ${res} | WEB DELETE | /foo/bar.do | {'foo': '1','bar': '2'} | {"foo": {"bar": [1,2,3]}} | cookie |
        | ${res} | WEB DELETE | /foo/bar.do | None | {"foo": {"bar": [1,2,3]}} | cookie |
		"""
		headers = {'Accept':'application/json','Content-Type':'application/x-www-form-urlencoded','Cookie': cookie}
		headers1 = {'Accept':'application/json','Content-Type':'application/json','Cookie': cookie}
		if parameter == 'None':
			url = self.__checkport() + path
		else:
			#url = self.__checkport() + path + '?' + str(self.__generate_url(parameter))
			url = self.__checkport() + path + '?' + str(self.__encodepara(parameter))
		print 'HttpDelete url is ' + url
		if data == 'None':
			request = urllib2.Request(url,headers = headers)
		else:
			if type(eval(data)) == dict:
				request = urllib2.Request(url,data = urllib.urlencode(data),headers = headers1)
			else:
				print 'please confirm data type,data is not json'
		request.get_method = lambda:'DELETE'
		opener = urllib2.build_opener()
		try:
			#response = urllib2.urlopen(request)
			response = opener.open(request)
		except Exception, e:
			raise e
		else:
			info = self.__replace_null(response.read())
			print 'HttpDelete response is ' + info
			return info.decode('utf-8')

	def web_put(self,path,parameter,data,cookie):
		"""Issues a HTTP PUT request,parameter should be a python dict,data is put entity, this method return a string object.

		Examples:
        | ${res} | WEB PUT | /foo/bar.do | {'foo': '1','bar': '2'} | {"foo": {"bar": [1,2,3]}} | cookie |
        | ${res} | WEB PUT | /foo/bar.do | {'foo': '1','bar': '2'} | None | cookie |
		"""
		headers = {'Accept':'application/json','Content-Type':'application/x-www-form-urlencoded','Cookie': cookie}
		headers1 = {'Accept':'application/json','Content-Type':'application/json','Cookie': cookie}

		if parameter == 'None':
			url = self.__checkport() + path
		else:
			#url = self.__checkport() + path + '?' + str(self.__generate_url(parameter))
			url = self.__checkport() + path + '?' + str(self.__encodepara(parameter))
		print 'HttpPut url is ' + url
		http = httplib2.Http()
		try:
			if data == 'None':
				http = httplib2.Http(".cache", disable_ssl_certificate_validation=True)
				response,content = http.request(url,'PUT',headers = headers)
			elif data != 'None':
				if type(eval(data)) == dict:
					http = httplib2.Http(".cache", disable_ssl_certificate_validation=True)
					response,content = http.request(url,'PUT',headers = headers1,body = json.dumps(eval(data)))
				else:
					print 'please confirm data type,data is not json'
			else:
				info = self.__replace_null(str(content))
				print 'Send HttpPut successful,content is ' + info
				return info.decode('utf-8')
		except Exception, e:
			raise e

	def web_post_file(self,path,parameter,entity,cookie):
		"""Issues a HTTP POST FILE request,url is the URL relative to the server root,parameter should be a python dict,this method return a string object.

		Examples:
        | ${res} | WEB POST FILE | https://b.yixin.im/addCodeConf.p | {'file':open('Resources/Material/codeConf.csv','rb'),'name':'text码活动ffd'}| cookie |
		"""
		if parameter == 'None':
			url = self.__checkport() + path
		else:
			url = self.__checkport() + path + '?' + str(self.__encodepara(parameter))
		opener = poster.streaminghttp.register_openers()
		datagen,headers = poster.encode.multipart_encode(eval(entity))
		res = urllib2.Request(url,datagen,headers)
		res.add_header('Cookie',cookie)
		try:
			response = urllib2.urlopen(res)
		except Exception, e:
			raise e
		else:
			info = self.__replace_null(response.read())
			print 'send file successful,http response is ' + info
			return info.decode('utf-8')

	def web_post_filebyte(self,path,para,entity):
		"""this keyword is for openplatform to post file.

		Examples:
		| ${res} | WEB POST FILEBYTE | /cgi-bin/file/upload | {'access_token':'ACCESS_TOKEN'} | {'content':'Resources/Material/logo.jpg','type':'jpg'}
		"""
		if type(eval(entity)) != dict:
			print 'entity must be dict'
			return
		else:
			entitydict = eval(entity)
			filename = entitydict['content']
			f = open(filename,'rb')
			fbyte = f.read()
			enbyte = base64.b64encode(fbyte)
			entitydict['content'] = enbyte
			res = self.web_post(path,para,str(entitydict),'None')
			return res

	def __replace_null(self,response):
		strres = json.dumps(response,ensure_ascii=False)
		return eval(strres.replace('null','\\"null\\"').replace('false','\\"false\\"').replace('true','\\"true\\"'))

	def web_environment_config(self,h,p):
		"""Set HTTP Request host and port,host and port is global variable.
		host default value is https://b.yixin.im,port default value is 0.

		Examples:
        | WEB Environment Config| host | port |
		"""
		global host
		global port
		host = h
		port = p
		print 'host is ' + h
		print 'port is ' + str(p)

	def __checkport(self):
		global host
		global port
		if port == "0":
			url = host
		else:
			url = host + ':' + str(port)
		return url

	def __encodepara(self,para):
		encodepara = urllib.urlencode(eval(para))
		return encodepara

	def web_formdatapost(self, path, para, data, cookie):
		http = httplib2.Http()
		headers = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded', 'Cookie': cookie}
		if para == 'None':
			url = self.__checkport() + path
		else:
			# url = self.__checkport() + path + '?' + str(self.__generate_url(para))
			url = self.__checkport() + path + '?' + str(self.__encodepara(para))
		print 'HttpPost url is ' + url
		try:
			http = httplib2.Http(".cache", disable_ssl_certificate_validation=True)
			response, content = http.request(url, 'POST', headers=headers, body=data)
			res_content = self.__replace_null(content)
			print 'send HttpPost successful! content is ' + res_content
			return res_content.decode('utf-8')

		except Exception, e:
			raise e


	def web_get_oauth(self, my_qiye_url,cookie, appKey, uid):
		'''
		内部系统访问外部应用接入OAuth免登
		使用时,需要开始VPN
		:param my_qiye_url: 未跳转前的url,如重要通知:"https://my.qiye.yixin.im/app/manageUrl?appId=613&url=https://inotice.qiye.yixin.im/manage/index"
		:param cookie: 后台普通管理员的cookie
		:param appKey: 大后台查看appKey
		:param uid: 后台普通管理员的uid,和获取cookie的管理员同一个
		:return:  带code的url

				Examples:
        | Web Get Oauth| my_qiye_url | cookie | appKey | uid |
		'''

		global ticket_path
		###获取url值###
		redirect_uri  = self.get_id_from_url(my_qiye_url, "url")

		###获取内部Web免登票据###
		# path = "http://10.164.96.78:8184/app/system/getAppAuthTicketFromWeb"
		para = 'None'
		data = '{"appid": "' + appKey + '"}'
		res_ticket = self.web_post(ticket_path ,'None', data, cookie,uid)
		st = json.loads(res_ticket).get('result').get('st')

		oauth_url = "https://oauth-test.qiye.yixin.im/authorize?response_type=code&client_id="+appKey+"&st="+st+"&redirect_uri="+redirect_uri
		url_code = requests.get(oauth_url).url
		return url_code


	def get_id_from_url(self, url, id):
		"""
		获取url里的关键字的值.
		比如 url="https://my.qiye.yixin.im/app/manageUrl?appId=613&url=https://inotice.qiye.yixin.im/manage/index"
		需要获取appId的值,在id处传入参数 "appId"
		"""
		if "?" not in url:
			print "The url is indissociable "
		else:
			spliturl = url.split("?")
			url_body = spliturl[1].split("&")
			print url_body
			for r in url_body:
				if id in r:
					id_long = len(id)
					print r[id_long+1:]
					return r[id_long+1:]
		print "There have not "+id

	def get_url_cookie(self, url):
		print 'start to getcookie'
		cookie = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

		print 'HttpPost url is ' + url
		try:
			response = opener.open(url)
		except urllib2.URLError as e:
			if hasattr(e, 'reason'):
				print 'getcookie failed!'
				print 'reason is ' + e.reason
			elif hasattr(e, 'code'):
				print 'getcookie failed!'
				print 'reson is ' + e.reason + ',error code is '
			else:
				print 'getcookie failed! the error is not URLError and HTTPError'
		else:
			content = response.read()
			print 'get cookie sussessful,getcookie response is ' + str(content).decode('utf-8')
			return response.info()['Set-Cookie']


if __name__ == '__main__':
	pass
	# h = HttpLibrary()
	# cookie = h.get_admin_cookie("numen_dev@163.com", "Admin123")
	# print cookie
	# cookie = h.get_cookie("chenyazhi@yixin.im", "Abc123456")
	#
	# r = h.web_get_oauth("https://my.qiye.yixin.im/app/manageUrl?appId=613&url=https://inotice.qiye.yixin.im/manage/index", cookie, "bossnotice", "130")
    #
	# ###管理员登录###
	# r = h.web_post("/checkLogin", "{'account':'chenyazhi@yixin.im','password':'Abc123456'}", "None", "NTESkolibri-adminSI=1658DE8D79232165A1E7A4AD47C77A79.hzabj-kolibri-1.server.163.org-8016; Path=/; HttpOnly")
	# print r

	# web_get(self,path,parameter,cookie):
	# print "!!!!!!!!!!!!!!!!!!!!!"
	# r = h.web_get('/smsquota/getCompanyInfo','{"domain":"yixin.im"}',cookie)
	# print r

	# h.get_id_from_url("https://my.qiye.yixin.im/app/manageUrl?appId=613&url=https://inotice.qiye.yixin.im/manage/index", "appId")


	#cookie = h.get_cookie('interfacetest@jiekou.com','Admin123')
	# h.web_post_filebyte('/cgi-bin/file/upload','{"access_token":"718ad40d0fbc4eba89621f86e0d23313"}','{"content":"Resources/Material/logo.jpg","type":"jpg"}')
	


			

			
		

		
