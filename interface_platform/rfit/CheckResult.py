# -*- coding: UTF-8 -*-
import json
import sys
import random
import mysql.connector
from mysql.connector import errorcode

reload(sys)
sys.setdefaultencoding('utf-8')
class CheckResult():
	global dbhost 
	dbhost= '10.164.96.67'
	global dbport 
	dbport = 6000
	global dbuser
	dbuser = 'kolibri_test'
	global dbpassword 
	dbpassword= '8w5orxBB'
	global dbdatabase
	dbdatabase = 'yxqy-test'

	"""docstring for CheckResult"""
	def __init__(self):
		pass

	def check_code(self,response,expectcode):
		"""Check HTTP response code.

		Examples:
        | Check | {"data":"null","code":"200","msg":"添加成功"}| 200 |
        """
		#strjson = json.dumps(response,ensure_ascii=False)
		try:
			dic = eval(response)
		except Exception, e:
			print 'Http response can not transfer to json,pelease check data format'
			raise e
		else:
			code = dic['code']
			if str(code)== expectcode:
				print 'response code ' + 'code' + ' is expectcode ' + expectcode
			else:
				raise AssertionError('response code ' + 'code' + ' is not expectcode ' + expectcode)

	def generate_random_int(self):
		""" generate random int between 1 and 999999
		"""
		randomInt = random.randint(1,999999)
		print 'generate random int is ' + str(randomInt)
		return randomInt

	def mysql_select(self,sql):
		""" Execute mysql SELECT statement,now it default handle the fist row of the select datas,
		if select one element,it return a string,if select multiple elements,it return a list.

		default host is 10.164.96.67,default port is 6000,default user is kolibri_test,default password
		is 8w5orxBB,default database is yxqy-test

		Examples:
		| Mysql Select | SELECT name FROM elf_activity_tab WHERE ID = 3|
		this examples return a string '云音乐'

		Examples:
		| Mysql Select | SELECT name,remark FROM elf_activity_tab WHERE ID = 3|
		this examples return a list {'云音乐','云音乐找茬大赛'}

		 """
		try:
			cnx = mysql.connector.connect(user=dbuser,password=dbpassword,host=dbhost,port=dbport,database=dbdatabase)
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print 'Something is wrong with your user name or password'
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				print 'Database does not exist'
			else:
				print (err)	
		else:
			print 'connect to database successful!,dburl is ' + dbhost + ":" + str(dbport)
			print 'user database ' + dbdatabase
		cursor = cnx.cursor(dictionary=True)
		try:
		    cursor.execute(sql)   
		except mysql.connector.Error as err:
			print err
		rows = cursor.fetchall()
		"""判断查询内容"""
		endn = sql.find('FROM')
		cutstr = sql[7:endn-1]
		spstr = cutstr.split(',')

		"""判断是否是全部查询"""
		if spstr[0] == '*':
			#print 'nonsupport select * ,please type accurate query condition'
			
			return len(rows)


		"""判断是否有数据返回"""
		if len(rows) == 0:
			print 'no data return'
			return
		#handle return data
		if len(spstr) == 1:
			print 'the value of ' + str(spstr[0]) + ' is ' + str(rows[0][spstr[0]])
			return str(rows[0][spstr[0]])
		else:
			listdata = []
			for element in spstr:
				print 'value of ' + element + ' is ' + str(rows[0][element])
				listdata.append(rows[0][element])
			return listdata
		cursor.close()
		cnx.close()

	def mysql_executesql(self,sql):
		"""Execute mysql statement except SELECT,it can handle like INSERT、DELETE and so on,
		default host is 10.164.96.67,default port is 6000,default user is kolibri_test,default 
		password,is 8w5orxBB,default database is yxqy-test"""
		try:
			cnx = mysql.connector.connect(user=dbuser,password=dbpassword,host=dbhost,port=dbport,database=dbdatabase)
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print 'Something is wrong with your user name or password'
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				print 'Database does not exist'
			else:
				print (err)	
		else:
			print 'connect to database successful!,dburl is ' + dbhost + ":" + str(dbport)
			print 'user database ' + dbdatabase
		cursor = cnx.cursor()
		try:
			cursor.execute(sql)
		except mysql.connector.Error as err:
			raise err
		cursor.close()
		cnx.close()

	def set_dbconfig(self,host,user,password,database,port):
		""""""
		global dbhost
		global dbuser
		global dbpassword
		global dbdatabase
		global dbport
		dbhost = host
		dbuser = user
		dbpassword = password
		dbdatabase = database
		dbport = port

if __name__ == '__main__':
	c = CheckResult()
	#c.check_code('{"data":"null","code":"400","msg":"公告类型名已存在!"}','400')
	#c.generate_random_int()
	#c.set_dbconfig("10.164.96.67",'sdfsadf','sdfsf','ee','6000')
	c.mysql_select("SELECT type FROM conf")

	#c.database_operation("show tables")

	

 


		


