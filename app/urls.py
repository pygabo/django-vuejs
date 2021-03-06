
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from apps.homepage.views import (
   func_games,
   ClassHistoryTemplateView,
   log_game_view,
   func_get_users,
 )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^$', ClassHistoryTemplateView.as_view(), name='history'),
    url(r'^log$', log_game_view, name='log'),
    url(r'^homepage/games$', func_games, name="games"),
    url(r'^app/users$',func_get_users, name="users"),
]
