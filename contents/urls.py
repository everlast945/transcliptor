from django.urls import path, include

from contents.views import ContentView

app_name = 'contents'

urlpatterns = [
    path('<int:pk>/', ContentView.as_view(), name='read-update-delete'),

    # post-apps
    path('category/', include('contents.category.urls')),
]
