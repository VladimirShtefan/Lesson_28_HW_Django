from django.urls import path

from user import views

urlpatterns = [
   path('', views.UserListView.as_view(), name='users'),
   path('<int:pk>/', views.UserDetailView.as_view(), name='detail_user'),
   path('create/', views.UserCreateView.as_view(), name='create_user'),
]
