from tkinter import _Cursor
from django.shortcuts import render
import mysql.connector as sql
em=''
pwd=''

# Create your views here.
def loginupaction(request):
    global em,pwd
    if request.method=='POST':
        m=sql.connect(host='localhost',user='root',passwd=' ',database='')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.item():
            if key=="email":
                em=value
            if key=="password":
                pwd==value
        c="select *  from users where email='{} and password='{}'('()','{}','{}','{}','{}')".format(em,pwd)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,'welcome.html')
    return render(request,'signup_page.html')