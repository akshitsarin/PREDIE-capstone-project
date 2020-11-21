from django.contrib import admin
from django.urls import path, include

from predictor.views import welcome_view, about_view, contact_view, team_view, predict_view, result_view
from register.views import register

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include("django.contrib.auth.urls")),
  path('', welcome_view),
  path('register/', register, name='register'),
  path('team/', team_view),
  path('about/', about_view),
  path('contact/', contact_view),
  path('predict/', predict_view),
  path('result/', result_view)
]