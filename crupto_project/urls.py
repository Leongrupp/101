from django.urls import path, include
from wagtail import urls as wagtail_urls

urlpatterns = [
    path('admin/', include('wagtail.admin.urls')),
    path('', include(wagtail_urls)),
]
