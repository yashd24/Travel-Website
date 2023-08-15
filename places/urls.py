from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.add, name="add"),
    path("delete/<str:id>/", views.delete, name='delete'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
