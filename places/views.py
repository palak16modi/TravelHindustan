from django.shortcuts import render
from django.db import connection

# Create your views here.
def Agra(request):
    return render(request,"places/agra_connecting_pages.html",{})

def Hotels_Agra(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM hotels where locality=%s",['Agra'])
    data=cursor.fetchall()
    print(data)
    i=0
    a=[]
    b={}
    while(i<len(data)):
        temp={}
        temp['name']=data[i][0]
        temp['image']=data[i][1]
        temp['url']=data[i][2]
        temp['locality']=data[i][3]
        temp['reviews']=data[i][4]
        temp['price_per_night']=data[i][5]
        temp['booking_provider']=data[i][6]
        temp['no_of_deals']=data[i][7]
        temp['features']=data[i][8]
        a.append(temp)
        i+=1
    b['hotels']=a
    return render(request,"places/agra_hotels.html",b)


def Jaipur(request):
    return render(request,"places/jaipur_connecting_pages.html",{})

def Hotels_Jaipur(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM hotels where locality=%s",['Jaipur'])
    data=cursor.fetchall()
    print(data)
    i=0
    a=[]
    b={}
    while(i<len(data)):
        temp={}
        temp['name']=data[i][0]
        temp['image']=data[i][1]
        temp['url']=data[i][2]
        temp['locality']=data[i][3]
        temp['reviews']=data[i][4]
        temp['price_per_night']=data[i][5]
        temp['booking_provider']=data[i][6]
        temp['no_of_deals']=data[i][7]
        temp['features']=data[i][8]
        a.append(temp)
        i+=1
    b['hotels']=a
    return render(request,"places/jaipur_hotels.html",b)


def Delhi(request):
    return render(request,"places/delhi_connecting_page.html",{})

def Hotels_Delhi(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM hotels where locality=%s",['Delhi'])
    data=cursor.fetchall()
    print(data)
    i=0
    a=[]
    b={}
    while(i<len(data)):
        temp={}
        temp['name']=data[i][0]
        temp['image']=data[i][1]
        temp['url']=data[i][2]
        temp['locality']=data[i][3]
        temp['reviews']=data[i][4]
        temp['price_per_night']=data[i][5]
        temp['booking_provider']=data[i][6]
        temp['no_of_deals']=data[i][7]
        temp['features']=data[i][8]
        a.append(temp)
        i+=1
    b['hotels']=a
    return render(request,"places/delhi_hotels.html",b)


def Shimla(request):
    return render(request,"places/shimla_connecting_page.html",{})

def Hotels_Shimla(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM hotels where locality=%s",['Shimla'])
    data=cursor.fetchall()
    print(data)
    i=0
    a=[]
    b={}
    while(i<len(data)):
        temp={}
        temp['name']=data[i][0]
        temp['image']=data[i][1]
        temp['url']=data[i][2]
        temp['locality']=data[i][3]
        temp['reviews']=data[i][4]
        temp['price_per_night']=data[i][5]
        temp['booking_provider']=data[i][6]
        temp['no_of_deals']=data[i][7]
        temp['features']=data[i][8]
        a.append(temp)
        i+=1
    b['hotels']=a
    return render(request,"places/shimla_hotels.html",b)


def Manali(request):
    return render(request,"places/MANALI_connecting_page.html",{})

def Hotels_Manali(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM hotels where locality=%s",['Manali'])
    data=cursor.fetchall()
    print(data)
    i=0
    a=[]
    b={}
    while(i<len(data)):
        temp={}
        temp['name']=data[i][0]
        temp['image']=data[i][1]
        temp['url']=data[i][2]
        temp['locality']=data[i][3]
        temp['reviews']=data[i][4]
        temp['price_per_night']=data[i][5]
        temp['booking_provider']=data[i][6]
        temp['no_of_deals']=data[i][7]
        temp['features']=data[i][8]
        a.append(temp)
        i+=1
    b['hotels']=a
    return render(request,"places/manali_hotels.html",b)


def Gangtok(request):
    return render(request,"places/gangtok_connecting_page.html",{})

def Hotels_Gangtok(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM hotels where locality=%s",['Gangtok'])
    data=cursor.fetchall()
    print(data)
    i=0
    a=[]
    b={}
    while(i<len(data)):
        temp={}
        temp['name']=data[i][0]
        temp['image']=data[i][1]
        temp['url']=data[i][2]
        temp['locality']=data[i][3]
        temp['reviews']=data[i][4]
        temp['price_per_night']=data[i][5]
        temp['booking_provider']=data[i][6]
        temp['no_of_deals']=data[i][7]
        temp['features']=data[i][8]
        a.append(temp)
        i+=1
    b['hotels']=a
    return render(request,"places/gangtok_hotels.html",b)


def Kerela(request):
    return render(request,"places/kerela_connecting_page.html",{})

def Hotels_Kerela(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM hotels where locality=%s",['Kerela'])
    data=cursor.fetchall()
    print(data)
    i=0
    a=[]
    b={}
    while(i<len(data)):
        temp={}
        temp['name']=data[i][0]
        temp['image']=data[i][1]
        temp['url']=data[i][2]
        temp['locality']=data[i][3]
        temp['reviews']=data[i][4]
        temp['price_per_night']=data[i][5]
        temp['booking_provider']=data[i][6]
        temp['no_of_deals']=data[i][7]
        temp['features']=data[i][8]
        a.append(temp)
        i+=1
    b['hotels']=a
    return render(request,"places/kerela_hotels.html",b)


def Kolkata(request):
    return render(request,"places/westbengal_connecting_page.html",{})

def Hotels_Kolkata(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM hotels where locality=%s",['Kolkata'])
    data=cursor.fetchall()
    print(data)
    i=0
    a=[]
    b={}
    while(i<len(data)):
        temp={}
        temp['name']=data[i][0]
        temp['image']=data[i][1]
        temp['url']=data[i][2]
        temp['locality']=data[i][3]
        temp['reviews']=data[i][4]
        temp['price_per_night']=data[i][5]
        temp['booking_provider']=data[i][6]
        temp['no_of_deals']=data[i][7]
        temp['features']=data[i][8]
        a.append(temp)
        i+=1
    b['hotels']=a
    return render(request,"places/kolkata_hotels.html",b)



def Goa(request):
    return render(request,"places/goa_connecting_page.html",{})

def Hotels_Goa(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM hotels where locality=%s",['Goa'])
    data=cursor.fetchall()
    print(data)
    i=0
    a=[]
    b={}
    while(i<len(data)):
        temp={}
        temp['name']=data[i][0]
        temp['image']=data[i][1]
        temp['url']=data[i][2]
        temp['locality']=data[i][3]
        temp['reviews']=data[i][4]
        temp['price_per_night']=data[i][5]
        temp['booking_provider']=data[i][6]
        temp['no_of_deals']=data[i][7]
        temp['features']=data[i][8]
        a.append(temp)
        i+=1
    b['hotels']=a
    return render(request,"places/goa_hotels.html",b)

def Mumbai(request):
    return render(request,"places/mumbai_connecting_pages.html",{})

def Hotels_Mumbai(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM hotels where locality=%s",['Mumbai'])
    data=cursor.fetchall()
    print(data)
    i=0
    a=[]
    b={}
    while(i<len(data)):
        temp={}
        temp['name']=data[i][0]
        temp['image']=data[i][1]
        temp['url']=data[i][2]
        temp['locality']=data[i][3]
        temp['reviews']=data[i][4]
        temp['price_per_night']=data[i][5]
        temp['booking_provider']=data[i][6]
        temp['no_of_deals']=data[i][7]
        temp['features']=data[i][8]
        a.append(temp)
        i+=1
    b['hotels']=a
    return render(request,"places/mumbai_hotels.html",b)

