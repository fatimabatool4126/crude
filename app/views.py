from django.shortcuts import render,HttpResponseRedirect
from .forms import UserReg
from .models import User

# Create your views here.


def add(request):
    stud = User.objects.all()
    if request.method == 'POST':
        sm = UserReg(request.POST)
        if sm.is_valid():
            sm.save()
            sm = UserReg()
    else:
        sm = UserReg()
    return render(request, 'add.html', {'form':sm, 'st':stud})
# update students data
def update(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        sm = UserReg(request.POST, instance=pi)
        if sm.is_valid():
            sm.save()
    else:
        pi = User.objects.get(pk=id)
        sm = UserReg(instance=pi)
    return render(request, 'update.html', {'form':sm})
        



# delete student data
def delete(request, id):
    if request.method == 'POST':
        ALI = User.objects.get(pk=id)
        ALI.delete()
        return HttpResponseRedirect('/')
        