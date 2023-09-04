from django.urls import path
from applications.package import views

urlpatterns = [
    path('', views.PackageListCreateAPIView.as_view(), name='package'),
    path('<int:pk>/', views.PackageDetailAPIView.as_view()),
    path('type/', views.PackageTypeAPIView.as_view()),
]
