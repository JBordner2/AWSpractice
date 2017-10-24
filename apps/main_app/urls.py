from django.conf.urls import url
from . import views

def test(request):
        print """


        function is firing


        """

urlpatterns = [
    url(r'^petApp$', views.index),
    url(r'^addPet$', views.addPet),
    url(r'^createPet$', views.createPet),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^show/(?P<id>\d+)$', views.show),

]