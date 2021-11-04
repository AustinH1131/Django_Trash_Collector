from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from datetime import date
import calendar
from django.apps import apps
from django.contrib.auth import get_user_model


from .models import Employee


# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


@login_required
def index(request):
    # The following line will get the logged-in user (if there is one) within any view function
    logged_in_user = request.user
    try:
        # This line will return the employee record of the logged-in user if one exists
        logged_in_employee = Employee.objects.get(user=logged_in_user)

        today = date.today()
        
        context = {
            'logged_in_employee': logged_in_employee,
            'today': today
        }
        return render(request, 'employees/index.html', context)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('employees:create'))

# def index(request):
#     # This line will get the employee model from the other app, it can now be used to query the db for employees
#     employee = apps.get_model('employees.employee')

#     return render(request, 'employees/index.html')

# Input employee information
@login_required
def create(request):
    logged_in_user = request.user
    if request.method == "POST":
        name_from_form = request.POST.get('name')
     
        new_employee = Employee(name=name_from_form, user=logged_in_user)
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/create.html')


@login_required
def edit_profile(request):
    logged_in_user = request.user
    logged_in_employee = Employee.objects.get(user=logged_in_user)
    if request.method == "POST":
        name_from_form = request.POST.get('name')
        address_from_form = request.POST.get('address')
        zip_from_form = request.POST.get('zip_code')
        weekly_pickup_from_form = request.POST.get('weekly')
        logged_in_employee.name = name_from_form
        logged_in_employee.address = address_from_form
        logged_in_employee.zip_code = zip_from_form
        logged_in_employee.weekly_pickup = weekly_pickup_from_form
        logged_in_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        context = {
            'logged_in_employee': logged_in_employee
        }
        return render(request, 'employees/edit_profile.html', context)


@login_required
def pickup_list(request):
    curr_date = date.today()
    logged_in_user=request.user
    logged_in_employee = Employee.objects.get(user=logged_in_user)
    Customer = apps.get_model('customers.Customer')
    employee_zip= logged_in_employee.zip_code
    # customer_zip= Customer.objects.filter(zip_code = employee_zip).filter(Q(weekly_pickup = (calendar.day_name[curr_date.weekday()])) | Q(one_time_pickup = (curr_date)))
    customer_zip= Customer.objects.filter(zip_code = employee_zip).filter(Q(weekly_pickup = (calendar.day_name[curr_date.weekday()])) | Q(one_time_pickup = (curr_date))).exclude(Q(date_of_last_pickup = curr_date) | Q(suspend_end__gt= curr_date, suspend_start__lt=curr_date))
    context={
        "customer_zip" : customer_zip
    }      

    return render(request,'employees/pickup_list.html', context)

@login_required
def pickup_confirm(request, customer_id):
    Customer = apps.get_model('customers.Customer')
    customer_object = Customer.objects.get(pk=customer_id)
    # date_pickup = customer_object.date_of_last_pickup
    customer_object.date_of_last_pickup = date.today()
    customer_object.balance -= 20
    customer_object.save()
  
        # Customer = apps.get_model('customers.Customer')
        # customer_pickup= Customer.objects.filter(zip_code = employee_zip)
        # context={
        #     "customer_zip" : customer_zip
        # }      
        # customer_balance +=20
        # customer_balance.save()
    # return render(request, 'employees/pickup_list.html',)
    return HttpResponseRedirect(reverse('employees:pickup_list'))
  
        # return render(request, 'employees/pickup_list.html', context)

@login_required
def sunday(request):
    logged_in_user=request.user
    logged_in_employee = Employee.objects.get(user=logged_in_user)
    Customer = apps.get_model('customers.Customer')
    employee_zip= logged_in_employee.zip_code
    customer_zip= Customer.objects.filter(zip_code = employee_zip).filter(weekly_pickup="Sunday")
    context={
        "customer_zip" : customer_zip
    }     
    return render(request,'employees/pickup_list.html', context)

@login_required
def monday(request):
    logged_in_user=request.user
    logged_in_employee = Employee.objects.get(user=logged_in_user)
    Customer = apps.get_model('customers.Customer')
    employee_zip= logged_in_employee.zip_code
    customer_zip= Customer.objects.filter(zip_code = employee_zip).filter(weekly_pickup="Monday")
    # curr_date = date.today()
    # if customer_zip.suspend_end __gt= curr_date and customer_zip.suspend_start __lt= curr_date:
    #     active = "Yes"
    # else:
    #     active = "No"
    context={
        "customer_zip" : customer_zip,
    #     "active" : active
    }      
    return render(request,'employees/pickup_list.html', context)


@login_required
def tuesday(request):
    logged_in_user=request.user
    logged_in_employee = Employee.objects.get(user=logged_in_user)
    Customer = apps.get_model('customers.Customer')
    employee_zip= logged_in_employee.zip_code
    customer_zip= Customer.objects.filter(zip_code = employee_zip).filter(weekly_pickup="Tuesday")
    context={
        "customer_zip" : customer_zip
    }      
    return render(request,'employees/pickup_list.html', context)

@login_required
def wednesday(request):
    logged_in_user=request.user
    logged_in_employee = Employee.objects.get(user=logged_in_user)
    Customer = apps.get_model('customers.Customer')
    employee_zip= logged_in_employee.zip_code
    customer_zip= Customer.objects.filter(zip_code = employee_zip).filter(weekly_pickup="Wednesday")
    context={
        "customer_zip" : customer_zip
    }      
    return render(request,'employees/pickup_list.html', context)

@login_required
def thursday(request):
    logged_in_user=request.user
    logged_in_employee = Employee.objects.get(user=logged_in_user)
    Customer = apps.get_model('customers.Customer')
    employee_zip= logged_in_employee.zip_code
    customer_zip= Customer.objects.filter(zip_code = employee_zip).filter(weekly_pickup="Thursday")
    context={
        "customer_zip" : customer_zip
    }      
    return render(request,'employees/pickup_list.html', context)

@login_required
def friday(request):
    logged_in_user=request.user
    logged_in_employee = Employee.objects.get(user=logged_in_user)
    Customer = apps.get_model('customers.Customer')
    employee_zip= logged_in_employee.zip_code
    customer_zip= Customer.objects.filter(zip_code = employee_zip).filter(weekly_pickup="Friday")
    context={
        "customer_zip" : customer_zip
    }      
    return render(request,'employees/pickup_list.html', context)

@login_required
def saturday(request):
    logged_in_user=request.user
    logged_in_employee = Employee.objects.get(user=logged_in_user)
    Customer = apps.get_model('customers.Customer')
    employee_zip= logged_in_employee.zip_code
    customer_zip= Customer.objects.filter(zip_code = employee_zip).filter(weekly_pickup="Saturday")
    context={
        "customer_zip" : customer_zip
    }      
    return render(request,'employees/pickup_list.html', context)