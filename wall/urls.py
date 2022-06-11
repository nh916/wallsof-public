from django.contrib import admin
from django.urls import path, include

from wallOf import url as wallOfUrls
# from home import url as homeURLS
from home import views as home_Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(wallOfUrls)),
    # path('wallof/', include(homeURLS)),

    path('about/', home_Views.about, name='about'),
    path('robot/', home_Views.robot, name='robot'),
    path('emil/', home_Views.emil),
]
