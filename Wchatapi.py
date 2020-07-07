# -*- coding: utf-8 -*-
import requests,json,ConfigParser,os

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Wchat:

    def __init__(self,url_token,corpid,corpsecret,url_send):
        self.url = url_token
        self.corpid = corpid
        self.corpsecret = corpsecret
        self.send_url = url_send

    def get_token(self):
        values = {'corpid':self.corpid,'corpsecret':self.corpsecret}
        self.header = {"Content-Type": "application/json"}
        req = requests.get(self.url,headers = self.header, params = values)
        data=json.loads(req.text)
        return data["access_token"]
    
    def send_message(self,access_token,AgentId,touser,message):
        i = 0
        msg = message.encode('utf-8')
        send_url = self.send_url + access_token       
        send_data = '{"msgtype": "text", "safe": "0", "agentid": %s, "touser": "%s", "text":{"content": "%s"}}' % (AgentId,touser,msg)
        result = requests.post(send_url, send_data)
        results = json.loads(result.content)
        resultcode = results["errcode"]
        print resultcode,i
        print type(resultcode)
        while resultcode == 42001 and i <= 3:
            if i == 4:
                print ('can not get access_token')
                exit()
            else:
                access_token = self.get_token()
                print access_token
                send_url = self.send_url + access_token
                result = requests.post(send_url, send_data)
                results = json.loads(result.content)
                resultcode = results["errcode"]
                i = i + 1
        return result.content
    
    def send_message(self,access_token,AgentId,touserList,message)
        for touser in touserList:
            self.send_message(access_token,AgentId,touser,message)

        