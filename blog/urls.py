from django.urls import path,include
from .views import BlogList,BlogDetailView,AboutPageView
from django.views.generic import ListView

urlpatterns = [
    path('post/<int:pk>/',BlogDetailView.as_view(),name='post_detail'),
    path('about/',AboutPageView.as_view(),name='about'),
    path('',BlogList.as_view(),name='home'),
    path('gtran/', include('gtranslate.urls')),
    # for user authorized dynamic translation
    path('gtran/', include('gtranslate.urls_auth')),
]
