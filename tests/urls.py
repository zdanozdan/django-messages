from django.conf.urls import include, url

urlpatterns = [
    url(r'^messages/', include('django_messages.urls')),
]
