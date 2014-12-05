#!/usr/bin/python
# -*- encoding: utf-8 -*-
#
__author__ = 'liwei'
__date__ = '2014-08-21'

import json
import subprocess
import shlex

import os
import sys
import time
import hashlib
import logging
import requests
import traceback
import collections
import logging.config


from jsonschema import Draft3Validator
import simplejson
project_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, project_path)
reload(sys)
sys.setdefaultencoding('utf8')




#51 test environment----------------------
Zeus_LITB_IP='192.168.66.51'#'23.253.5.32'#'166.78.222.125'
Zeus_MINI_IP='192.168.66.51'#'166.78.222.126'
Zeus_PORT='8081'
#
Vela_LITB_IP='192.168.66.51'#'166.78.222.125'
Vela_MINI_IP='192.168.66.51'
Vela_PORT='80'
#------------------------------------------

#staging testing-------------------------
#Zeus_LITB_IP='166.78.222.125'
#Zeus_MINI_IP='166.78.222.126'
#Zeus_PORT='8081'#'80'
#
#Vela_LITB_IP='166.78.222.125'
#Vela_MINI_IP='166.78.222.126'
#Vela_PORT='81'
#----------------------------------------

def dump(obj, fname):
    fp = open(fname, 'w')
    json.dump(obj, fp, indent=True, sort_keys=True)
    fp.close()

def exec_cmd(cmd):
    cmds = shlex.split(cmd)
    p = subprocess.Popen(cmds, stdout=subprocess.PIPE)
    out, err = p.communicate()
    return out, err

def diff(schema_DS, req_json):
    print "===============Draft3Validator=============="
    validator = Draft3Validator(schema_DS)

    errors=validator.iter_errors( req_json )
    error_msg=[]
    for error in errors:
        print "error.relative_schema_path-->"
        print error.relative_schema_path
        print "error.message-->"
        print error.message
        error_msg.append(error.relative_schema_path)
        error_msg.append(error.message)

    return error_msg

def has_diff(result):
#return result.find('---') > 0
    return  len(str(result)) > 0



def runHttpCase_LITB(data_file,ds_file, report_name):
    lines = open(os.path.join(project_path, 'data', data_file)).readlines()
    #lines=open('./data/%s'%(data_file)).readlines()
    runTimeString= time.strftime('%Y%m%d_%H%M', time.localtime())

    report_file = open('./reports/%s_httpCase_%s_ok.txt' % (report_name,runTimeString), 'w')
    report_error = open('./reports/%s_httpCase_%s_error.txt' % (report_name,runTimeString), 'w')




    report_file.writelines('<html>\n<pre>\n ')
    report_error.writelines('<html>\n<pre>\n ')

    totalCase = 0
    rightCase = 0
    wrongCase = 0

    lines_ds = open(os.path.join(project_path, 'ds_json', ds_file)).readlines()
    str_lines=''.join(lines_ds)
    schema_DS_new=str_lines.replace(' ','').replace('\n','')
    ret_dict = simplejson.loads(schema_DS_new)
    print "json_dict:"
    print ret_dict
    schema_ApiDS=dict(ret_dict)

    for line in lines:
        line = str(line).strip()
        if line.startswith('http'):
            totalCase = totalCase + 1
            try:
                zeusURL = line.replace('zeus-m.lightinthebox.com',Zeus_LITB_IP+':'+Zeus_PORT)
                print zeusURL
                zeus_req = requests.get(zeusURL, headers={'host': 'zeus-m.lightinthebox.com'})#'zeus-m.lightinthebox.com'})
                zeus_json = zeus_req.json()
                print "---litb_zeus_json---:"
                print zeus_json


                result= diff(schema_ApiDS,zeus_json)
                print result
                code = '_False' if has_diff(result) else '_True'
                if code == '_True':
                    rightCase = rightCase +1
                    print "TRUE"
                    report_file.writelines('\n====================================================================\n ')
                    report_file.writelines('\nright case number: %s\n ' % str(rightCase))
                    report_file.writelines('\n---------------------------one Success start------------------------\n ')
                    report_file.writelines( '\n'+'%s\n' % code.__str__())
                    report_file.writelines( '\n'+'success number: %s\n' % str(rightCase))
                    report_file.writelines( '\n'+'zeusURL  %s\n' % str(zeusURL))
                    #report_file.writelines( '\n'+'velaURL  %s\n' % str(velaURL))
                    report_file.writelines('\n====================================================================\n ')

                    report_file.writelines('Zeus: %s\n' % zeus_json)
                    report_file.writelines('Data Struction: %s\n' % schema_ApiDS)

                else:
                    wrongCase = wrongCase +1
                    print "False"
                    report_error.writelines('\n====================================================================\n ')
                    report_error.writelines('\nwrong case number: %s\n ' % str(wrongCase))
                    report_error.writelines('\n---------------------------one Failed start-------------------------\n ')
                    report_error.writelines( '\n'+'%s\n' % code.__str__())
                    report_error.writelines( '\n'+'failed number: %s\n' % str(wrongCase))
                    report_error.writelines( '\n'+'zeusURL  %s\n' % str(zeusURL))
                    #report_error.writelines( '\n'+'velaURL  %s\n' % str(velaURL))
                    report_error.writelines('\n====================================================================\n ')

                    report_error.writelines('Zeus: %s\n' % zeus_json)
                    report_error.writelines('\n--------------------------------------------------------------------\n ')
                    report_error.writelines('Data Struction: %s\n' % schema_ApiDS)

                    report_error.writelines('\n--------------------------------------------------------------------\n ')
                    report_error.writelines('zeus output VS DS ')
                    report_error.writelines('\n--------------------------------------------------------------------\n ')
                    report_error.writelines('%s\n' % result)
                    report_error.writelines('\n---------------------------one Failed over--------------------------\n ')

            except Exception, e:
                print e
                #logging.error(e)
                #logging.error(traceback.format_exc())


    report_file.writelines('\n\n Total case: %s  \n Succeful case: %s \n Failed case: %s \n' % (str(totalCase),str(rightCase),str(wrongCase)))
    report_error.writelines('\n\n Total case: %s  \n Succeful case: %s \n Failed case: %s \n' % (str(totalCase),str(rightCase),str(wrongCase)))

    report_file.writelines('\n<\pre>\n<\html>')
    report_error.writelines('\n<\pre>\n<\html>')
    report_file.close()
    report_error.close()





if __name__ == '__main__':
#config_dict = settings.config_dict_template
#config_dict['handlers']['default']['filename'] = os.path.join(project_path, 'logs', 'error.log')
#logging.config.dictConfig(config_dict)


 runHttpCase_LITB('vela.items.get.txt','vela_item_get_ds.json','vela.items.get_LITB_ds')


