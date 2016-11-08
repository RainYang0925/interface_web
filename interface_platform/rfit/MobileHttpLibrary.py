# -*- coding: UTF-8 -*-
import time
import uuid
import httplib2
from pyDes import *
import base64
import hashlib
import binascii
import urllib
import json
import requests
import urllib2

reload(sys)
sys.setdefaultencoding('utf-8')


class MobileHttpLibrary:
    """Mobile Http Client"""
    global time
    time = long(time.time())
    global host
    host = 'https://kolibri.yixin.im/x'
    global port
    port = 0
    global login_port
    login_port = "102"
    global ticket_port
    ticket_port = "901"
    global web_ticket_port
    web_ticket_port = "900"

    def __init__(self):
        pass

    def __encrpyt(self, key, data):
        if len(key) != 8:
            print 'key length is not 16!'
            return None
        """DES对称加密"""
        k = des(str(key), ECB, pad=None, padmode=PAD_PKCS5)
        d = k.encrypt(str(data))
        """base64加密"""
        return base64.b64encode(d)

    def __decrypt(self, key, data):
        if len(key) != 8:
            print 'key length is not 16!'
            return None
        """base64解密"""
        d = base64.b64decode(data)
        """DES对称解密"""
        k = des(key, ECB, pad=None, padmode=PAD_PKCS5)
        destr = k.decrypt(d)
        return destr

    def __getkey(self, key1, unique):
        """generate the key of DES"""
        print 'uuid is ' + unique
        listuuid = []
        listuuid.append(unique[0:4])
        listuuid.append(unique[4:8])
        listuuid.append(unique[8:12])
        listuuid.append(unique[12:16])
        listuuid.append(unique[16:20])
        listuuid.append(unique[20:24])
        listuuid.append(unique[24:28])
        listuuid.append(unique[28:32])
        listcrc32 = []
        for element in listuuid:
            listcrc32.append(binascii.crc32(element))
        list32 = []
        for element in listcrc32:
            list32.append(element % 32)
        key = key1[list32[0]] + key1[list32[1]] + key1[list32[2]] + key1[list32[3]] + key1[list32[4]] + key1[
            list32[5]] + key1[list32[6]] + key1[list32[7]]
        print 'key is ' + key
        return key

    def __generate_sign(self, key, enbody, unique):
        """generate sign, sign = sha1(key+time+unique+enbody),then transform 16 byte string"""
        value = key + str(time) + str(unique) + str(enbody)
        h = hashlib.sha1()
        h.update(value)
        return h.hexdigest()

    def mobile_post(self, para, body, encryptkey="None", key1='a!onWY311h9cGV2L>>mxuQAx8Z#%z>+v', uid=''):
        """set mobile http post,para is json,necessary.body is json,necessary.ebcrykey is list,default value is None.
        key1 is necessary,default value is a!onWY311h9cGV2L>>mxuQAx8Z#%z>+v,uid is necessary,default value is '' """

        unique = str(uuid.uuid1()).replace('-', '')
        key = self.__getkey(key1, unique)
        bodykey = self.__getkey("a!onWY311h9cGV2L>>mxuQAx8Z#%z>+v", unique)

        """判断body里的参数是否要加密，如果是先加密"""
        if encryptkey == "None":
            pass
        else:
            dicbody = eval(body)
            print 'body is ' + body
            listen = eval(encryptkey)
            for element in listen:

                keys = dicbody.keys()
                if element in keys:
                    dicbody[element] = self.__encrpyt(bodykey, dicbody[element])
                else:
                    pass
            dicbody = str(dicbody).replace("'", "\"")

        """指定两种body:body里参数不需要加密，body里参数需要加密"""
        if encryptkey == "None":
            enbody = self.__encrpyt(key, body)
        else:
            enbody = self.__encrpyt(key, dicbody)

        """判断uid,登陆后的uid需要加密"""
        if uid == '':
            print "have no UID"
            pass
        else:
            uid = base64.b64encode(uid)

        """发送请求"""
        headers = {'Content-Type': 'text/plain', 'time': str(time), 'unique': unique,
                   'sign': self.__generate_sign(key1, enbody, unique), 'uid': uid, 'ua': 'IOS/162'}
        http = httplib2.Http()
        if para == 'None':
            url = self.__checkport()
        else:
            url = self.__checkport() + '?' + str(self.__encodepara(para))
        print 'HttpPost url is ' + url

        try:
            if type(eval(body)) == dict:
                http = httplib2.Http(".cache", disable_ssl_certificate_validation=True)
                resp, content = http.request(url, 'POST', headers=headers, body=enbody)
            # return resp
            else:
                print 'please confirm data type,data is not json'
        except Exception, e:
            raise e
        else:
            de_content = self.__decrypt(key, content)
            res_content = self.__replace_null(de_content)
            print 'send HttpPost successful! content is ' + res_content
            if res_content == "":
                # 如果body值为空,返回header
                http = httplib2.Http(".cache", disable_ssl_certificate_validation=True)
                resp, content = http.request(url, 'POST', headers=headers, body=enbody)
                print 'body is None, return headers: ' + str(resp)
                return str(resp).decode('utf-8')
            else:
                # print type(res_content)
                # 返回body值
                print "return body: "
                return res_content.decode('utf-8')

    def qrcode_get(self, url, uid, key2):

        uidencode = base64.b64encode(uid)
        # 手机端扫描二维码
        unique = str(uuid.uuid1()).replace('-', '')
        key = self.__getkey(key2, unique)

        # 计算签名
        value = key2 + uidencode + str(time)
        h = hashlib.sha1()
        h.update(value)
        sign = h.hexdigest()
        # 发送请求
        http = httplib2.Http()
        qrpara = {'uid': uidencode, 'timestamp': str(time), 'signature': sign, 'unique': unique}
        geturl = url + "&" + self.__encodepara(str(qrpara))
        print 'HttpGet url is ' + geturl
        try:
            http = httplib2.Http(".cache", disable_ssl_certificate_validation=True)
            resp, content = http.request(geturl, 'GET')
        except Exception, e:
            raise e
        else:
            de_content = self.__decrypt(key, content)
            res_content = self.__replace_null(de_content)
            print 'send HttpPost successful! content is ' + res_content
            return res_content.decode('utf-8')
        # print content

    def __encodepara(self, para):
        encodepara = urllib.urlencode(eval(para))
        return encodepara

    def __replace_null(self, response):
        strres = json.dumps(response, ensure_ascii=False)
        return eval(strres.replace('null', '\\"null\\"').replace('false', '\\"false\\"').replace('true', '\\"true\\"'))

    def __checkport(self):
        global host
        global port
        if port == 0:
            url = host
        else:
            url = host + ':' + str(port)
        return url

    def mobile_environment_config(self, h, p):
        """Set HTTP Request host and port,host and port is global variable.
        host default value is https://b.yixin.im,port default value is 0.

        Examples:
        | Environment Mobile Config| host | port |
        """
        global host
        global port
        host = h
        port = p
        print 'host is ' + h
        print 'port is ' + str(p)

    def get_app_oAuth(self, url, user, password, mac):
        """
        Examples:
        | Mobile Get OAuth| url | user | password | mac |
        | Mobile Get OAuth|"https://kolibrinest.yixin.im/contact"|"cyz1@yixin.im"|"Abc123456"|"D4-3D-7E-C8-12-75"|
        """

        ###获取重定向URL###
        r = requests.get(url)
        oAuthUrl = r.history[1].url

        ###去服务器拿临时票据ticket###
        # 调用102登录接口#
        para_login = str({"c": login_port})
        body_login = str(
            {"email": user.encode("utf-8"), "password": password.encode("utf-8"), "mac": mac.encode("utf-8")})
        res_login = self.mobile_post(para_login, body_login, '["password"]')
        res_json_login = json.loads(res_login)
        uid_login = str(res_json_login["result"]["uid"])
        key2_login = str(res_json_login["result"]["key2"])
        # 调用901获取应用免登票据#
        para = str({"c": ticket_port})
        body = '{"url": "' + oAuthUrl + '"}'
        sbody = str(body)
        res_ticket = self.mobile_post(para, sbody, "None", key2_login, uid_login)
        st = json.loads(res_ticket).get('result').get('st')

        ###oauth地址加上st参数,获取带code地址###
        url_st = oAuthUrl + "&st=" + st
        url_code = requests.get(url_st).url
        print url_code
        return url_code


if __name__ == '__main__':
    pass
# mobile = MobileHttpLibrary()
# mobile.qrcode_get("https://kolibriqrcode.yixin.im/qrcode/portal?code=9BDECF48-561C-4601-8977-8702FEC36290&qrcodeType=login&timestamp=1466159794&unique=5d3955d1347711e688b7d43d7ec81275&uid=WycyMTcnLCAneng2Q2ZTVjxAJk1%2BUTVYUlQhQmxNdWIkKTg5MnItJUgnXVswXQ%3D%3D&signature=e0233748780c53d62388a739c5f23c46eff51f98")
# oAuth = mobile.get_app_oAuth("https://kolibrinest.yixin.im/contact", "cyz1@yixin.im", "Abc123456", "D4-3D-7E-C8-12-75")
# print oAuth
# web_oAuth = mobile.web_get_oauth("https://inotice.qiye.yixin.im/manage/index", "chenyazhi@yixin.im", "Abc123456", "D4-3D-7E-C8-12-75")
# web_oAuth = mobile.web_get_oauth("https://inotice.qiye.yixin.im/bossNotice/index", "chenyazhi@yixin.im", "Abc123456", "D4-3D-7E-C8-12-75")

# print web_oAuth
# mobile.__encrpyt('2$R821+6','{\'name\':\'weiyating\'}')
# mobile.__decrypt('2$R821+6','fqvHJRtY/j528Arl9RXy1p01odr7bGkV')
# mobile.mobile_post("{\"c\":\"100\"}","{\"email\":\"liuyuxiaoee@yixin.im\",\"mac\":\"D4-3D-7E-C8-12-75\"}")
# mobile.environment_mobileconfig("https://kolibri.yixin.im",8)
# mobile.mobile_post("{\"c\":\"100\"}","{\"email\":\"liuyuxiaoee@yixin.im\",\"mac\":\"D4-3D-7E-C8-12-75\"}")
# unique = mobile.get_uuid()
# key = mobile.__getkey("a!onWY311h9cGV2L>>mxuQAx8Z#%z>+v",unique)
# password = mobile.__encrpyt(key,"sdfsadfsafsdafasf")
# print "password " + password
# mobile.mobile_post("{\"c\":\"101\"}","{\"email\":\"liuyuxiaoe@yixin.im\",\"name\":\"weiyating\",\"password\":\"" + password + "\",\"mac\":\"D4-3D-7E-C8-12-75\"}")
# res = mobile.mobile_post("{\"c\":\"102\"}","{\"email\":\"liuyuxiao@yixin.im\",\"password\":\"Abc123456\",\"mac\":\"D4-3D-7E-C8-12-75\"}","[\"password\"]")
# res = mobile.mobile_post("{\"c\":\"102\"}","{\"email\":\"cyz1@yixin.im\",\"password\":\"Abc123456\",\"mac\":\"D4-3D-7E-C8-12-75\"}","[\"password\"]")
# print res
# key2 = eval(res)['result']['key2']
# uid = eval(res)['result']['uid']
# print type(key2)
# print key2
# print uid
# res400 = mobile.mobile_post("{\"c\":\"400\"}","{\"userId\":\"" + uid + "\"}","None",key2,uid)
# print res400
# print "!!!!!!!!!!!!!!!!!!!-----------------------------------"
# mrs = mobile.mobile_post("{\"c\":\"419\"}","{\"email\":\"cyz1@yixin.im\",\"password\":\"Abc123456\",\"mac\":\"D4-3D-7E-C8-12-75\"}", "None", key2, "lalal")
# print mrs
