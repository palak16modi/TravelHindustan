from django.shortcuts import render
from django.db import connection
# Create your views here.

def events(request):
    cursor = connection.cursor()
    cursor.execute("SELECT name,place,details,MONTH(CURRENT_DATE()) AS month, url FROM event_fes where MONTH(month1) = MONTH(CURRENT_DATE()) or MONTH(month2) = MONTH(CURRENT_DATE())")
    data=cursor.fetchall()
    print(data)
    i=0
    a=[]
    b={}
    while(i<len(data)):
        temp={}
        temp['name']=data[i][0]
        temp['place']=data[i][1]
        temp['details']=data[i][2]

        temp['month']=data[i][3]
        temp['url']=data[i][4]

        if(data[i][3]==12) :
            temp['month']='December'
        elif(data[i][3]==11):
            temp['month']='November'
        elif(data[i][3]==10):
            temp['month']='October'
        elif(data[i][3]==9):
            temp['month']='September'
        elif(data[i][3]==8):
            temp['month']='August'
        elif(data[i][3]==7):
            temp['month']='July'
        elif(data[i][3]==6):
            temp['month']='June'
        elif(data[i][3]==5):
            temp['month']='May'
        elif(data[i][3]==4):
            temp['month']='April'
        elif(data[i][3]==3):
            temp['month']='March'
        elif(data[i][3]==2):
            temp['month']='February'
        elif(data[i][3]==1):
            temp['month']='January'
        a.append(temp)
        i+=1
    b['event_fes']=a
    return render(request,"events/events.html",b)
