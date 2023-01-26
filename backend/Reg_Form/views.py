from curses.ascii import HT
from errno import errorcode
import re
from sqlite3 import Cursor
from unittest import result
from django.shortcuts import render
from django.http import HttpResponse
import Reg_Form
from Reg_Form.models import users
from django.db import connection
from django.contrib import messages
import razorpay
from django.views.decorators.csrf import csrf_exempt
import uuid
from datetime import datetime


# Create your views here.
def form(request):
    return render(request, 'index.html')


def technical(request):
    return render(request, 'technical.html')


def management(request):
    return render(request, 'management.html')


def design(request):
    return render(request, 'design.html')


def architecture(request):
    return render(request, 'architecture.html')


def food(request):
    return render(request, 'food.html')


def about(request):
    return render(request, 'about.html')

# def Contactus(request):
#     return render(request,'Contactus.html')


def saveform(request):
    if request.method == 'POST':
        global Fullname, email, College, PhoneNo
        Fullname = request.POST.get('Fullname')
        email = request.POST.get('email')
        College = request.POST.get('College')
        PhoneNo = request.POST.get('PhoneNo')
        event = request.POST.get('event')

        global en
        en = users(Fullname=Fullname, email=email,
                   College=College, PhoneNo=PhoneNo, event=event)
        # en.save()
        global total_cost
        total_cost = []
        global x
        x = event.split(",")
        for y in x:
            cursor = connection.cursor()
            sql_update_query = """SELECT cost from costs where event = %s"""
            data_tuple = (y,)
            cursor.execute(sql_update_query, data_tuple)
            result = cursor.fetchall()
            for cost in result:
                for cost1 in cost:
                    total_cost.append(cost1)
    print(sum(total_cost))
    # amount = sum(total_cost)
    result = int(sum(total_cost))
    if result != 0:
        amount = 100*(result)
        order_currency = 'INR'
        client = razorpay.Client(
            auth=("rzp_test_ASZsjsfB2r7y5C", "w8ZyJSQScX7q4x1wrURFK4yE"))
        payment = client.order.create(
            {'amount': amount, 'currency': 'INR',  'payment_capture': 1})

        context = {'amount': amount,
                   'result': result}
        return render(request, 'payment.html', context)
    else:
        for y in x:
            order_id = uuid.uuid1()
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            cursor = connection.cursor()
            cursor.execute('INSERT INTO reg_form_users (id , Fullname, email, College, PhoneNo , event , timestamp)'
                           'VALUES (%s ,%s, %s, %s, %s , %s , %s)',
                           (order_id, Fullname, email, College, PhoneNo, y, now),
                           )
        return HttpResponse("Registered Sucessfully")


def registration(request):
    return render(request, 'register.html')


@csrf_exempt
def success(request):
    # saveform.en.save()

    for y in x:
        # print(Fullname,email,PhoneNo,College, y)
        order_id = uuid.uuid1()
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        cursor = connection.cursor()
        cursor.execute('INSERT INTO reg_form_users (id , Fullname, email, College, PhoneNo , event , timestamp)'
                       'VALUES (%s ,%s, %s, %s, %s , %s , %s)',
                       (order_id, Fullname, email, College, PhoneNo, y, now),
                       )

    return render(request, 'success.html')
