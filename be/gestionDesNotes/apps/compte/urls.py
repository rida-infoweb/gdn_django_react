from django.conf.urls import url, include

compte_urlpatterns = [
    url(r'^api/', include('djoser.urls')),
    url(r'^api/', include('djoser.urls.authtoken')),
]