
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.homepage),
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('article/', include('articles.urls'))
    
]

urlpatterns += staticfiles_urlpatterns()
