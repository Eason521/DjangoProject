from django.shortcuts import render, redirect, render_to_response
from django.shortcuts import HttpResponse
from Myapp.models import Person
from CommonMethod.models import Student, Subject


# Create your views here.
#   常用方法


def test_all(request):
    # 1. all() 返回一个QuerySet对象
    person_obj_list = Person.objects.all()
    print(person_obj_list)
    # <QuerySet [<Person: <obj: name:zs>]>
    print(person_obj_list[0].name)  # 取出第一个对象的name值。
    return HttpResponse(person_obj_list[0].name)


def test_filter(request):
    # 2. filter() ： 过滤  返回一个QuerySet对象，
    # select * from person where name='ls' and age = 12
    ret = Person.objects.filter(age=12, name='ls')  # 默认使用and 连接。
    print(ret)
    # <QuerySet [<Person: <obj: name:ls>>, <Person: <obj: name:ww>>]>
    return HttpResponse(ret)


def test_get(request):
    # 3. get() 只能查询出唯一的一个 ： 返回的是一个具体对象
    person_obj = Person.objects.get(id=2)
    print(person_obj)  # <obj: name:zs>
    print(person_obj.name)
    # 如果不存在则报错
    person_obj = Person.objects.get(id=1)
    print(person_obj)
    person_obj_lst = Person.objects.filter(id=1)
    print(person_obj_lst)  # <QuerySet []>
    if person_obj_lst:
        pass
    else:
        pass
    return HttpResponse(person_obj_lst)


def test_first(request):
    # 4. first()： 返回一个具体的对象。
    ret = Person.objects.filter(age=28)
    print(ret)  # <QuerySet [<Person: <obj: name:ls>>, <Person: <obj: name:ww>>]>
    ret1 = Person.objects.filter(age=12).first()
    print(ret1)  # <obj: name:ls>
    return HttpResponse(ret, ret1)


def test_last(request):
    # 5. last(): 也是具体的对象
    # ret = Person.objects.filter(age=28).last()
    # print(ret)  # <obj: name:ww>
    ret = Person.objects.filter(age=10).first()
    print(ret)  # None
    # ret = Person.objects.filter(age=10)
    # print(ret[0])  # 报错！！！ list index out of range
    return HttpResponse(ret)


def test_exclude(request):
    # 6.exclude() :返回与所给筛选条件不匹配的对象 ， 返回 QuerySet对象，
    person_obj_lst = Person.objects.exclude(age=11)
    print(person_obj_lst)
    # <QuerySet [<Person: <obj: name:ls>>, <Person: <obj: name:ww>>]>
    return HttpResponse(person_obj_lst)


def test_values(request):
    # 7. values(): 返回一个QuerySet 对象，对象中包含的是字典的形式。
    ret = Person.objects.filter(age=12).values()
    print(ret)
    # 返回一个QuerySet 对象，对象中包含的是字典的形式。 <QuerySet [{'id': 3, 'age': 12, 'birthday': datetime.date(2019, 7, 12),
    # 'name': 'ls'}, {'id': 4, 'age': 12, 'birthday': datetime.date(2019, 7, 12), 'name': 'ww'}]>
    ret = Person.objects.filter(age=28).values('name')
    print(ret)  # <QuerySet [{'name': 'ls'}, {'name': 'ww'}]>
    return HttpResponse(ret)


def test_values_list(request):
    # 8.values_list(*field): 它与values()非常相似，它返回的是一个元组序列
    ret = Person.objects.filter(age=12).values_list('name')
    print(ret)  # <QuerySet [('ls',), ('ww',)]>
    return HttpResponse(ret)


def test_order_by(request):
    # 9. order_by(*field):  对查询结果排序
    #  负号 "-" : 表示降序。
    person_obj_list = Person.objects.all().order_by('-age', 'name')
    print(person_obj_list)
    # <QuerySet [<Person: <obj: name:ls>>, <Person: <obj: name:ww>>, <Person: <obj: name:zs>>]>
    # <QuerySet [<Person: <obj: name:zs>>, <Person: <obj: name:ls>>, <Person: <obj: name:ww>>]>
    return HttpResponse(person_obj_list)


def test_person_obj_list(request):
    # 10. reverse():  对查询结果反向排序
    person_obj_list = Person.objects.all().order_by('age').reverse()
    print(person_obj_list)
    # <QuerySet [<Person: <obj: name:zs>>, <Person: <obj: name:ls>>, <Person: <obj: name:ww>>]>
    return HttpResponse(person_obj_list)


def test_count(request):
    # 11. count(): 返回数据库中匹配查询(QuerySet)的对象数量。
    ret = Person.objects.all().count()
    print(ret)  # 3
    return HttpResponse(ret)


def test_exists(request):
    # 12.exists():  如果QuerySet包含数据，就返回True，否则返回False
    ret = Person.objects.exists()
    print(ret)  # True
    return HttpResponse(ret)

    """
    总结:
    1．返回具体对象方法get()、first()、last()
    2．返回QuerySet对象方法
        all()、filter()、exclude()、order_by()、reverse()、
        values() 返回一个可迭代的字典序列。
        values_list() 返回一个可迭代的元祖序列。
    3．返回Boolean值方法 exists()
    4．返回数字的方法count()
    """


# 双下划线方法
def test1(request):
    # 1. xx__lt : 小于
    # person_obj_lst =models.Person.objects.filter(age__lt=13)
    # print(person_obj_lst) # <QuerySet [<Person: <obj: name:ls>>, <Person: <obj: name:ww>>]>
    # 2. xx__lte: 小于等于
    # person_obj_lst =models.Person.objects.filter(age__lte=13)
    # print(person_obj_lst) # <QuerySet [<Person: <obj: name:zs>>, <Person: <obj: name:ls>>, <Person: <obj: name:ww>>]>
    # 3. xx__gt : 大于
    # person_obj_lst =models.Person.objects.filter(age__gt=12)
    # print(person_obj_lst) # <QuerySet [<Person: <obj: name:zs>>]>
    # 4. xx__gte: 大于等于
    # person_obj_lst = models.Person.objects.filter(age__gte=12)
    # print(person_obj_lst)  #<QuerySet [<Person: <obj: name:zs>>, <Person: <obj: name:ls>>, <Person: <obj: name:ww>>]>

    # 5. xx__in ： 包含某些值
    # person_obj_lst =models.Person.objects.filter(age__in=[10,11])
    # print(person_obj_lst) # <QuerySet [<Person: <obj: name:zs>>, <Person: <obj: name:ls>>]>

    # 6. 不包含， exclude() 和 age__in 联合使用
    # ret =models.Person.objects.exclude(age__in=[10,11])
    # print(ret) # <QuerySet [<Person: <obj: name:ww>>]>

    # 7．xx__contains(): 包含某个字符的记录
    # ret =models.Person.objects.filter(name__contains='s')
    # print(ret)
    # <QuerySet [<Person: <obj: name:zs>>, <Person: <obj: name:ls>>]>
    # 8.  xx__icontains() 忽略大小写  (sqlite3 不支持)

    # 9．xx__range(): 查找范围
    # ret =models.Person.objects.filter(age__range=[10,12])
    # print(ret)
    # <QuerySet [<Person: <obj: name:zs>>, <Person: <obj: name:ls>>, <Person: <obj: name:ww>>]>

    # 10．name__startswith='z' : 获取 以 z 开头的记录
    # ret =models.Person.objects.filter(name__startswith='z')
    # print(ret) # <QuerySet [<Person: <obj: name:zs>>, <Person: <obj: name:zss>>]>

    # 11. name__endswith='s'
    # ret =models.Person.objects.filter(name__endswith='s')
    # print(ret)
    # <QuerySet [<Person: <obj: name:zs>>, <Person: <obj: name:ls>>, <Person: <obj: name:zss>>]>

    # 12.date类型字段可以根据年月日进行过滤
    ret = Person.objects.filter(birthday__year=2019)
    print(ret)
    # <QuerySet [<Person: <obj: name:zs>>, <Person: <obj: name:ls>>, <Person: <obj: name:ww>>, <Person: <obj: name:zss>>]>

    return HttpResponse(ret)


# 一对多CRUD操作
def test2(request):
    # 1.查询操作
    # 正向查询
    # zs 对应的学科
    student_obj = Student.objects.get(name='邓紫棋')
    print(student_obj) # <obj name:zs>
    # subject_obj = Subject.objects.get(id=student_obj.subject_id)
    # print(subject_obj) # <obj name:python>

    # student_obj = Student.objects.get(name='zs')
    # subject_obj =student_obj.subject # 返回一个对象
    # print(subject_obj) # <obj name:python>
    # print(subject_obj.name) # python
    # 反向查询
    # 查询 学python的 学员
    # sub_obj = Subject.objects.get(name='python')
    # ret =sub_obj.student_set.all() # 默认使用 类名小写_set 属性进行关联。
    # print(ret)
    # <QuerySet [<Student: <obj name:zs>>, <Student: <obj name:ls>>]>

    # 2.增加操作
    # 新增学员 邓诗颖 学python
    # sub_obj = Subject.objects.get(name='Python')
    # stu_obj = Student()
    # stu_obj.name='邓诗颖'
    # # stu_obj.subject= sub_obj # 赋值对象
    # stu_obj.subject_id=sub_obj.id # 赋值id
    # stu_obj.save()

    # stu_obj = Student.objects.create(
    #     name='金鱼嘴',
    #     subject=sub_obj
    # )
    # print(stu_obj) # 返回创建好的对象: <obj name:金鱼嘴>

    # java 学科 新增一个学员 jj
    # sub_obj=m Subject.objects.get(name='java')
    # sub_obj.student_set.create(name='jj')

    # 3.删除操作
    # 删除jj
    # Student.objects.get(name='jj').delete()
    # Student.objects.filter(name__contains='j').delete()
    # java 毕业了，会级联删除对应的学员。
    # models.Subject.objects.get(name='java').delete()

    # 4. 修改
    # zs 转学 java
    # sub_obj = Subject.objects.get(name='java')
    # stu_obj = Student.objects.get(name='zs')
    # stu_obj.subject=sub_obj
    # stu_obj.save()
    # 使用 update()
    # sub_obj = Subject.objects.get(name='java')
    # models.Student.objects.filter(name='zs').update(subject=sub_obj)

    # sub_obj = Subject.objects.get(name='java')
    # stu_obj1 = Student.objects.get(name='zs')
    # stu_obj2 = Student.objects.get(name='ls')
    # sub_obj.student_set.set([stu_obj1, stu_obj2])

    return HttpResponse('请求成功，返回内容请看pycharm控制台')
