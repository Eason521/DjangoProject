from django.shortcuts import render, redirect, render_to_response, HttpResponse
from Myapp.models import Person


# Create your views here.


def add_person(request):
    if request.method == "POST":
        username = request.POST.get('uesrname')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        birthday = request.POST.get('birthday')
        # print(username,age)

        Person.objects.create(
            name=username,
            age=age,
            gender=gender,
            birthday=birthday
        )
        # return HttpResponse("成功")
        return redirect("/all/")
    else:
        return render(request, "myapp/add.html")


def all_person(request):
    person_obj_lst = Person.objects.all()

    return render(request, "myapp/all.html", {"person_obj_list": person_obj_lst})


def delete_person(request):
    id = request.GET.get('id')
    Person.objects.get(id=id).delete()
    return redirect("/all/")


def update_person(request):
    if request.method == "POST":
        username = request.POST.get('username')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        birthday = request.POST.get('birthday')
        id = request.POST.get('id')

        person_obj = Person.objects.get(id=id)
        person_obj.name = username
        person_obj.age = age
        person_obj.gender = gender
        person_obj.birthday = birthday
        person_obj.save()
        return redirect("/all/")
    else:
        id = request.GET.get('id')
        person_obj = Person.objects.get(id=id)
        return render(request, 'myapp/update.html', {'person_obj': person_obj})


# #   常用方法
#
#
# def test_all(request):
#     # 1. all() 返回一个QuerySet对象
#     person_obj_list = models.Person.objects.all()
#     print(person_obj_list)
#     # <QuerySet [<Person: <obj: name:zs>]>
#     print(person_obj_list[0].name)  # 取出第一个对象的name值。
#     return HttpResponse('请求返回测试页面')
#
#
# def test_filter(request):
#     # 2. filter() ： 过滤  返回一个QuerySet对象，
#     # select * from person where name='ls' and age = 12
#     ret = models.Person.objects.filter(age=12, name='ls')  # 默认使用and 连接。
#     print(ret)
#     # <QuerySet [<Person: <obj: name:ls>>, <Person: <obj: name:ww>>]>
#     return HttpResponse('请求返回测试页面')
#
#
# def test_get(request):
#     # 3. get() 只能查询出唯一的一个 ： 返回的是一个具体对象
#     person_obj = models.Person.objects.get(id=2)
#     print(person_obj)  # <obj: name:zs>
#     print(person_obj.name)
#     # 如果不存在则报错
#     person_obj = models.Person.objects.get(id=1)
#     print(person_obj)
#     person_obj_lst = models.Person.objects.filter(id=1)
#     print(person_obj_lst)  # <QuerySet []>
#     if person_obj_lst:
#         pass
#     else:
#         pass
#     return HttpResponse('请求返回测试页面')
#
#
# def test_first(request):
#     # 4. first()： 返回一个具体的对象。
#     ret = models.Person.objects.filter(age=12)
#     print(ret)  # <QuerySet [<Person: <obj: name:ls>>, <Person: <obj: name:ww>>]>
#     ret1 = models.Person.objects.filter(age=12).first()
#     print(ret1)  # <obj: name:ls>
#     return HttpResponse('请求返回测试页面')
#
#
# def test_last(request):
#     # 5. last(): 也是具体的对象
#     ret = models.Person.objects.filter(age=12).last()
#     print(ret)  # <obj: name:ww>
#     ret = models.Person.objects.filter(age=10).first()
#     print(ret)  # None
#     ret = models.Person.objects.filter(age=10)
#     print(ret[0])  # 报错！！！ list index out of range
#     return HttpResponse('请求返回测试页面')
#
#
# def test_exclude(request):
#     # 6.exclude() :返回与所给筛选条件不匹配的对象 ， 返回 QuerySet对象，
#     person_obj_lst = models.Person.objects.exclude(age=11)
#     print(person_obj_lst)
#     # <QuerySet [<Person: <obj: name:ls>>, <Person: <obj: name:ww>>]>
#     return HttpResponse('请求返回测试页面')
#
#
# def test_values(request, 对象中包含的是字典的形式=None):
#     # 7. values(): 返回一个QuerySet 对象，对象中包含的是字典的形式。
#     ret = models.Person.objects.filter(age=12).values()
#     print(ret)
#     # 返回一个QuerySet 对象，对象中包含的是字典的形式。
#     # <QuerySet [{'id': 3, 'age': 12, 'birthday': datetime.date(2019, 7, 12),'name': 'ls'}, {'id': 4, 'age': 12, 'birthday': datetime.date(2019, 7, 12), 'name': 'ww'}]>
#     ret = models.Person.objects.filter(age=12).values('name')
#     print(ret)  # <QuerySet [{'name': 'ls'}, {'name': 'ww'}]>
#     return HttpResponse('请求返回测试页面')
#
#
# def test_values_list(request):
#     # 8.values_list(*field): 它与values()非常相似，它返回的是一个元组序列
#     ret =models.Person.objects.filter(age=12).values_list('name')
#     print(ret) # <QuerySet [('ls',), ('ww',)]>
#     return HttpResponse('请求返回测试页面')
#
#
# def test_order_by(request):
#     # 9. order_by(*field):  对查询结果排序
#     #  负号 "-" : 表示降序。
#     person_obj_list = Person.objects.all().order_by('-age','name')
#     print(person_obj_list)
#     # <QuerySet [<Person: <obj: name:ls>>, <Person: <obj: name:ww>>, <Person: <obj: name:zs>>]>
#     # <QuerySet [<Person: <obj: name:zs>>, <Person: <obj: name:ls>>, <Person: <obj: name:ww>>]>
#     return HttpResponse('请求返回测试页面')
#
#
# def test_person_obj_list(request):
#     # 10. reverse():  对查询结果反向排序
#     person_obj_list = Person.objects.all().order_by('age').reverse()
#     print(person_obj_list)
#     # <QuerySet [<Person: <obj: name:zs>>, <Person: <obj: name:ls>>, <Person: <obj: name:ww>>]>
#     return HttpResponse('请求返回测试页面')
#
#
# def test_count(request):
#     # 11. count(): 返回数据库中匹配查询(QuerySet)的对象数量。
#     ret =Person.objects.all().count()
#     print(ret) # 3
#     return HttpResponse('请求返回测试页面')
#
#
# def test_exists(request):
#     # 12.exists():  如果QuerySet包含数据，就返回True，否则返回False
#     ret = Person.objects.exists()
#     print(ret)  # True
#     """
#     总结:
#     1．返回具体对象方法get()、first()、last()
#     2．返回QuerySet对象方法
#         all()、filter()、exclude()、order_by()、reverse()、
#         values() 返回一个可迭代的字典序列。
#         values_list() 返回一个可迭代的元祖序列。
#     3．返回Boolean值方法 exists()
#     4．返回数字的方法count()
#     """
#     return HttpResponse('请求返回测试页面')
