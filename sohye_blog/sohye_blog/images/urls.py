from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^feed/$',
        views.Feed.as_view(),
        name='feeds'
    ),
]
