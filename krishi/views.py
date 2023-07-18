from django.shortcuts import render
from .models import *
# Create your views here.
 
from django.http import HttpResponse

def home(request):
    return render(request,"index.html")

def show(request,id):
    sell1=selling.objects.filter(product=id).all()
    return render(request,"show.html",{"sell1":sell1,"id":id})

def sell(request):
    if request.method=="POST":
        img=request.FILES['filename']
        product=request.POST['product']
        productdet=request.POST['productdet']
        quantity=request.POST['quantity']
        price=request.POST['price']
        phone=request.POST['Phone']
        email=request.POST['email']
        username=request.POST['username']
        seller1=selling(username=username,img=img,product=product,productdet=productdet,quantity=quantity,price=price,email=email,phone=phone)
        seller1.save()
        return render(request,"sell.html")

    return render(request,"sell.html")

def about(request):
    return render(request,"about.html")
def product(request):
    # item1=item()
    # item1.name="vegetable"
    # item1.img="product1.jpg"
    # item1.show=True
    # item2=item()
    # item2.name="cereals"
    # item2.img="product2.jpg"
    # item2.show=True
    # item3=item()
    # item3.name="fruits"
    # item3.img="product3.jpg"
    # item3.show=True
    # item4=item()
    # item4.name="sunflower"
    # item4.img="product4.jpg"
    # item4.show=True
    # item5=item()
    # item5.name="livestock"
    # item5.img="product5.jpg"
    # item5.show=True
    items=item.objects.all()

    return render(request,"products.html",{"items":items})
def blog(request):
    return render(request,"blog.html")
def login(request):
    return render(request,"login.html")
def contact(request):
    if request.method=="POST":
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]
        Email=request.POST["mail"]
        Phone_Number=request.POST["phone"]
        address=request.POST["local address"]
        state=request.POST["state"]
        postal=request.POST["postal code"]
        contact=counsel(first_name=firstname,email=Email,phone=Phone_Number,local_address=address,state=state,postal_code=postal,last_name=lastname)
        contact.save()
        return render(request,"contact.html")
    return render(request,"contact.html")
def index(request):
    return render(request,"index.html")

def feedback1(request):
    Full_Name=request.POST["Full Name"]
    Email=request.POST["Email"]
    Phone_Number=request.POST["Phone Number"]
    message=request.POST["message"]
    page=request.POST["page"]
    contact=feedback(first_name=Full_Name,email=Email,phone=Phone_Number,message=message)
    contact.save()
    print(page)
    return render(request,page+".html")

def news(request):
    Email=request.POST["Email"]
    page=request.POST["page"]
    email1=newsletter(email=Email)
    email1.save()
    return render(request,page+".html")

def counselling(request):
    firstname=request.POST["firstname"]
    lastname=request.POST["lastname"]
    Email=request.POST["mail"]
    Phone_Number=request.POST["Phone"]
    address=request.POST["local address"]
    state=request.POST["state"]
    postal=request.POST["postal code"]
    contact=feedback(first_name=firstname,email=Email,phone=Phone_Number,local_address=address,state=state,postal_code=postal,last_name=lastname)
    contact.save()
    print(page)
    return render(request,"contact.html")
