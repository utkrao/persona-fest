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

# Create your views here.
def form(request):
    return render (request,'index.html')



def saveform(request):
    if request.method == 'POST':
        Fullname = request.POST.get('Fullname')
        email = request.POST.get('email')
        College = request.POST.get('College')
        PhoneNo = request.POST.get('PhoneNo')
        en = users(Fullname=Fullname,email=email,College = College , PhoneNo = PhoneNo ,  )
        en.save()
        return render(request,'register.html')

        # cursor = connection.cursor()
        # sql_checkemail_query = """SELECT PhoneNo from persona_users where PhoneNo = %s """
        # data_tuple1 = (PhoneNo,)
        # cursor.execute(sql_checkemail_query, data_tuple1)
        # result = cursor.fetchall()
        # if len(result) == 0:
        #     messages.success(request,"Signup sucessful")
        #     en.save()
        #     return render(request,'login.html')
        # else:   
        #     messages.error(request,"This Phone number is already taken please use a different email")
        #     return render(request,'form.html')

def registration(request):
    return render(request, 'register.html')