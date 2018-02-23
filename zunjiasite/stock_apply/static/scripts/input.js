 var dic_op = { 
 				"1": "操作成功", 
 				"2": "此代码系统中已有，不能重复",
 				"3": "此代码聚源中已有，不能重复"
 			};

function get_content_by_dic(num)
{
	rt="";
	for (var key in dic_op) 
	{
		if(key==num) rt=dic_op[key]
	}
	return rt;
}

setSelect=function(_sName, _sVal)
  {
                var oObj = document.getElementsByName(_sName);
                for (var i = 0; i < oObj.length; i++)
                {
                        if (oObj[i].type == "select-one")
                        {
                                for (var j = 0; j < oObj[i].options.length; j++)
                                {
                                        if (_sVal == oObj[i].options[j].value)
                                        {
                                                oObj[i].options[j].selected = true;
                                        }
                                }
                        }
                        if ((oObj[i].type == "checkbox" || oObj[i].type == "radio") && _sVal == oObj[i].value)
                        {
                                oObj[i].checked = true;
                        }
                }
  }

	function submit_result(ret,act)
	{
		if(ret=='1')
		{
			show_hint('提交成功');
			/*
			if(act=='update')
			{
				location.href='/list/';
			}
			else if(act=='add')
			{
				document.getElementById('stockname').value='';
			    document.getElementById('code').value='';
			    document.getElementById('issuevolplanned').value='';
			    document.getElementById('publicnewshareplanned').value='';
			    document.getElementById('issueprice').value='';
			    document.getElementById('issuepriceceiling').value='';
			    document.getElementById('issuepricefloor').value='';
			    document.getElementById('tradeunitpriceatceiling').value='';
			    document.getElementById('exchange').value='HKEX';
			    setSelect('issuetype','0')
			    setSelect('marketcode','0')
			    document.getElementById('applystartdate').value='';
			    document.getElementById('issueenddate').value='';
			    document.getElementById('proposedlistdate').value='';
			    document.getElementById('datetoaccount').value='';
			    document.getElementById('tradeunit').value='';
			    document.getElementById('pin_yin').value='';
			}
			*/
			location.href='/list/';		
		}
		else
		{
			conent = get_content_by_dic(ret);
			show_hint(conent);
		}
	}

//校验是否全由数字组成 
function isDigit(s) 
{ 
	//alert(s)
var re = /^\d{1,3}[,\.\d{3}]*$/;
//alert(re.test(s)); 
	if(!re.test(s)) 
		return false 
	else
		return true 
}	
//校验是否字母
function isaletter(s)
{
	var re = /^[a-zA-Z]*$/;
	if(!re.test(s)) 
		return false 
	else
		return true 
}


function mycheck()
	{
		//if(document.getElementById('stockname').value==''){show_hint('"股票名称"不能为空!');return false;} 
    	if(document.getElementById('code').value==''){show_hint('"股票代码"不能为空!');return false;}
    	if(document.getElementById('code').value.trim().length!=5)
	    {
	    	show_hint('股票代码长度应为5位');
	    	return false;
	    }
    	
    	//if(document.getElementById('issuevolplanned').value==''){show_hint('"计划发行总股数"不能为空!');return false;}
    	if( document.getElementById('issuevolplanned').value!='' && !isDigit(document.getElementById('issuevolplanned').value))
    	{
    		show_hint('"计划发行总股数"不是有效数字!');return false;
    	}
    	//if(document.getElementById('publicnewshareplanned').value==''){show_hint('"公开发售新股股数"不能为空!');return false;}
    	if(document.getElementById('publicnewshareplanned').value!='' && !isDigit(document.getElementById('publicnewshareplanned').value))
    	{
    		show_hint('"公开发售新股股数"不是有效数字!');return false;
    	}
    	if(document.getElementById('issueprice').value!='' && !isDigit(document.getElementById('issueprice').value))
    	{
    		show_hint('"发行价"不是有效数字!');return false;
    	}
    	//if(document.getElementById('issueprice').value==''){show_hint('"发行价"不能为空!');return false;}
    	//if(document.getElementById('tradeunit').value==''){show_hint('"买卖单位"不能为空!');return false;}
    	if(document.getElementById('issuepriceceiling').value!='' && !isDigit(document.getElementById('issuepriceceiling').value))
    	{
    		show_hint('"每股最低价"不是有效数字!');return false;
    	}
    	//if(document.getElementById('issuepricefloor').value==''){show_hint('"每股最高价"不能为空!');return false;}
    	if(document.getElementById('issuepricefloor').value!='' && !isDigit(document.getElementById('issuepricefloor').value))
    	{
    		show_hint('"每股最高价"不是有效数字!');return false;
    	}
    	//if(document.getElementById('tradeunitpriceatceiling').value==''){show_hint('"按最高价每手支付价格"不能为空!');return false;}
    	if(document.getElementById('tradeunitpriceatceiling').value!='' && !isDigit(document.getElementById('tradeunitpriceatceiling').value))
    	{
    		show_hint('"按最高价每手支付价格"不是有效数字!');return false;
    	}
    	//if(document.getElementById('tradeunit').value==''){show_hint('"买卖单位"不能为空!');return false;}
    	if(document.getElementById('tradeunit').value!='' && !isDigit(document.getElementById('tradeunit').value))
    	{
    		show_hint('"买卖单位"不是有效数字!');return false;
    	}
    	
    	if(document.getElementById('exchange').value==''){show_hint('"交易所"不能为空!');return false};
    	
    	
    	var obj = document.getElementById('marketcode')
    
    	if(obj.options[obj.options.selectedIndex].value=='0')
    	{
    		show_hint('请选择"市场代码"');return false;
    	}
        
        obj = document.getElementById('issuetype')
    
    	if(obj.options[obj.options.selectedIndex].value=='0')
    	{
    		show_hint('请选择"发行类别"');return false;
    	}
    
 
    	if(document.getElementById('applystartdate').value==''){show_hint('"申购起始日"不能为空!');return false;}
    	if(document.getElementById('issueenddate').value==''){show_hint('"发行截止日"不能为空!');return false;}
    	//if(document.getElementById('proposedlistdate').value==''){show_hint('"预计上市日"不能为空!');return false;}
    	//if(document.getElementById('datetoaccount').value==''){show_hint('"股票发放日"不能为空!');return false;}
    	//if(document.getElementById('pin_yin').value==''){show_hint('"拼音首字母"不能为空!');return false;}
    	if(document.getElementById('pin_yin').value!='' && !isaletter( document.getElementById('pin_yin').value))
    	{
    		show_hint('"拼音首字母"应是字母!');
    		return false;
    	}
        //show_hint('can submit')
    	//return false;
    return true;
	}
function comdify(n){
　　var re=/\d{1,3}(?=(\d{3})+$)/g;
　　var n1=n.replace(/^(\d+)((\.\d+)?)$/,function(s,s1,s2){return s1.replace(re,"$&,")+s2;});
　　return n1;
}
//给input的value添加千分符
function add_separator(obj)
{
	var reg = new RegExp( ',',"g" )
	//var str = String(obj.value);
	var  newvalue= String(obj.value).replace(reg,'');
	obj.value = comdify(newvalue)
	
}

//当输入内容不正确时，设置input边框为红色,并且给某两个input添加千分符
function check_value(obj)
{
	flag=1
	
	
	
	if(obj.value=='' && (obj.id=='code'||obj.id=='exchange'||obj.id=='applystartdate'||obj.id=='issueenddate') )
	{
		flag=0
	}
	
	if(obj.id =='code')
	{
		val= obj.value.trim();
	    if(val.length!=5)
	    {
	    	flag=0;
	    	show_hint('股票代码长度应为5位');
	    }
    }
	
	//添加千分符
	if(obj.id=='issuevolplanned'|| obj.id=='publicnewshareplanned')
	{
		add_separator(obj)
	}
	
	if( obj.value!='' && (obj.id=='issuevolplanned'|| obj.id=='publicnewshareplanned'||obj.id=='issuepriceceiling'
		||obj.id=='issuepricefloor'||obj.id=='tradeunitpriceatceiling'||obj.id=='tradeunit'||obj.id=='issueprice'))
	{
		if(!isDigit(obj.value))
			flag=0
	}
	
	if(obj.id=='pin_yin')
	{
		if(!isaletter(obj.value))
			flag=0
	}
	
	
	if(flag==1)
	{
		obj.style.border = '1px #ccc solid'
	}
	else
	{
		obj.style.border = '1px #c00 solid'
	}
}
