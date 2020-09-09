from django.urls import path, include
from rest_framework import routers
from . import views
from .views import CustomObtainAuthToken


router = routers.DefaultRouter()
router.register('answer', views.AnswerViewSet)
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('login/', views.UserLoginApiView.as_view()),
    #path('login/', CustomObtainAuthToken.as_view()),
    #path('usertodos/', views.TodosList.as_view())
]
