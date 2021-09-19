from django.conf.urls import url
from django.urls import path
from django.views.static import serve

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  url(r'^best_executers$', views.best_executers, name='best_executers'),
                  url(r'^ganre$', views.ganre, name='ganre'),
                  url(r'^album$', views.album, name='album'),
                  url(r'^execute$', views.execute, name='execute'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
