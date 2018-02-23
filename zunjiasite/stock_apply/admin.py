from django.contrib import admin
from .models import Stock

class StockAdmin(admin.ModelAdmin):
    list_display = ('id','code','name','applystartdate','issueenddate',)
    search_fields = ('code', 'id',)
    list_filter = ('issuetype',)
 
admin.site.register(Stock,StockAdmin)