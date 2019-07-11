from django.shortcuts import render,redirect,render_to_response,HttpResponse
from Myapp.models import *

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
        gender=request.POST.get('gender')
        birthday=request.POST.get('birthday')
        id = request.POST.get('id')

        person_obj = Person.objects.get(id=id)
        person_obj.name=username
        person_obj.age=age
        person_obj.gender=gender
        person_obj.birthday=birthday
        person_obj.save()
        return redirect("/all/")
    else:
        id = request.GET.get('id')
        person_obj = Person.objects.get(id=id)
        return render(request, 'myapp/update.html', {'person_obj': person_obj})
