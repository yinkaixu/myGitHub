function del_stock(code,jy_id)
{
	 if(confirm('确定要删除代码为"'+code+'"的股票信息吗?'))
 	{
 		myform = document.getElementById('formak');
 		myform.elements["code"].value = code
 		myform.elements["jy_id"].value = jy_id
 		myform.submit();
 		return true;
 	}
 	return false;
}

function del_result(ret)
{
	if(ret=='1')
	{
			//show_hint('删除成功')
		    document.location.reload()
	}
	else
	{
	    show_hint(result)
	}
}

function searchbar_focus(obj)
    {
    	if($(obj).val()=='股票代码或名称')
    	    $(obj).val('')
    }
function searchbar_blur(obj)
{
    if($('#searchbar').val()=='') 
	{
	     $('#searchbar').val('股票代码或名称');
    }
} 
    
function check_search()
{
    searchbar_focus($('#searchbar').get(0))
    return true
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

function check_set_issuprice(code,jy_id)
{
	if($('#issueprice_'+code+'_'+jy_id).val() == '')
	{
		$('#hint_issueprice_'+code+'_'+jy_id).html("请输入发行价");
		return false;
	}
	
	
	if(document.getElementById('issueprice_'+code+'_'+jy_id).value!='' && !isDigit(document.getElementById('issueprice_'+code+'_'+jy_id).value))
	{
		$('#hint_issueprice_'+code+'_'+jy_id).html("无效值");
		return false;	
	}
	if($('#issueprice_'+code+'_'+jy_id).val() == $('#old_issueprice_'+code+'_'+jy_id).val())
	{
		$('#hint_issueprice_'+code+'_'+jy_id).html("没有改动");
		return false;
	}
	return true;
}


function hide_hint_issueprice(code,jy_id)
{
	$('#hint_issueprice_'+code+'_'+jy_id).html("");
}

function set_issueprice(code,jy_id,value,source)
{
  var str='<form id="form'+code+'_'+jy_id+'" action="/info_submit/"  method="get" target=infopost onsubmit="return check_set_issuprice(\''+code+'\',\''+jy_id+'\')">'
   str+='<input style="width:55px;" type="text" id="issueprice_'+code+'_'+jy_id+'" name="issueprice_'+code+'_'+jy_id+'"  value="'+value+'" onfocus="hide_hint_issueprice(\''+code+'\',\''+jy_id+'\')">'
   str+='<input type="hidden" id="old_issueprice_'+code+'_'+jy_id+'" name="old_issueprice_'+code+'_'+jy_id+'" value="'+value+'">'
   str+='<input type="hidden" id="act" name="act" value="set_issueprice">'
   str+='<input type="hidden" id="code" name="code" value="'+code+'">'
   str+='<input type="hidden" id="jy_id" name="jy_id" value="'+jy_id+'">'
   str+='<input type="hidden" id="source" name="source" value="'+source+'">'
   str+='<button type="submit" >存</button>'
   str+='</form>'
   document.getElementById('div_issueprice_'+code+'_'+jy_id).innerHTML=str;
   $('#hint_issueprice_'+code+'_'+jy_id).html("");
}

function set_issuprice_result(ret,code,jy_id,val)
{
	 //document.location.reload()
	 if(ret=='1')
	 {
	     var content = "<div onclick=\"set_issueprice('"+code+"','"+jy_id+"','"+val+"','ZJ')\">"+val+"</div>";
	     $('#div_issueprice_'+code+'_'+jy_id).html(content);
	     $('#hint_issueprice_'+code+'_'+jy_id).html("提交成功");
	     $('#source_'+code+'_'+jy_id).css("color","#d20");
	     $('#source_'+code+'_'+jy_id).html("尊嘉");
	     content = "<input type=\"button\" onclick=\"del_stock('"+code+"','"+jy_id+"')\" value=\"删除\">";
	     $('#span_btn_del_'+code+'_'+jy_id).html(content);
	    
	 }
	 else
	 {
	 	$('#hint_issueprice_'+code+'_'+jy_id).html(ret);	
	 }
}

