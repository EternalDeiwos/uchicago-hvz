from django.conf.urls import patterns, include, url
from uchicagohvz.game.views import *
from uchicagohvz.game.api_views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uchicagohvz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', ListGames.as_view(), name='game|list'),
    url(r'^game/(?P<pk>[0-9]+)/$', ShowGame.as_view(), name='game|show'),
    url(r'^game/(?P<pk>[0-9]+)/leaderboard/$', Leaderboard.as_view(), name='game|leaderboard'),
    url(r'^game/(?P<pk>[0-9]+)/register/$', RegisterForGame.as_view(), name='game|register'),
    url(r'^game/(?P<pk>[0-9]+)/bite/$', EnterBiteCode.as_view(), name='game|bite'),
    url(r'^game/sms-code/$', SubmitCodeSMS.as_view(), name='game|smscode'),
    url(r'^game/(?P<pk>[0-9]+)/code/$', SubmitAwardCode.as_view(), name='game|code'),
    url(r'^game/(?P<pk>[0-9]+)/data/kills/$', KillFeed.as_view(), name='game|data|kills'),
    url(r'^game/(?P<pk>[0-9]+)/data/humans-per-hour/$', HumansPerHour.as_view(), name='game|data|hph'),
    url(r'^game/(?P<pk>[0-9]+)/data/kills-by-tod/$', KillsByTimeOfDay.as_view(), name='game|data|kbtod'),
    url(r'^game/(?P<pk>[0-9]+)/data/humans-by-major/$', HumansByMajor.as_view(), name='game|data|hbm'),
    url(r'^game/(?P<pk>[0-9]+)/data/zombies-by-major/$', ZombiesByMajor.as_view(), name='game|data|zbm'),
    url(r'^player/(?P<pk>[0-9]+)/$', ShowPlayer.as_view(), name='player|show'),
    url(r'^player/(?P<pk>[0-9]+)/data/kills/$', PlayerKillFeed.as_view(), name='player|data|kills'),
    url(r'^kill/(?P<pk>[0-9]+)/geotag/$', AddKillGeotag.as_view(), name='kill|geotag'),
)
