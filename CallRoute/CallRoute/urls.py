"""
URL configuration for CallRoute project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import main.views as main_views
from django.conf.urls import i18n

handler404 = main_views.custom_404
urlpatterns = [
    path('admin/', admin.site.urls),
    path('selectlanguage/', main_views.selectlanguage, name='selectlanguage'),
    path('i18n/', include('django.conf.urls.i18n')),

    ]
urlpatterns += i18n.i18n_patterns(
    path('', include('main.urls')),
    path('news/', include('news.urls')),
    path('users/', include('users.urls')),
    path('calldetail/', include('calldetail.urls')),
    path('icmitems/', include('icmitems.urls')),
    path('dashboard/', include('dashboard.urls'))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #чтобы работали медиа файлы

if settings.DEBUG:
    import debug_toolbar
    urlpatterns=[
        path('__debug/__', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #чтобы работали статические файлы

#Измеяем название панели администратор
admin.site.site_header = "Панель администрирования CallRoute"
admin.site.index_title = "Администрирование CallRoute"