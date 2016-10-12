from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'itweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'itweb.views.home', name='home'),
    url(r'^add_it/$', 'itweb.views.add_it', name='add_it'),

    url(r'^interface/create/$', 'itweb.views.create_it', name='create_it'),
    url(r'^interface/create/it_details', 'itweb.views.it_details', name='it_details'),

    url(r'^interface/manage/$', 'itweb.views.manage_it', name='manage_it'),
]

