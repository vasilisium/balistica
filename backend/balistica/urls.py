from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    # path('', include(router.urls)),
    path ('api/v1/', include('api.urls')),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]

urlpatterns += i18n_patterns (
    # path('', admin.site.urls),
    path('admin/', admin.site.urls),
    prefix_default_language=False
)
