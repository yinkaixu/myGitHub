from datetime import datetime
from datetime import timedelta
from oracle_models import *
from mysql_models import *
from sqlalchemy.sql import select, distinct,delete,insert,update
from sqlalchemy import (MetaData, Table, Column, Integer, Numeric, String,text,func,desc )
from public import *
import optparse

Usage = "associate_jy_id.py -t force|limit"
Parser = optparse.OptionParser( usage=Usage )

def usage():
    Parser.add_option("-t", dest="runtype", help=r'[force|limit]')
    
def associate_jy_id():
    logDir = './log/'
    logFileName = 'associate_%s.log'
    logFrmt = r"%(asctime)s (%(filename)s.%(lineno)d) %(message)s"
    logger = None
    #处理日志级别
    logLevel = logging.INFO
    logFile = os.path.join(logDir, logFileName%(getSysDate("%Y%m")))  
    log = Log(logFile, logFrmt, level=logLevel)
    logger = log.getLogger()
    logger.info("begin associate ..... ")
    try:
        sl = select([stock_oracle]).select_from(stock_oracle).where(stock_oracle.c.jy_id==0)
        result = oracle_connect.execute(sl)
        zj_stocks = result.fetchall()
        logger.info("need associate count="+str(len(zj_stocks)))
        for zj_stock in zj_stocks:
            code = zj_stock.code
            logger.info("zj_stock.code="+code)
            updatetime = zj_stock.updatetime
            start = updatetime-timedelta(days=4)
            end = updatetime+timedelta(days=10)
            #print start
            #print end
            #print start.strftime('%Y-%m-%d')
            s2 = select([jy_hk_ipo]).select_from(jy_hk_ipo).where(jy_hk_ipo.c.code==code).where(jy_hk_ipo.c.xgrq>start).where(jy_hk_ipo.c.xgrq<end)
            #print str(s2)
            jy_ipos = oracle_connect.execute(s2).fetchall()
            print 'len(jy_ipos)=%s'%len(jy_ipos)
            logger.info("len(jy_ipos)="+str(len(jy_ipos)))
            if len(jy_ipos)>0 :
                for jy_ipo in jy_ipos:
                    print jy_ipo.id
                    #print jy_ipo.code
                    #print jy_ipo.xgrq
                    logger.info("jy_ipo.id="+str(jy_ipo.id))
                    upt = update(stock_oracle).where(stock_oracle.c.id == zj_stock.id).values(jy_id=jy_ipo.id)
                    result3 = oracle_connect.execute(upt)
                    print("update_count => %s" %result3.rowcount)
                    logger.info("update ok")
                    break;
    except Exception as e:
        logger.info(str(e))
    logger.info("end associate ..... ")
    return 1
        
def main():
    associate_jy_id()
if __name__ == '__main__':
    main()
       
    
