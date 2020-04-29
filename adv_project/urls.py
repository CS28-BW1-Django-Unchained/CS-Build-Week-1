from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include

from rest_framework import routers
from rest_framework.authtoken import views
router = routers.DefaultRouter()
'''
{% if request.user.is_superuser %}
  <a href="{% url 'admin:index' %}">Django Admin</a>
{% endif %}
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/adv/', include('adventure.urls')),
    path('api-token-auth/', views.obtain_auth_token)
]
