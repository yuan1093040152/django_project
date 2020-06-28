from django.db import models

#创建数据库

class emp_login(models.Model):
    class Meta:
        db_table = 'emp_login'  #表名
    username = models.CharField(max_length=255,blank = False)  #用户名
    password = models.CharField(max_length=255,blank = False)  #密码
    problem =  models.CharField(max_length=255,blank = False)  #问题
    answer =   models.CharField(max_length=255,blank = False)  #答案
    creat_time = models.DateField(auto_now=False)  # 创建时间，可覆盖