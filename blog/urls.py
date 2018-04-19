from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^api/', views.post_data, name='post_data'),
    url(r'^church/', views.church_data, name='church_data'),
    url(r'^crime/', views.crime_data, name='crime_data'),
    url(r'^construction/', views.construction_data, name='construction_data'),
    url(r'^permit/', views.permit_data, name='permit_data'),
    url(r'^graffiti/', views.graffiti_data, name='graffiti_data'),
]