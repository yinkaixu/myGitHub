from sqlalchemy import (MetaData, Table, Column, Integer, Numeric, String, Boolean, 
                        DateTime, ForeignKey, Date, create_engine,func,select,and_)
from datetime import datetime
import ConfigParser
#SQLALCHEMY_ECHO=True
ConfFile = "./stock_apply/cfg/DB.cfg"
DBCnf = ConfigParser.ConfigParser()
#Read configure
DBCnf.read( ConfFile )
host = DBCnf.get("DB", "host")
username = DBCnf.get("DB", "user")
passwd = DBCnf.get("DB", "passwd")
database = DBCnf.get("DB", "database")
connect_str = 'mysql://'+username+':'+passwd+'@'+host+':3306/'+database+'?charset=utf8'
print connect_str
engine2 = create_engine(connect_str,echo=False)
metadata2 = MetaData(engine2)
hk_shareipo = Table('hk_shareipo', metadata2,
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
        Column('createtime', DateTime,default=datetime.now ) ,
        Column('jy_id', Integer)
        )  
mysql_connect = engine2.connect()

