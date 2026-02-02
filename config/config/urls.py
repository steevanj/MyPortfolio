from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('core.urls')),
]

# ✅ Admin available ONLY in development
if settings.DEBUG:
    urlpatterns += [
        path('Steve@123/', admin.site.urls),
    ]

# ✅ Serve media files in development
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
