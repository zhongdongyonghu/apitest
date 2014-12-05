#!/usr/bin/python
# -*- encoding: utf-8 -*-
#
__author__ = 'liwei'
__date__ = '2014-12-5'


import urllib
import urllib2
import json
import subprocess
import shlex
import urlparse
from urlparse import urlparse
import os
import sys
import time
import hashlib
import logging
import requests
import traceback
import collections
import logging.config
import subprocess
import requests
import re
import sys
from jsonschema import validate
from jsonschema import ValidationError
from jsonschema import Draft4Validator

from vela_item_get1 import vela_item_get

project_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, project_path)
reload(sys)
sys.setdefaultencoding('utf8')

from urlparse import parse_qs,urlunparse


Zeus_LITB_IP='192.168.66.51'#'166.78.222.125'#'23.253.5.32'#'166.78.222.125'
#Zeus_MINI_IP='166.78.222.126'#'23.253.5.30'#'166.78.222.126'
Zeus_PORT='8081'#'80'

Vela_LITB_IP='166.78.222.125'#'192.168.66.51'
#Vela_MINI_IP='166.78.222.126'
Vela_PORT='80'

##192.168.66.137  zeus-m.lightinthebox.com
#192.168.66.137 litb-api.tbox.me
Sign_LITB_IP='192.168.66.137'
Vela_PORT='8081'

#需要替换某些参数的url---(之后可以读文件)
caseurl="http://zeus-m.lightinthebox.com/api/rest/app_server.php?client=vela&format=json&method=vela.item.get&app_key=V06GF3A2&app_secret=f838905ddd031399ffdm8n3mymrrzomk&v=1.1&sign_method=md5&timestamp=2014-11-19+11%3A39%3A49&language=en&currency=USD&sid=qmb6t2279ug76bqs4ahifk5tr0&fields=&item_id=1021065&is_hd=false&keys=client,format,method,app_key,app_secret,v,sign_method,timestamp,language,currency,sid,fields,item_id,is_hd&sign=E51A6BE0DA94220B76E08228DD89C9A7"

#post 加密
#--->需要替换后加密的key
regularkey="sid"

#--->需要更换的值
regularvalue="vl6tg1sk2489mcpm4lt650k2o5"#"90340c11786d4e458bb5e2b42faed30b"





#将需要更新参数值的请求串解析，替换参数值
#newzeusurl = "http://192.168.66.137:8080/api/v1/searches/categorySearch?cid=71&currency=USD&language=en&page_no=1&page_size=10&sid=3230a98742404f4bdc1e849f9c6375eb&app_key=V06GF3A2&sign=9C4601CCEACE07B58878E978FBE2F37F"
def Updata_url_paramvalue(caseurl,regularkey,regularvalue):
    url=caseurl
    uri=urlparse( url)
    print uri.query
    uri_query=uri.query
    #---------2014-12-1------------------------
    if uri_query.find("=&")>0:
        uri_query_paramlist=uri_query.split('&')
        print uri_query_paramlist
        uri_query_paramdict={}
        for uri_query_p in uri_query_paramlist:
            uri_query_paramdict[uri_query_p.split('=')[0]]=uri_query_p.split('=')[1]
        print uri_query_paramdict

        #重新赋值
        #print params[regularkey]
        uri_query_paramdict[regularkey]=regularvalue
        print uri_query_paramdict[regularkey]
        #print params[regularkey]
        print uri_query_paramdict
        newParams=uri_query_paramdict

        print "=====test======="
    else:
        print "传入的修改key&value："
        print regularkey
        print regularvalue

        newParams = {}
        params = parse_qs(uri.query)
        print "----params:----"
        print params
        for param in params:
            paramValue = params[param]
            newParams[param] = paramValue[0]
            print param + "=" + newParams[param]
            #重新赋值
        #print params[regularkey]
        newParams[regularkey]=regularvalue
        print newParams[regularkey]
        #print params[regularkey]
        print newParams


    paramsjoinlist=[]
    paramq=""
    for paramj in newParams:
        value=newParams[paramj]
        paramsjoinlist.append(paramj+"="+value)


    for paramandparam in paramsjoinlist:
        paramandparam +="&"
        paramq +=paramandparam

    query=paramq.strip('&')
    #uri.query=query
    newreq=urlunparse((uri.scheme, uri.netloc, uri.path, uri.params, query, uri.fragment))
    return newreq


def ZeusApi_v1_to_sign(change_Param_Url):
    sign_url="http://zeus-m.lightinthebox.com:8081/api/v1/admin/sign?url=http%3A%2F%2Fzeus-m.lightinthebox.com%2Fapi%2Frest%2Fapp_server.php%3Fclient%3Dvela%26format%3Djson%26method%3Dvela.sys.sessionid.get%26app_key%3DV06GF3A2%26app_secret%3Df838905ddd031399ffdm8n3mymrrzomk%26v%3D1.1%26sign_method%3Dmd5%26timestamp%3D2014-11-26%2B12%253A31%253A33%26language%3Den%26currency%3DUSD%26sid%3Dlnosnvfep4hsva3utndphl61p7%26keys%3Dclient%2Cformat%2Cmethod%2Capp_key%2Capp_secret%2Cv%2Csign_method%2Ctimestamp%2Clanguage%2Ccurrency%2Csid%26sign%3DBE5AD11E1D2133EB74D067FFC6135856&sid=lnosnvfep4hsva3utndphl61p7&app_key=V06GF3A2&sign=D41D8CD98F00B204E9800998ECF8427E"
    #zeusURL = 'http://%s:%s/api/rest/app_server.php' % (Zeus_LITB_IP, Zeus_PORT)
    regularurl=change_Param_Url
    payload_sign = {
        'url':regularurl ,
        'method': '',
        'sid': '253ehps5jdt2jkfgc55ep9imc2'#此处可以任何值没有影响
    }

    signparam_urlencode = urllib.urlencode(payload_sign)
    signrequrl = sign_url
    signreq = urllib2.Request(url = signrequrl,data =signparam_urlencode)
    #print signreq
    #新的加密后的sign
    signres_data = urllib2.urlopen(signreq)
    new_sign = signres_data.read()
    print "new_sign:"
    new_sign_dict= eval(new_sign)
    print new_sign_dict['info']
    new_sign_value=new_sign_dict['info']
    #return new sign
    return new_sign_value

def ZeusApi_copy_vela(Change_Param_Url):
    old_sign_urlparse = urlparse( Change_Param_Url )
    old_sign_newParams = {}
    old_sign_urlparams = parse_qs(old_sign_urlparse.query)
    print old_sign_urlparams
    for old_sign_param in old_sign_urlparams:
        old_sign_paramValue = old_sign_urlparams[old_sign_param]
        old_sign_newParams[old_sign_param] = old_sign_paramValue[0]

    print old_sign_newParams
    old_sign_urlkeys = old_sign_newParams['keys'].split(',')
    print old_sign_urlkeys
    old_sign_urlkeys.sort()
    tmp = ''

    for i in old_sign_urlkeys:
        #print i
        #print old_sign_newParams[i]
        if old_sign_newParams.has_key( i ):
            tmp += '%s%s' % (i, old_sign_newParams[i])
        else:
            tmp += '%s%s' % (i, "")
    print "tmp:" + tmp
    m = hashlib.md5(tmp)
    #新的加密后的sign
    old_sign_newParams['sign'] = m.hexdigest().upper()
    print old_sign_newParams['sign']
    old_newsign=old_sign_newParams['sign']
    return old_newsign



def Change_params_in_case(data_file, report_name,regularkey,regularvalue):

    lines = open(os.path.join(project_path, 'data', data_file)).readlines()
    runTimeString= time.strftime('%Y%m%d_%H%M', time.localtime())
    #new_file = open('/opt/djangostack-1.6/apache2/reports/%s_httpCase_%s_NewCaseFile.txt' % (report_name,runTimeString), 'w')
    new_file = open('./data201412/%s_httpCase_%s_NewCaseFile.txt' % (report_name,runTimeString), 'w')


    totalCase = 0
    for line in lines:
        line = str(line).strip()
        if line.startswith('http'):
            #print line
            totalCase = totalCase + 1
            caseurl = line.replace('zeus-m.lightinthebox.com',Zeus_LITB_IP+':'+Zeus_PORT)

            #调用“更新url中的参数和值”的方法，对sid进行更新
            changeParamUrl=Updata_url_paramvalue(caseurl,regularkey,regularvalue)
            print changeParamUrl

            # if api is new zeus api:
            if changeParamUrl.find("/v1/")>0:
                new_sign_value=ZeusApi_v1_to_sign(changeParamUrl)
            else:
            #不存在/v1/，就是旧接口，用老的加密方式获得sign
                new_sign_value=ZeusApi_copy_vela(changeParamUrl)

            #加密接口返回的结果，调用“更新url中的参数和值”的方法，对sign进行更新
            regularsign="sign"
            regularsignvalue=new_sign_value
            newsign_url=Updata_url_paramvalue(changeParamUrl,regularsign,regularsignvalue)

            print newsign_url
            new_file.writelines( '%s\n' % str(newsign_url))




    new_file.close()

if __name__ == '__main__':
    #config_dict = settings.config_dict_template
    #config_dict['handlers']['default']['filename'] = os.path.join(project_path, 'logs', 'error.log')
    #logging.config.dictConfig(config_dict)

    Change_params_in_case('vela.categories.get_test.txt', 'vela.categories.get_test',regularkey,regularvalue)



