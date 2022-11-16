from django.conf.urls.static import static
from django.urls import path

from ad import views
from django.conf import settings

urlpatterns = [
    path('', views.AdListView.as_view(), name='ads'),
    path('create/', views.AdCreateView.as_view(), name='create_ad'),
    path('<int:pk>/', views.AdDetailView.as_view(), name='detail_ads'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
