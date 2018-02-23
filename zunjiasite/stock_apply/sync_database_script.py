from datetime import datetime
from datetime import timedelta
from oracle_models import *
from mysql_models import *
from sqlalchemy.sql import select, distinct,delete,insert
from sqlalchemy import (MetaData, Table, Column, Integer, Numeric, String,text,func,desc )
from public import *
import optparse

Usage = "sync_database_script.py -t force|limit"
Parser = optparse.OptionParser( usage=Usage )

def usage():
    Parser.add_option("-t", dest="runtype", help=r'[force|limit]')

def sync_mysql_by_code(code = '',old_code='',jy_id=0):
    print __file__
    sl = select([zjjy_hk_ipo]).select_from(zjjy_hk_ipo).where(zjjy_hk_ipo.c.code==code).where(zjjy_hk_ipo.c.jy_id==jy_id)
    result = oracle_connect.execute(sl)
    oracle_hk_ipo = result.fetchall()
    print 'len(oracle_hk_ipo)=%s'%len(oracle_hk_ipo)
    if len(oracle_hk_ipo)>1:#应该最多只有一条
        return -1
    if old_code=='':
    	old_code=code
    calltype='django'
    print 'code:%s|old_code:%s|jy_id:%s'%(code,old_code,jy_id)
    trans = mysql_connect.begin();
    try:
        # mysql表删除old_code
        dl1= delete(hk_shareipo).where(hk_shareipo.c.code==old_code).where(hk_shareipo.c.jy_id==jy_id)
        #print str(dl1)
        result1 = mysql_connect.execute(dl1)
        #print  'result1.rowcount%s'%result1.rowcount
        print len(oracle_hk_ipo)
        if(len(oracle_hk_ipo)>0):#zjjy_hk_ipo表中有，到mysql表加上此code
            for row in oracle_hk_ipo:
                if(calltype=='script'):
                    rname = row.name.decode('GBK').encode('utf-8')
                    rpin_yin = row.pin_yin.decode('GBK').encode('utf-8')
                else:
                    rname = row.name
                    rpin_yin = row.pin_yin
                ins = insert(hk_shareipo).values(
                      code = row.code,
                      name = rname,
                      source = row.source,
                      issuevolplanned = row.issuevolplanned,
                      publicnewshareplanned = row.publicnewshareplanned,
                      issuepriceceiling = row.issuepriceceiling,
                      issuepricefloor = row.issuepricefloor,
                      tradeunitpriceatceiling = row.tradeunitpriceatceiling,
                      exchange = row.exchange,
                      issuetype = row.issuetype,
                      applystartdate = row.applystartdate,
                      issueenddate = row.issueenddate,
                      proposedlistdate = row.proposedlistdate,
                      datetoaccount = row.datetoaccount,
                      tradeunit = row.tradeunit,
                      updatetime = row.updatetime,
                      marketcode = row.marketcode,
                      issueprice = row.issueprice,
                      pin_yin = rpin_yin,
                      jy_id = row.jy_id
                      )
                rt = mysql_connect.execute(ins)
        trans.commit()
    except Exception as e:
        trans.rollback()
        print str(e)
        raise
    return 1;

def sync_database(calltype='script'):
    '''
    usage()
    args = []
    (option, args) = Parser.parse_args()
    runtype = option.runtype
    if(runtype==None):
        runtype ='force'
    '''
    runtype ='force'
    print 'runtype=%s'%runtype
    if(calltype=='script'):
        logDir = './log/'
    else:
        logDir = './stock_apply/log/'
    logFileName = 'sync_%s.log'
    logLevel = 'INFO'
    logFrmt = r"%(asctime)s (%(filename)s.%(lineno)d) %(levelname)s %(message)s"
    logger = None
    #处理日志级别
    logLevel = logLevel.upper()
    if "INFO" == logLevel:
        logLevel = logging.INFO
    elif "ERROR" == logLevel:
        logLevel = logging.ERROR
    elif "WARING" == logLevel:
        logLevel = logging.WARN
    else:
        logLevel = logging.DEBUG
    logFile = os.path.join(logDir, logFileName %(getSysDate("%Y%m")))  
    log = Log(logFile, logFrmt, level=logLevel)
    logger = log.getLogger()
    logger.info("begin sync ..... ")
    #sl = select([zjjy_hk_ipo]).order_by(desc(zjjy_hk_ipo.c.updatetime))
    #compiled = sl.compile(engine2, compile_kwargs={"literal_binds": True})
    #print compiled
    
    if(runtype !='force'):
        sl = select([func.count('*')]).select_from(zjjy_hk_ipo).where(text('UPDATETIME>sysdate -1/24'))
        #compiled = sl.compile(engine2, compile_kwargs={"literal_binds": True})
        result = oracle_connect.execute(sl).scalar()
        logger.info("data number that need sync is:"+str(result))
        print result
        if(result<=0):
            print "needn not sync data,count=%s"%result
            logger.info("need not sync data")
            return 0
    

    oracle_hk_ipo = oracle_connect.execute(select([zjjy_hk_ipo]).select_from(zjjy_hk_ipo).order_by(desc(zjjy_hk_ipo.c.updatetime))).fetchall()
    logger.info("selected count="+str(len(oracle_hk_ipo)))
    logger.info("mysql_connect_str="+connect_str)
    
    trans = mysql_connect.begin();
    try:
        del1 = delete(hk_shareipo)
        result1 = mysql_connect.execute(del1)
        
        for row in oracle_hk_ipo:
            #print row.name.decode('GBK').encode('utf-8')
            #print row.code
            if(calltype=='script'):
                rname = row.name.decode('GBK').encode('utf-8')
                rpin_yin = row.pin_yin.decode('GBK').encode('utf-8')
            else:
                rname = row.name
                rpin_yin = row.pin_yin
            ins = insert(hk_shareipo).values(
                  code = row.code,
                  name = rname,
                  source = row.source,
                  issuevolplanned = row.issuevolplanned,
                  publicnewshareplanned = row.publicnewshareplanned,
                  issuepriceceiling = row.issuepriceceiling,
                  issuepricefloor = row.issuepricefloor,
                  tradeunitpriceatceiling = row.tradeunitpriceatceiling,
                  exchange = row.exchange,
                  issuetype = row.issuetype,
                  applystartdate = row.applystartdate,
                  issueenddate = row.issueenddate,
                  proposedlistdate = row.proposedlistdate,
                  datetoaccount = row.datetoaccount,
                  tradeunit = row.tradeunit,
                  updatetime = row.updatetime,
                  marketcode = row.marketcode,
                  issueprice = row.issueprice,
                  #pin_yin = row.pin_yin.decode('GBK').encode('utf-8'),
                  pin_yin = rpin_yin,
                  jy_id = row.jy_id
                  )
            rt = mysql_connect.execute(ins)
        trans.commit()
        
        logger.info("sync [ok]")
    except Exception as e:
        trans.rollback()
        print str(e)
        logger.info("sync [error]")
        logger.info(str(e))
        raise
    return 1
    
def main():
    sync_database()
    #sync_mysql_by_code(code = '08509')
    #sync_mysql_by_code(code = '44444')
if __name__ == '__main__':
    main()
       
    
