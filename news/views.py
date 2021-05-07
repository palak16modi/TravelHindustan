from django.shortcuts import render
from django.db import connection

# Create your views here.
def News(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM news")
    data=cursor.fetchall()
    print(data)
    i=0
    a=[]
    b={}
    while(i<len(data)):
        temp={}
        temp['news_headline']=data[i][1]
        temp['city']=data[i][2]
        temp['link']=data[i][3]
        
        a.append(temp)
        i+=1
    b['news']=a
    return render(request,"news/news.html",b)