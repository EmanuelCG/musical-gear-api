"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_views = get_schema_view(
    openapi.Info(
        title="Intrument Shop API",
        default_version="v1",
        description="Documentation of the Instrument Shop API",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/items/', include('items.urls')),
    path('swagger/', schema_views.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_views.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/v1/auth/',  include('accounts.urls')),
    path('api/v1/customers/',  include('customers.urls')),
]
