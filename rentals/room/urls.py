from django.urls import path
from .import views
from .views import RoomTypeList
urlpatterns=[
    path('',views.index,name='index'),
    path('createroomtype',views.RoomTypeCreate,name='createroomtype'),
    path('roomtypes',views.roomtypes,name='roomtypes'),
    #path('getallroomtypes',views.getAllRooms,name='getroomtypes'),
    path('getroomtypes',RoomTypeList.as_view(),name='roomtypes')
]