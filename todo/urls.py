from django.urls import path
from .  import views 
urlpatterns = [
    path('',views.index,name='index'),
    path('addtodo',views.addtodo,name='addtodo'),
    path('complete/<Todo_id>',views.completetodo,name='complete'),
    path('deletecompleted',views.deletecompleted,name='deletecompleted'),
    path('deleteall',views.deleteall,name='deleteall'),
]
