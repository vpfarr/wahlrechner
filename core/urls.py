import os
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from core.settings import URL_PREFIX

urlpatterns = [
    path(f"{URL_PREFIX}", include("wahlrechner.urls")),
    path(f"{URL_PREFIX}admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Wahlrechner Admin"
admin.site.site_title = "Wahlrechner Admin"
admin.site.index_title = "Konfiguration"

handler404 = "wahlrechner.views.handler404"
handler500 = "wahlrechner.views.handler500"
