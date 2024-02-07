
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name='index'),
    # path('details',views.details,name='details')
    path('delete/<int:taskid>/', views.delete,name='delete'),
    path('update/<int:taskid>/', views.update,name='update'),
    path('cbvhome/', views.Todolistview.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/', views.TodoDetailview.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.TodoUpdateview.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TodoDeleteview.as_view(), name='cbvdelete'),

]
