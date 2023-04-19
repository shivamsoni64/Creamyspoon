from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Creamy Spoon Admin"
admin.site.site_title = "Creamy Spoon Admin Portal"
admin.site.index_title = "Welcome to Creamy Spoon"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),
    path('', include('app2.urls')),

]
 

urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)