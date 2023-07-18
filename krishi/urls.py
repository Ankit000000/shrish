from django.urls import path
from . import views

urlpatterns = [
        path("", views.home ,name='home'),
        path("products.html",views.product,name="product"),
        path("about.html",views.about,name="about"),
        path("blog.html",views.blog,name="blog"),
        path("contact.html",views.contact,name="contact"),
        path("contact",views.contact,name="contact"),
        path("index.html",views.index,name="index"),
        path("feedback1",views.feedback1,name="feedback1"),
        path("news",views.news,name="news"),
        path("sell.html",views.sell,name="sell"),
        path("sell",views.sell,name="sell"),
        path("show/<str:id>",views.show,name="show"),
]

