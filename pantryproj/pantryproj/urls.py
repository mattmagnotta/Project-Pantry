from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pantryapp.urls')),
    path('users/', include('userapp.urls'))

]
