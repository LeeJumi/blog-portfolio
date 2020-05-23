"""firstsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
import hi.views
import two.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hi.views.home, name='home'),
    path('hi/<int:hi_id>',hi.views.detail, name="detail"),
    path('portfolio/', two.views.portfolio, name='portfolio'),
    path('hi/new/', hiapp.views.new, name='new'),
    path('hi/create', hiapp.views.new, name='create'), path('two/portfolio', two.views.portfoilo, name="portfolio"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

