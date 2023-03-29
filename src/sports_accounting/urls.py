"""sports_accounting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views

from main import urls as main_urls
from base_app import urls as base_app_urls

from base_app import api_urls as api_base_app_urls
from cash_module import api_urls as cash_module_urls
from member_module import api_urls as member_module_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    # API (rest_framework)
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(api_base_app_urls)),
    path('api/', include(cash_module_urls)),
    path('api/', include(member_module_urls)),
    # "Normal" views
    path('', include(main_urls)),
    path('mt940/', include(base_app_urls)),
]

# In production, serve static files with a web server like Nginx or Apache
# The following approach is only for development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
