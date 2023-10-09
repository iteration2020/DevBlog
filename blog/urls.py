from django.urls import path,include
from .views import BlogList,BlogDetailView,AboutPageView,LerningPageView,upload
from django.views.generic import ListView

urlpatterns = [
    path('post/<int:pk>/',BlogDetailView.as_view(),name='post_detail'),
    path('about/',AboutPageView.as_view(),name='about'),
    path('',BlogList.as_view(),name='home'),
    path('gtran/', include('gtranslate.urls')),
    # for user authorized dynamic translation
    path('gtran/', include('gtranslate.urls_auth')),
    path('Lerning/',LerningPageView.as_view(),name='Lerning'),
    path('upload', upload, name='upload')
]
