from . import views
from django.urls import path

urlpatterns = [
    path('userlogin/' , views.login , name='userlogin' ),
    path('adminlogin/' , views.adminlogin , name='adminlogin' ),
    path('adminpanel/' , views.adminpanel , name='adminpanel' ),
    path('adminbookshelf/' , views.adminbookshelf , name='adminbookshelf' ),
    path('adminpanel/book/<bookid>/' , views.bookchange , name='change' ),
    path('adminusermanagement/' , views.adminusermanagement , name='usermanagement' ),
    path('adminpanel/adminusermanagement/<userid>/' , views.adminuserchanger , name='userchanger' ),
    path('adminpanel/inbox' , views.inbox_handeling , name='inbox' ),
    path('borrow/' , views.borrow , name='borrow'),
    path('<userid>/' , views.userpanel , name = 'userpanel')
]
