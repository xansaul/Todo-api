

from django.urls import path
from .views import UserView
from .CustomToken import CustomTokenResponse

urlpatterns = [ 
  path('',UserView.as_view()),
  path('<int:id>',UserView.as_view()),
  path('signin',CustomTokenResponse.as_view()),
]