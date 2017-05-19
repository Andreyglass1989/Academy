from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
#import staff.urls
from login_user.views import login, logout, register

#app_name = 'quadratic'
urlpatterns = [
    url(r'^login/', login, name="login"),
    url(r'^logout/', logout, name="logout"),
    url(r'^register/', register, name="register"),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)