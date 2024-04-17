from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from blog.views import hello_world, post_news_view, post_news_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello_world/', hello_world),
    path('blog/', post_news_view),
    path('blog/<int:id>/', post_news_detail_view),
    path('', include('it_forum.urls')),
    path('', include('parser.urls')),
    path('', include('product.urls')),
    path('', include('registration.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
