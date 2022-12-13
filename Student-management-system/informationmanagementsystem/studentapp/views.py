from django.shortcuts import render, redirect

from studentapp.forms import StudentForm
from studentapp.models import Student


# Create your views here.
def addStudent(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                return redirect("/all-students")
            except:
                pass
    else:
        form = StudentForm()
    return render(request, 'index.html', {"form": form})


def getAllData(request):
    students = Student.objects.all() #  select * from table ;
    return render(request, "show.html", {"students": students})


def edit(request, id):
    student = Student.objects.get(id=id)# select * from table where id = id
    return render(request, "edit.html", {"student": student})


def update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
        form.save()
        return redirect("/all-students")
    return render(request, "edit.html", {"student": student})


def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("/all-students")
