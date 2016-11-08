from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from views import ProjectsView

from django.contrib import admin

urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="mybase.html"), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),


    url(r"^projects/(?P<project_id>[0-9]{1,11})/interface", ProjectsView.as_view(), name="test"),
    # url(r"^projects/(?P<project_id>[0-9]{1,11})/interface", "interface_platform.views.get_projects", name="test"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
