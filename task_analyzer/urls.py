from django.contrib import admin
from django.urls import path, include  # 'include' add karna mat bhoolna

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/', include('tasks.urls')),
]