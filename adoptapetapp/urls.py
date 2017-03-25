from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    url(r'^accounts/login/$', views.login),
    url(r'^$', views.home, name="home"),
    url(r'^details/(?P<petname>.*)/$', views.details, name="viewDetailsOne"),
    url(r'^signUp',views.signUp,name="signUp"),
    url(r'^createMessage', views.createMessage, name="createMessage"),
    url(r'^dialogues/(?P<petname>.*)/$', views.dialogues, name="dialogues"),
    url(r'^editProfile', views.editProfile, name="editProfile"),
    url(r'^Profile', views.profile, name="editProfile"),
    url(r'^logout', views.logout_view, name="logout"),
    url(r'^registerusr', views.registerUsr, name="register"),
    url(r'^insertAd', views.insertAd, name="register"),
    url(r'^mypets', views.mypets, name="register"),
    url(r'^editPet/(?P<editingPet>.*)/$', views.editPet, name="register"),
    url(r'^comments/(?P<petname>.*)/$', views.comments),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
