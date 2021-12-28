
from django.contrib import admin
from django.urls import path
from zaap.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include
urlpatterns = [
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('admin/', admin.site.urls),
    path('',HOME,name= 'home'),
    path('menu',MENU,name= 'menu'),
    path('about',ABOUT,name= 'about'),
    path('book_table',BOOK_TABLE,name= 'book_table'),
    path('Logout/',LOGOUT,name='Logout'),
    path('Login/',LOGIN,name='Login'),
    #####       admin pannel   ##########
    path('admin_index',ADMIN_INDEX,name= 'admin_index'),
    path('menu_delete/<int:del_id>/', MENU_DELETE, name='menu_delete'),
    path('admin_youtube',ADMIN_YOUTUBE, name='admin_youtube'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
