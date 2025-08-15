from django.urls import path
from .views import HomePageView,AboutPageView,ContactView,BlogDetailPageView,BlogPageView

urlpatterns = [
    path('',HomePageView.as_view(),name='home-page'),
    path('about/',AboutPageView.as_view(),name='about-page'),
    path('contact/',ContactView.as_view(),name='contact-page'),
    path('blog/',BlogPageView.as_view(),name='blog-page'),
    path('blog/1',BlogDetailPageView.as_view(),name='blog-detail-page'),
]
