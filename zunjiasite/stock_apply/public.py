#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#
#
#
#@author liwq(vince_lee@bizconf.cn)

import os
import sys
import time
import datetime
import math
import shutil
import logging
import re

def isStr(var):
    """是否为字符串"""
    return isinstance(var, basestring)

def getSysTime(frmt="%Y-%m-%d %H:%M:%S"):
    return time.strftime(frmt, time.localtime())

def getSysDate(frmt="%Y-%m-%d"):
    return datetime.date.today().strftime(frmt)

def rplcTime(strTime):
    if strTime is None or len(strTime.strip()) == 0:
        return ""
    return strTime.replace('-', '').replace(':', '').replace(' ', '').strip()

def formatTime(strTime, frmt="%H:%M:%S"):
    """格式化字符串时间为%H:%M:%S"""
    t = time.strptime(strTime, frmt)
    return time.strftime(frmt, t)

def timeTtimeStr(strTime):
    if len(strTime) != 6:
        raise TimeconvertException("paras len not equals 6:", strTime)
    return ':'.join(re.compile(r'.{2}').findall(strTime))

def getTimeStamp(strT, frmt="%Y%m%d%H%M%S"):
    """接收一个制定格式的字符串时间，返回对应时间戳"""
    return int(time.mktime(time.strptime(strT,frmt)))

def timeDiff(strT1, strT2, fmt="%H:%M:%S"):
    """时间差值,返回为向上进位的分钟"""
    t1 = time.mktime(time.strptime(strT1, fmt))
    t2 = time.mktime(time.strptime(strT2, fmt))
    df = int(math.ceil((t1-t2)/60))
    return df

def minDiff(strT1, strT2):
    """时间差值,返回为向下进位的分钟"""
    t1 = time.mktime(time.strptime(strT1,"%H:%M:%S"))
    t2 = time.mktime(time.strptime(strT2,"%H:%M:%S"))
    df = int((t1-t2)/60)
    return df

def secDiff(strT1, strT2, fmt = "%H:%M:%S"):
    """时间差值,返回为T1-T2的秒数"""
    t1 = time.mktime(time.strptime(strT1, fmt))
    t2 = time.mktime(time.strptime(strT2, fmt))
    df = int(t1-t2)
    return df

def dtDiff(strD1, strT1, strD2, strT2, timeFmt="%H%M%S"): 
    sDt1 = strD1+formatTime(strT1, timeFmt)
    sDt2 = strD2+formatTime(strT2, timeFmt)
    return secDiff(rplcTime(sDt1), rplcTime(sDt2), fmt="%Y%m%d%H%M%S")

def secToMin(strSec):
    return int(math.ceil(float(strSec)/60))


def addSec(sec, strTime, frmt="%H:%M:%S"):
    tmptime = ""
    try:
        dt = datetime.datetime.strptime(strTime, frmt) + datetime.timedelta(seconds = int(sec))
        tmptime = dt.strftime(frmt)
    except Exception, e:
        raise TimeconvertException(e, "paras:", sec, strTime)
    return tmptime

def getLastMonth(currenMonth):
    '''前一个月，输出“YYYYMM”
    '''
    currenMonth = rplcTime(currenMonth)
    curren = currenMonth[0:6] + "01000000"
    last = addSec(-1, curren, "%Y%m%d%H%M%S")
    return last[0:6]

import MySQLdb
class MySQL:
    def __init__(self,host,user,password,port=3306,charset="utf8",autoComm = False):
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.charset=charset
        self.autoComm = autoComm
        self._connect()

    def _connect(self):
        try:
            self.conn=MySQLdb.connect(host=self.host,port=self.port,user=self.user,passwd=self.password)
            self.conn.autocommit(self.autoComm)
            self.conn.set_character_set(self.charset)
            self.cur=self.conn.cursor()
        except MySQLdb.Error as e:
            raise BillSqlException, "Mysql Error %d: %s" % (e.args[0], e.args[1])
            return 0

    def __del__(self):
        self.close()

    def ping(self):
        try:
            self.conn.ping()
            return 1
        except:
            try:
                self._connect()
                return 1
            except:
                return 0


    def selectDb(self,db):
        try:
            self.conn.select_db(db)
        except MySQLdb.Error as e:
            raise BillSqlException, "Mysql Error %d: %s" % (e.args[0], e.args[1])


    def execute(self, sql, parameters=None):
        try:
            n=self.cur.execute(sql, parameters)
            return n
        except MySQLdb.Error as e:
            raise BillSqlException, "Mysql Error:%s\nSQL:%s" %(e,sql)


    def fetchRow(self):
        result = self.cur.fetchone()
        return result


    def fetchAll(self):
        result=self.cur.fetchall()
        desc =self.cur.description
        d = []
        for inv in result:
            _d = {}
            for i in range(0,len(inv)):
                _d[desc[i][0]] = str(inv[i])
            d.append(_d)
        return d


    def rowcount(self):
        return self.cur.rowcount


    def commit(self):
        self.conn.commit()


    def rollback(self):
        self.conn.rollback()


    def close(self):
        self.cur.close()
        self.conn.close()

class Log(object):
    """日志类
    使用：
    lg = Log(logFile='', fmt='', level='')
    loger = lg.getLogger()
    loger.info('')
    """
    def __init__(self, logFile, fmt, level=logging.INFO):
        self.logFile = logFile
        self.fmt = fmt
        self.level = level
        self.logger = None
        self.hdlr = None

    def __del__(self):
        if self.logger is not None and self.hdlr is not None:
            self.logger.removeHandler(self.hdlr)
            self.hdlr.close()


    def getLogger(self):
        if self.logger:
            return self.logger
        self.logger = logging.getLogger()
        self.hdlr = logging.FileHandler(self.logFile)
        formatter = logging.Formatter(self.fmt)
        self.hdlr.setFormatter(formatter)
        self.logger.addHandler(self.hdlr)
        self.logger.setLevel(self.level)
        return self.logger

