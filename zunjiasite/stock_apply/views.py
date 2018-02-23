from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from models import Stock
from datetime import timedelta
from .oracle_models import *
from .mysql_models import *
from .sync_database_script import *
from sqlalchemy.sql import select, distinct,delete
from sqlalchemy import (MetaData, Table, Column, Integer, Numeric, String,text,func,desc,or_)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
import json
import urllib2
from public import *
import ConfigParser
import sys
reload(sys) 
sys.setdefaultencoding('utf8')


# Create your views here.
def stock_input(request):
    #form = AddForm()
    act = request.GET.get('act')
    if(act is None ):
        act='add'
    print('act=%s'%act)
    if(act=='update'):
        code=request.GET.get('code')
        source = request.GET.get('source')
        if(code==''):
            return HttpResponse("code is NULL")
        if(source==''):
            return HttpResponse("source is NULL")
            
        dic_record={}
        try:
            if(source=='ZJ'):
                stock = Stock.objects.get(code=code)
                dic_record['stockname']=stock.name
                dic_record['code']=stock.code
                if(stock.issuevolplanned!=None):
                    dic_record['issuevolplanned']=stock.issuevolplanned
                if(stock.publicnewshareplanned):
                    dic_record['publicnewshareplanned']=stock.publicnewshareplanned
                if(stock.issuepriceceiling):
                    dic_record['issuepriceceiling']=str(float(stock.issuepriceceiling))
                if(stock.issuepricefloor):
                    dic_record['issuepricefloor']=str(float(stock.issuepricefloor))
                if(stock.tradeunitpriceatceiling):
                    dic_record['tradeunitpriceatceiling']=str(float(stock.tradeunitpriceatceiling))
                dic_record['exchange']=stock.exchange
                dic_record['issuetype']=stock.issuetype
                dic_record['applystartdate']=stock.applystartdate.strftime('%Y-%m-%d')
                dic_record['issueenddate']=stock.issueenddate.strftime('%Y-%m-%d')
                if(stock.proposedlistdate):
                    dic_record['proposedlistdate']=stock.proposedlistdate.strftime('%Y-%m-%d')
                if(stock.datetoaccount):
                    dic_record['datetoaccount']=stock.datetoaccount.strftime('%Y-%m-%d')
                if(stock.tradeunit):
                    dic_record['tradeunit']=stock.tradeunit
                dic_record['id']=stock.id
                if(stock.issueprice!=None):
                    dic_record['issueprice']=stock.issueprice
                dic_record['marketcode']=stock.marketcode
                if(stock.pin_yin):
                    dic_record['pin_yin']=stock.pin_yin
                dic_record['jy_id']=stock.jy_id
                return render(request, 'input.html',{'render_dic':dic_record,'act':act})

            elif(source=='JY'):
                ipo = oracle_connect.execute(zjjy_hk_ipo.select().where(zjjy_hk_ipo.c.code==code)).first()
                dic_record['stockname']=ipo.name
                dic_record['code']=ipo.code
                if(ipo.issuevolplanned!=None):
                    dic_record['issuevolplanned']=ipo.issuevolplanned
                if(ipo.publicnewshareplanned):
                    dic_record['publicnewshareplanned']=ipo.publicnewshareplanned
                if(ipo.issuepriceceiling):
                    dic_record['issuepriceceiling']=ipo.issuepriceceiling
                if(ipo.issuepricefloor):
                    dic_record['issuepricefloor']=str(float(ipo.issuepricefloor))
                if(ipo.tradeunitpriceatceiling):
                    dic_record['tradeunitpriceatceiling']=str(float(ipo.tradeunitpriceatceiling))
                dic_record['exchange']=ipo.exchange
                dic_record['issuetype']=ipo.issuetype
                dic_record['applystartdate']=ipo.applystartdate.strftime('%Y-%m-%d')
                dic_record['issueenddate']=ipo.issueenddate.strftime('%Y-%m-%d')
                if(ipo.proposedlistdate):
                    dic_record['proposedlistdate']=ipo.proposedlistdate.strftime('%Y-%m-%d')
                if(ipo.datetoaccount):
                    dic_record['datetoaccount']=ipo.datetoaccount.strftime('%Y-%m-%d')
                if(ipo.tradeunit):
                    dic_record['tradeunit']=ipo.tradeunit
                if(ipo.issueprice!=None):
                    dic_record['issueprice']=ipo.issueprice
                dic_record['marketcode']=ipo.marketcode
                if(ipo.pin_yin):
                    dic_record['pin_yin']=ipo.pin_yin
                dic_record['jy_id']=ipo.jy_id
                print dic_record
                return render(request, 'input.html',{'render_dic':dic_record,'act':'add'})#如source是聚源，update操作是ZJ_HK_IPO表的insert
            else:
                pass                  
        except Exception as e:
            return HttpResponse(str(e))
    elif act=='add':
        dic_record={}
        dic_record['exchange']='HKEX'
        dic_record['jy_id']='0'
        return render(request, 'input.html',{'render_dic':dic_record,'act':act})
    return render(request, 'input.html')
    
    
def showlist(request):
    number_per_page = 20 #每页显示条数
    render_list=[]
    now = datetime.datetime.now()
    #前60天
    start = now-timedelta(days=60) 
    orderby = request.GET.get('orderby','issueenddate')
    q = request.GET.get('q','')
    if(q=='股票代码或名称'):
        q=''      
    if(q!=''):
        zjjy_ipos = oracle_connect.execute(select([zjjy_hk_ipo]).where(zjjy_hk_ipo.c.issueenddate > start).where(or_(zjjy_hk_ipo.c.name.ilike('%'+q+'%'),(zjjy_hk_ipo.c.code.ilike('%'+q+'%')))).order_by(text(orderby+" DESC"))).fetchall()
    else:
        zjjy_ipos = oracle_connect.execute(select([zjjy_hk_ipo]).where(zjjy_hk_ipo.c.issueenddate > start).order_by(text(orderby+" DESC"))).fetchall()
    
    linenum=0
    for ipo in zjjy_ipos:
        #print ipo.source
        linenum += 1
        dic_record={}
        dic_record['source']=ipo.source
        dic_record['jy_id']=ipo.jy_id
        if(ipo.issueprice):
            dic_record['issueprice']=str(float(ipo.issueprice))
        dic_record['stockname']=ipo.name
        #print ipo.name
        dic_record['code']=ipo.code
        dic_record['exchange']=ipo.exchange
        dic_record['applystartdate']=ipo.applystartdate.strftime('%Y-%m-%d')
        dic_record['issueenddate']=ipo.issueenddate.strftime('%Y-%m-%d')
        if(ipo.datetoaccount is not None):
        	dic_record['datetoaccount']=ipo.datetoaccount.strftime('%Y-%m-%d')
        updatetime =ipo.updatetime
        dic_record['updatetime']=updatetime.strftime('%Y-%m-%d %H:%M:%S')
        dic_record['linenum'] = linenum%2+1
        render_list.append(dic_record)
    page = request.GET.get('page')
    print 'page=%s'%page
    paginator = Paginator(render_list, number_per_page)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'list.html',{'render_list':contacts,'q':q,'orderby':orderby})
    #return render(request, 'list.html',{'render_list':render_list})
    #return render(request, 'list.html',{'render_list':mystocks})
def contact(request):
    """Renders the contact page."""
    return render(request,'contact.html',{'title':'Contact','year':datetime.now().year,'message':'Your contact page.'})
        
def info_submit(request):
    rt='1'
    act = request.POST.get('act')
    if(act=='del'):
        code=request.POST.get('code').strip()
        jy_id=request.POST.get('jy_id')
        try:
            print 'code=%s'%code
            del_stock = Stock.objects.filter(code=code).filter(jy_id=jy_id)
            for dstock in del_stock:
            	del_issueprice=dstock.issueprice
            	break;
            #print 'del_issueprice=%s'%del_issueprice
            del_stock.delete()  
            #同步到mysql  
            sync_mysql_by_code(code=code,old_code=code,jy_id=int(jy_id))
            #for notify issueprice change
            result = oracle_connect.execute(select([zjjy_hk_ipo.c.issueprice]).select_from(zjjy_hk_ipo).where(zjjy_hk_ipo.c.code==code).where(zjjy_hk_ipo.c.jy_id==int(jy_id))).fetchall()
            if(len(result)>0):
            	#print 'issueprice=%s,in jy'%result[0].issueprice
            	newissueprice = result[0].issueprice
            else:
            	#print 'code:%s,jyid:%s is not record in jy'%(code,jy_id)
            	newissueprice = ''
            if(newissueprice!='' and newissueprice!=del_issueprice):
            	notify_issueprice(exchange='HKEX',code=code,lclose=float(newissueprice))
            
              
        except Exception as e:
            print e
            rt=str(e).replace('\'','')
        return HttpResponse("<script>parent.del_result('"+rt+"')</script>")
    elif act=='update' or act=='add':
        code = request.POST.get('code').strip()
        old_code = request.POST.get('old_code').strip()
        id = request.POST.get('stockid')
        #check whether this is a new code
        if(code!=old_code and False==is_zj_new_code(code)):
            return HttpResponse("<script>parent.submit_result('2','"+act+"')</script>")
        #return HttpResponse("<script>parent.submit_result('can submit','"+act+"')</script>")
        if(act=='update'):
            if(code!=old_code and False==is_jy_new_code(code)):
                return HttpResponse("<script>parent.submit_result('3','"+act+"')</script>")
            try:
                print 'oldcode=%s'%old_code
                stock = Stock.objects.get(code=old_code)
               
            except Exception as e:
                print e
        else:#act==add
            stock = Stock()
             
        stockname = request.POST.get('stockname').strip()
        issuevolplanned = request.POST.get('issuevolplanned').strip()
        issuevolplanned = issuevolplanned.replace(',','')
        publicnewshareplanned = request.POST.get('publicnewshareplanned').strip()
        publicnewshareplanned = publicnewshareplanned.replace(',','').strip()
        issuepriceceiling  = request.POST.get('issuepriceceiling').strip()
        issuepricefloor = request.POST.get('issuepricefloor').strip()
        tradeunitpriceatceiling = request.POST.get('tradeunitpriceatceiling').strip()
        exchange = request.POST.get('exchange').strip()
        issuetype = request.POST.get('issuetype').strip()
        applystartdate = request.POST.get('applystartdate').strip()
        issueenddate = request.POST.get('issueenddate').strip()
        proposedlistdate = request.POST.get('proposedlistdate').strip()
        datetoaccount = request.POST.get('datetoaccount').strip()
        tradeunit = request.POST.get('tradeunit').strip()
        issueprice = request.POST.get('issueprice').strip()
        marketcode = request.POST.get('marketcode').strip()
        pin_yin = request.POST.get('pin_yin').strip().upper()
        old_issueprice = request.POST.get('old_issueprice').strip()
        jy_id = request.POST.get('jy_id').strip()
        try:
            stock.code = code
            stock.name=stockname
            if(issuevolplanned!=''):
                stock.issuevolplanned=issuevolplanned
            else:
                stock.issuevolplanned=None
            if(publicnewshareplanned!=''):
                stock.publicnewshareplanned=publicnewshareplanned
            else:
                stock.publicnewshareplanned=None
            if(issuepriceceiling!=''):
                stock.issuepriceceiling=issuepriceceiling
            else:
                stock.issuepriceceiling=None
            if(issuepricefloor!=''):
                stock.issuepricefloor=issuepricefloor
            else:
                stock.issuepricefloor=None
            if(tradeunitpriceatceiling!=''):
                stock.tradeunitpriceatceiling =tradeunitpriceatceiling
            else:
                stock.tradeunitpriceatceiling =None
            stock.exchange=exchange
            stock.issuetype=issuetype
            stock.applystartdate=applystartdate
            stock.issueenddate=issueenddate
            if(proposedlistdate!=''):
                stock.proposedlistdate=proposedlistdate
            else:
                stock.proposedlistdate=None
            if(datetoaccount!=''):
                stock.datetoaccount=datetoaccount
            else:
                stock.datetoaccount=None
            if(tradeunit!=''):
                stock.tradeunit=tradeunit
            else:
                stock.tradeunit=None
            if(issueprice!=''):
                stock.issueprice=issueprice
            else:
                stock.issueprice=None
            stock.marketcode=marketcode
            stock.pin_yin=pin_yin
            if(jy_id!=''):
                stock.jy_id=jy_id
                ijy_id=int(jy_id)
            else:
                ijy_id = 0
            stock.save()
            id=stock.id
            print 'id=%d'%id
            #se='select * from nls_session_parameters'
            #print oracle_connect.execute(se).fetchall()
            
            if(old_issueprice!=issueprice):
            	if(issueprice==''):#修改了发行价为空
            		issueprice = '0'
                print("use redis interface")
                notify_issueprice(exchange='HKEX',code=code,lclose=float(issueprice))
            #同步到 mysql
            print 'code=%s'%code
            
            sync_mysql_by_code(code=code,old_code=old_code,jy_id=ijy_id)
        except Exception as e:
            print e
            rt = str(e).replace("'","")
        return HttpResponse("<script>parent.submit_result('"+rt+"','"+act+"')</script>")
    elif(act=='sync_data'):
        try:
            add_count = 0
            rt =sync_database(calltype='django')
        except Exception as e:
            rt = str(e).replace("'","")
            #print rt
        print "rt=%s"%(rt)
        return HttpResponse("<script>parent.sync_result('"+str(rt)+"','"+str(add_count)+"')</script>")
    else:#处理get的情况
        act=request.GET.get('act')
        if(act=='set_issueprice'):#在列表页填issueprice
            code = request.GET.get('code')
            jy_id = request.GET.get('jy_id')
            issueprice = request.GET.get('issueprice_'+code+'_'+jy_id).strip()
            old_issueprice = request.GET.get('old_issueprice_'+code+'_'+jy_id).strip()
            source = request.GET.get('source')
            try:
                if(source=='ZJ'):
                    stock = Stock.objects.get(code=code)
                    stock.issueprice=issueprice
                    stock.save()
                elif(source=='JY'):
                    stock = Stock()
                    ipo = oracle_connect.execute(zjjy_hk_ipo.select().where(zjjy_hk_ipo.c.code==code).where(zjjy_hk_ipo.c.jy_id==jy_id)).first()
                    stock.name=ipo.name
                    stock.code=ipo.code
                    if(ipo.issuevolplanned):
                        stock.issuevolplanned=ipo.issuevolplanned
                    if(ipo.publicnewshareplanned):
                        stock.publicnewshareplanned=ipo.publicnewshareplanned
                    if(ipo.issuepriceceiling):
                        stock.issuepriceceiling=ipo.issuepriceceiling
                    if(ipo.issuepricefloor):
                        stock.issuepricefloor=ipo.issuepricefloor
                    if(ipo.tradeunitpriceatceiling):
                        stock.tradeunitpriceatceiling=ipo.tradeunitpriceatceiling
                    stock.exchange=ipo.exchange
                    stock.issuetype=ipo.issuetype
                    stock.applystartdate=ipo.applystartdate.strftime('%Y-%m-%d')
                    stock.issueenddate=ipo.issueenddate.strftime('%Y-%m-%d')
                    if(ipo.proposedlistdate):
                        stock.proposedlistdate=ipo.proposedlistdate.strftime('%Y-%m-%d')
                    if(ipo.datetoaccount):
                        stock.datetoaccount=ipo.datetoaccount.strftime('%Y-%m-%d')
                    if(ipo.tradeunit):
                        stock.tradeunit=ipo.tradeunit
                    stock.marketcode=ipo.marketcode
                    if(ipo.pin_yin):
                        stock.pin_yin=ipo.pin_yin
                    stock.issueprice=issueprice
                    stock.jy_id=jy_id
                    stock.save()
                    
                #use redis interface
                if(issueprice!='' and old_issueprice != issueprice):
                    notify_issueprice(exchange='HKEX',code=code,lclose=float(issueprice))
                #save to mysql
                sync_mysql_by_code(code=code,old_code=code,jy_id=int(jy_id))
            except Exception as e:
                str(e).replace("'","")      
                    
            return HttpResponse("<script>parent.set_issuprice_result('"+rt+"','"+code+"','"+jy_id+"','"+issueprice+"')</script>")
        
def show_sync(request):
    render_dic={}
    oracle_zj_count = oracle_connect.execute(select([func.count('*')]).select_from(zjjy_hk_ipo).where(zjjy_hk_ipo.c.source == 'ZJ')).scalar()
    oracle_jy_count = oracle_connect.execute(select([func.count('*')]).select_from(zjjy_hk_ipo).where(zjjy_hk_ipo.c.source == 'JY')).scalar()
    mysql_zj_count = mysql_connect.execute(select([func.count('*')]).select_from(hk_shareipo).where(hk_shareipo.c.source == 'ZJ')).scalar()
    mysql_jy_count = mysql_connect.execute(select([func.count('*')]).select_from(hk_shareipo).where(hk_shareipo.c.source == 'JY')).scalar()
    
    
    render_dic['oracle_zj_count']=oracle_zj_count
    render_dic['oracle_jy_count']=oracle_jy_count
    render_dic['mysql_zj_count']=mysql_zj_count
    render_dic['mysql_jy_count']=mysql_jy_count
    #test
    notify_issueprice()  
    return render(request, 'sync.html',{'render_dic':render_dic})
        
        
def notify_issueprice(exchange='HKEX',code='',lclose=0):    
    #print 'interface_url=%s'%interface_url
    logDir = './stock_apply/log/'
    logFileName = 'notify_%s.log'
    logFrmt = r"%(asctime)s %(message)s"
    logger = None
    #处理日志级别
    logLevel = logging.INFO
    logFile = os.path.join(logDir, logFileName %(getSysDate("%Y%m")))  
    log = Log(logFile, logFrmt, level=logLevel)
    logger = log.getLogger()
    logger.info("begin nitify ..... ")
    ConfFile = "./stock_apply/cfg/DB.cfg"
    DBCnf = ConfigParser.ConfigParser()
    #Read configure
    DBCnf.read( ConfFile )
    requrl = DBCnf.get("INTERFACE", "interface_url")
    logger.info("requrl="+requrl) 
    data={
        "request_data" : {
        "list" : [ {
        "exchange" : exchange,
        "code" : code,
        "lclose" : lclose
        }]},
        "header" : {
        "version" : 1,
        "imei" : "046097B8690EA0D2DDFC76CA05D957C8",
        "key_code" : "1B1D9D39F50EE4302D65A3438FD43067",
        "user_type" : 1,
        "user_name" : "15699885506",
        "auth_code" : "345C51A23487E33CC0E72601B855C1F2",
        "system_time" : 1422263479031,
        "ua" : {
        "trader" : "mining_p"
        } } }    
    jdata= json.dumps(data)
    logger.info("send_date:"+jdata)
    #print jdata
    print '-------------'
    
    try:
        req = urllib2.Request(url = requrl,headers={'Content-Type': 'application/json'}, data =jdata)
        #print 'req:%s'%req
        res_data = urllib2.urlopen(req)
        res = res_data.read()
        logger.info("response:"+res)
        #print res
        #dic_rt = json.loads(res)
        #print dic_rt.get('header').get('response_code')
        
    except Exception as e:
        print str(e)
        logger.info(str(e))  
    logger.info("end nitify ..... ")
    
    return 1
        