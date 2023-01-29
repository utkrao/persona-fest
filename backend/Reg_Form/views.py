from curses.ascii import HT
from errno import errorcode
import re
from sqlite3 import Cursor
from unittest import result
from django.shortcuts import render
from django.http import HttpResponse
import Reg_Form
from Reg_Form.models import users,admin_data
from django.db import connection
from django.contrib import messages
import razorpay
from django.views.decorators.csrf import csrf_exempt
import uuid
from datetime import datetime
import django_tables2 as tables



# Create your views here.
def form(request):
    return render (request,'index.html')

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
    return render(request,'about.html')
    
# def Contactus(request):
#     return render(request,'Contactus.html')

def saveform(request):
    if request.method == 'POST':
        global Fullname , email , College , PhoneNo
        Fullname = request.POST.get('Fullname')
        email = request.POST.get('email')
        College = request.POST.get('College')
        PhoneNo = request.POST.get('PhoneNo')
        event = request.POST.get('event')
        

        global en
        en = users(Fullname=Fullname,email=email,College = College , PhoneNo = PhoneNo , event = event )
        # en.save()
        global total_cost
        global cost_events

        global uncost_events
        global uncostreceipt

        total_cost =[]
        cost_events = []

        uncost_events=[]
        uncostreceipt = []

        global x
        x = event.split(",")
        for y in x :
            cursor = connection.cursor()
            sql_update_query = """SELECT cost from costs where event = %s"""
            data_tuple = (y,)
            cursor.execute(sql_update_query, data_tuple)
            result = cursor.fetchall()
            for cost in result:
                for cost1 in cost:
                    if cost1 == 0:
                        uncost_events.append(y)
                        order_id = uuid.uuid1()
                        now = datetime.now()
                        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                        cursor = connection.cursor()
                        cursor.execute(
                            'INSERT INTO reg_form_users (id , Fullname, email, College, PhoneNo , event , timestamp)'
                            'VALUES (%s ,%s, %s, %s, %s , %s , %s )',
                            (order_id, Fullname, email, College, PhoneNo, y, now),
                            )

                        bill = y + ' - ' + str(order_id)
                        uncostreceipt.append(bill)

                    else:
                        total_cost.append(cost1)
                        cost_events.append(y)

    else:
        return HttpResponse("Access Denied")
    result1 = int(sum(total_cost))

    if result1 != 0:
        amount = (result1)
        context = {'amount': amount,
                   'result': result1}
        return render(request, 'total_payable.html', context)

    else:
        context = {
            'Fullname': Fullname,
            'email': email,
            'PhoneNo': PhoneNo,
            'receipt': uncostreceipt,
            'College': College
        }
        return render(request, 'checkout.html', context)



def registration(request):
    return render(request, 'register.html')


@csrf_exempt
def success(request):
    # saveform.en.save() 
    receipt1 = []
    bill = []
    if request.method == "POST":
        Txn_id = request.POST.get('Txn_id')

    else:
        return HttpResponse("404 Not Found")

        # en = users(Txn_id = Txn_id)
        
    for y in cost_events :
            # print(Fullname,email,PhoneNo,College, y)
            order_id = uuid.uuid1()
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            cursor = connection.cursor()
            cursor.execute('INSERT INTO reg_form_users (id , Fullname, email, College, PhoneNo , event , timestamp , Txn_id)'
                'VALUES (%s ,%s, %s, %s, %s , %s , %s , %s)',
                ( order_id , Fullname, email, College,PhoneNo , y, now ,Txn_id),
            )
            es = admin_data(Fullname = Fullname , email = email , College = College , PhoneNo = PhoneNo , timestamp = now , event = y , Txn_id = Txn_id)
            es.save()

            bill = y + ' - ' + str(order_id)
            receipt1.append(bill)

    if len(uncostreceipt) == 0:
        context = {
            'Fullname': Fullname,
            'email': email,
            'PhoneNo': PhoneNo,
            'receipt': receipt1,
            'College': College
        }
        return render(request, 'checkout.html', context)
    else:
        final_receipt = receipt1 + uncostreceipt
        context = {
             'Fullname': Fullname,
             'email': email,
             'PhoneNo': PhoneNo,
             'receipt': final_receipt,
             'College': College
        }
        return render(request,'checkout.html',context)

