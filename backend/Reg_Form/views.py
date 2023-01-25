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

# Create your views here.
def form(request):
    return render (request,'index.html')



def saveform(request):
    if request.method == 'POST':
        Fullname = request.POST.get('Fullname')
        email = request.POST.get('email')
        College = request.POST.get('College')
        PhoneNo = request.POST.get('PhoneNo')
        event = request.POST.get('event')

        global en
        en = users(Fullname=Fullname,email=email,College = College , PhoneNo = PhoneNo , event = event )
        # en.save()
        global total_cost
        total_cost =[]
        global x
        x = event.split(",")
        for y in x :
            cursor = connection.cursor()
            # cursor.execute('INSERT INTO reg_form_users (Fullname, email, College, PhoneNo , event )'
            #     'VALUES (%s, %s, %s, %s,%s)',
            #     (Fullname, email, College,PhoneNo , y ),
            # )
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
    amount = 100*(result)
    order_currency = 'INR'
    client = razorpay.Client(auth=("rzp_test_ASZsjsfB2r7y5C", "w8ZyJSQScX7q4x1wrURFK4yE"))
    payment = client.order.create({'amount': amount, 'currency' : 'INR',  'payment_capture' : 1})
    context = {'amount' : amount,}
    return render(request,'payment.html',context)



def registration(request):
    return render(request, 'register.html')


@csrf_exempt
def success(request):
    # saveform.en.save() 
    print(x)
    en.save()
    return render(request,'success.html')
