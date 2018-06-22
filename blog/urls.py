from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.menu, name='menu'),
    url(r'^blog/', views.post_list, name='post_list'),
    url(r'^bird_api/', views.bird_api, name='bird_api'),	# returns data in json format.
    url(r'^bird/', views.bird_data, name='bird_data'),		# returns data in a file format.
    url(r'^graffiti/', views.graffiti_data, name='graffiti_data'),
    url(r'^church/', views.church_data, name='church_data'),
    url(r'^crime/', views.crime_data, name='crime_data'),
    url(r'^construction/', views.construction_data, name='construction_data'),
    url(r'^permit/', views.permit_data, name='permit_data'),
    url(r'^move/', views.move_data, name='move_data'),
    url(r'^tree/', views.tree_data, name='tree_data'),
    url(r'^map/', views.mymap, name='mymap'),
]