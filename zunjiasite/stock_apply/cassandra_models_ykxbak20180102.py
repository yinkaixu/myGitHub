from cassandra.cluster import Cluster, BatchStatement
from cassandra import ConsistencyLevel

cassandra_tables = ['hk_shareipo','hk_shareipo_enddate','hk_shareipo_enddate_code','hk_shareipo_enddate_id']
cassandra_hosts = ['192.168.2.238']
cluster = Cluster(cassandra_hosts)
session = cluster.connect()
session.default_consistency_level = ConsistencyLevel.ALL




def delete_from_cassantra(dic_para):
    code=dic_para.get('code','')
    exchange=dic_para.get('exchange','')
    id=dic_para.get('id','')
    issueenddate=dic_para.get('issueenddate','')
    print ("code=%s,exchange=%s,id=%s,issueenddate=%s"%(code,exchange,id,issueenddate) )
    if code=='' or exchange=='' or id=='' or issueenddate=='':
        return False;
    try:
        tablename = 'hk_shareipo'
        cql = session.prepare("delete from market.{} where id=:id;".format(tablename))
        session.execute(cql.bind({"id":float(id)}))
            
        tablename = 'hk_shareipo_enddate'
        cql = session.prepare("delete from market.{} where exchange=:exchange and code=:code;".format(tablename))
        session.execute(cql.bind({"exchange":exchange,"code":code}))
            
        tablename = 'hk_shareipo_enddate_code'
        cql = session.prepare("delete from market.{} where exchange=:exchange and issueenddate=:issueenddate and code=:code;".format(tablename))
        session.execute(cql.bind({"exchange":exchange,"issueenddate":issueenddate,"code":code}))
            
        tablename = 'hk_shareipo_enddate_id'
        cql = session.prepare("delete from market.{} where exchange=:exchange and issueenddate=:issueenddate and id=:id;".format(tablename))
        session.execute(cql.bind({"exchange":exchange,"issueenddate":issueenddate,"id":float(id)}))
    except:
        raise
    return True
    
def insert_stock_to_cassandra(dic_para):
    
    id=dic_para.get('id','')
    code=dic_para.get('code','')
    stockname=dic_para.get('stockname','')
    updatetime=dic_para.get('updatetime','')
    issuevolplanned = dic_para.get('issuevolplanned','')
    publicnewshareplanned=dic_para.get('publicnewshareplanned','')
    issuepriceceiling=dic_para.get('issuepriceceiling','')
    issuepricefloor=dic_para.get('issuepricefloor','')
    tradeunitpriceatceiling=dic_para.get('tradeunitpriceatceiling','')
    exchange=dic_para.get('exchange','')
    issuetype=dic_para.get('issuetype','')
    applystartdate=dic_para.get('applystartdate','')
    issueenddate=dic_para.get('issueenddate','')
    proposedlistdate=dic_para.get('proposedlistdate','')
    datetoaccount=dic_para.get('datetoaccount','')
    tradeunit=dic_para.get('tradeunit','')
    
    try:
        for tablename in cassandra_tables:
            cql = session.prepare("insert into market.{} (id,initialinfopubldate,code,name,issuevolplanned,publicnewshareplanned,issuepriceceiling,issuepricefloor,tradeunitpriceatceiling,exchange,issuetype,applystartdate,issueenddate,proposedlistdate,datetoaccount,tradeunit)\
                values(:id,:initialinfopubldate,:code,:name,:issuevolplanned,:publicnewshareplanned,:issuepriceceiling,:issuepricefloor,:tradeunitpriceatceiling,:exchange,:issuetype,:applystartdate,:issueenddate,:proposedlistdate,:datetoaccount,:tradeunit);".format(tablename))
            session.execute(cql.bind({"id":id,"initialinfopubldate":updatetime,"code":code,"name":stockname,"issuevolplanned":float(issuevolplanned),"publicnewshareplanned":float(publicnewshareplanned),"issuepriceceiling":float(issuepriceceiling),
                    "issuepricefloor":float(issuepricefloor),"tradeunitpriceatceiling":float(tradeunitpriceatceiling),"exchange":exchange,"issuetype":float(issuetype),"applystartdate":applystartdate,"issueenddate":issueenddate,"proposedlistdate":proposedlistdate,
                     "datetoaccount":datetoaccount,"tradeunit":float(tradeunit)}))
    except:
        raise 
        
    return 1 
