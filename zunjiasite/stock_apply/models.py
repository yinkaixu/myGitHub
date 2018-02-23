from django.db import models

# Create your models here.
class Stock(models.Model):      
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,null=True)
    code = models.CharField(max_length=10,null=True)
    issuevolplanned = models.DecimalField(max_digits=18, decimal_places=2,null=True)
    publicnewshareplanned = models.DecimalField(max_digits=18, decimal_places=2,null=True)
    issuepriceceiling  = models.DecimalField(max_digits=18, decimal_places=8,null=True)
    issuepricefloor = models.DecimalField( max_digits=18, decimal_places=8 ,null=True)
    tradeunitpriceatceiling = models.DecimalField( max_digits=19, decimal_places=4,null=True)
    exchange = models.CharField(max_length=10,default="HKEX")
    issuetype = models.IntegerField(null=True)
    applystartdate = models.DateField(null=True)
    issueenddate = models.DateField(null=True)
    proposedlistdate = models.DateField(null=True)
    datetoaccount = models.DateField(null=True)
    tradeunit = models.IntegerField(null=True)
    updatetime = models.DateTimeField(auto_now=True)
    marketcode = models.CharField(max_length=10,null=True)
    issueprice = models.DecimalField(max_digits=18, decimal_places=8,null=True)
    pin_yin = models.CharField(max_length=20,null=True) 
    jy_id = models.IntegerField(null=True) 
    
    def __unicode__(self):
        return self.name
      
    class Meta:
        app_label = "stock_apply"
        db_table = 'ZJ_HK_IPO'#define table_name
        

        
