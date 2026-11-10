"""
URL configuration for Recipe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from reviews import views

urlpatterns = [
    path('review/',views.Review.as_view()),
    path('rr/<int:pk>/', views.ReadReview.as_view()),
    path('update/<int:pk>/',views.UpdateReview.as_view()),
    # path('partial/<int:pk>/',views.PartialUpdateReview.as_view()),
    path('delete/<int:pk>/',views.DeleteReview.as_view()),
]
