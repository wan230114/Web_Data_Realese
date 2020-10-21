"""urlconf for the layout application"""

from django.conf.urls import url
from layout import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^Release_Data/.+', views.check),
    url(r'^downzip/$', views.zipfile_down)
    # url(r'^$', views.index),
    # url(r'^folder/(?P<url>.+)/$', views.show_folder),
]
