from django.urls import path, include
# For images
from django.conf.urls.static import static
from django.conf import settings
#
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:pk>/page=<int:p>/', views.book, name='book'),
    path('about/', views.about, name='about')
]

# For images
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)