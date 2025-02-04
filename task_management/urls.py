
from django.contrib import admin
from django.urls import path,include
from tasks.views import sifat_page
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/',include('tasks.urls')),
    path('',sifat_page)
]+ debug_toolbar_urls()
