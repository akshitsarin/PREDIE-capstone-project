from django.contrib import admin
from django.urls import path, include

from predictor.views import welcome_view
from register.views import register

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include("django.contrib.auth.urls")),
  path('', welcome_view),
  path('register/', register, name='register'),
]