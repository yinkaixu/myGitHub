from sqlalchemy import (MetaData, Table, Column, Integer, Numeric, String, Boolean, 
                        DateTime, ForeignKey, Date, create_engine,func,select,and_)
from datetime import datetime
#SQLALCHEMY_ECHO=True
engine = create_engine('oracle://hkpre:hkpre@192.168.2.248:1521/zunjia',echo=False)
metadata = MetaData(engine)
stock_oracle = Table('ZJ_HK_IPO', metadata,
        Column('id', Integer),
        Column('code', String(20)),
        Column('name', String(50)),
        Column('issuevolplanned', Numeric(18,2)),
        Column('publicnewshareplanned', Numeric(18,2)),
        Column('issuepriceceiling', Numeric(18,8)),
        Column('issuepricefloor', Numeric(18,8)),
        Column('tradeunitpriceatceiling', Numeric(19,4)),
        Column('exchange', String(10)),
        Column('issuetype', Integer),
        Column('applystartdate',Date),
        Column('issueenddate',Date),
        Column('proposedlistdate', Date),
        Column('datetoaccount',Date),
        Column('tradeunit', Integer),
        Column('updatetime', DateTime,default=datetime.now),
        Column('marketcode', String(10)),
        Column('issueprice', Numeric(18,8)),
        Column('pin_yin', String(20)),
        Column('jy_id', Integer) 
        )

zjjy_hk_ipo = Table('ZJJY_HK_IPO', metadata,
        Column('code', String(20)),
        Column('name', String(50)),
        Column('source', String(2)),
        Column('issuevolplanned', Numeric(18,2)),
        Column('publicnewshareplanned', Numeric(18,2)),
        Column('issuepriceceiling', Numeric(18,8)),
        Column('issuepricefloor', Numeric(18,8)),
        Column('tradeunitpriceatceiling', Numeric(19,4)),
        Column('exchange', String(10)),
        Column('issuetype', Integer),
        Column('applystartdate',Date),
        Column('issueenddate',Date),
        Column('proposedlistdate', Date),
        Column('datetoaccount',Date),
        Column('tradeunit', Integer),
        Column('updatetime', DateTime),
        Column('marketcode', String(10)),
        Column('issueprice', Numeric(18,8)),
        Column('pin_yin', String(20)),
        Column('jy_id', Integer)
        ) 
jy_hk_ipo = Table('V_HK_SHAREIPO', MetaData(engine,schema='JYDB'),
        Column('code', String(20)),
        Column('xgrq', DateTime),
        Column('id', Integer)
        )      
oracle_connect = engine.connect()
sql="alter session set nls_date_format='YYYY-MM-DD'"
oracle_connect.execute(sql)

def is_jy_new_code(code):
    try:
        result1 = oracle_connect.execute("select COUNT(*) from SECDEF_HKEX where code='"+code+"'").first()
        if( int(result1[0])>0):
            return False
    except Exception as e:
        print e
        return False
    return True
    
def is_zj_new_code(code):
    try:
        result2 = oracle_connect.execute(select([func.count(stock_oracle.c.code)]).where(stock_oracle.c.code==code)).first()
        if( int(result2[0])>0):
            return False
    except Exception as e:
        print e
        return False
    return True   
