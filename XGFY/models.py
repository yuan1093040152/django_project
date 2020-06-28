from django.db import models

#创建数据库
class XGFY_SQL(models.Model):
    #字段
    country = models.CharField(max_length=10,default='Country')   #国家
    nationality = models.IntegerField()  #国别 1=中国，2=外国
    new_add =  models.IntegerField()     #今日新增
    Existing = models.IntegerField()     # 现有病例
    Cumulative = models.IntegerField()   # 累计病例
    Cure = models.IntegerField()         # 治愈病例
    death = models.IntegerField()        # 死亡病例
    creat_time = models.DateField(auto_now=False)   #创建时间，可覆盖

