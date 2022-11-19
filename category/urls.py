from django.urls import path

from category import views

urlpatterns = [
   path("", views.CategoryListView.as_view(), name="categories"),
   path('create/', views.CategoryCreateView.as_view(), name='create_category'),
   path("<int:pk>/", views.CategoryDetailView.as_view(), name="category_detail"),
]
