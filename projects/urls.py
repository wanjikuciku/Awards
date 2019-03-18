from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[

    url(r'^$',views.index, name='index'),
    url(r'^profile/',views.profile, name='profile'),
    url(r'^new_project/',views.send_project, name='send_project'),
    url(r'^search/',views.search_project,name='search_project'),
    url(r'^project/(\d+)',views.project,name='project'),
    url(r'^api/profile/$',views.ProfileList.as_view(),name='profile_list'),
    url(r'^api/project/$', views.ProjectList.as_view()),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)





