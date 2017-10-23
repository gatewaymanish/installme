"""suwebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import howtosetupview, landing, productlist
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^setup/(?P<id>\d+)/', howtosetupview, name='setup'),
    url(r'^$', landing, name='home'),
    url(r'^productlist/(?P<category>.+?)$',productlist, name='productlist' )
    ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# else:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



# if settings.DEBUG:
#     urlpatterns += urlpatterns('',
#              (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),
#          )
#
#     urlpatterns += urlpatterns('',
#             (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
#         )