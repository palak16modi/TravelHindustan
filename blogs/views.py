from django.shortcuts import render
from django.db import connection



# Create your views here.
def Blogs(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM blogs")
    data=cursor.fetchall()
    print(data)
    i=0
    a=[]
    b={}
    while(i<len(data)):
        temp={}
        temp['text1']=data[i][1]
        temp['location']=data[i][2]
        
        a.append(temp)
        i+=1
    b['blogs']=a
    return render(request,"blogs/blogs.html",b)



