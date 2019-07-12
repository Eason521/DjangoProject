from django.db import models
from Myapp.models import Person


# Create your models here.
#  学科和学生是一对多的关系
# 学科模型类
class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    price = models.IntegerField()

    def __str__(self):
        return '<obj name:{}>'.format(self.name)


# 学生模型类
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    # to：表示要关联的表格
    # on_delete: 删除表格时的策略。
    # 属性 subject 在表格中 会默认增加 _id -->> subject_id
    subject = models.ForeignKey(to='Subject', on_delete=models.CASCADE)

    def __str__(self):
        return '<obj name:{}>'.format(self.name)
