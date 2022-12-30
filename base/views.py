from django.db.models import Q
from django.shortcuts import render, HttpResponse, redirect
from base.form import EmployeeForm
from base.models import EmployeDetail


# Create your views here.


def home(request):
    return render(request, 'home.html')


def allEmployee(request):
    employe_detail = EmployeDetail.objects.all()
    context = {'employe_detail': employe_detail}
    return render(request, 'subpage/all_employee.html', context)


def addEmployee(request):
    # for form model data getting
    form = EmployeeForm()
    context = {'form': form}
    # check the data is coming or not
    if request.method == 'POST':
        # for form templete this method to use data
        form = EmployeeForm(request.POST)
        # checking the form is valid or not
        if form.is_valid():
            # this is save the form in database
            form.save()
            return redirect('home')

    return render(request, 'subpage/add_employee.html', context)


def removeEmployee(request, pk):
    form = EmployeDetail.objects.get(id=pk)
    if request.method == 'POST':
        form.delete()
        return render(request, 'subpage/all_employee.html')
    return render(request, 'subpage/remove_employee.html')


def filterEmployee(request):
    search_data = request.GET.get('search')
    if search_data:
        employe_detail = EmployeDetail.objects.filter(
            Q(fullname__icontains=search_data))
        return render(request, 'subpage/filter_employee.html', {'employe_detail': employe_detail})
   
    return render(request, 'subpage/filter_employee.html')
