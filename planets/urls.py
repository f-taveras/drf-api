from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from planets import views



urlpatterns = [
    path("planets/", views.PlanetList.as_view(), name="planet-list"),
    path("planets/<int:pk>/", views.PlanetDetail.as_view(), name="planet-detail"),
    path(
        "planets/<int:pk>/highlight/", 
        views.PlanetHighlight.as_view(), 
        name="planet-highlight",),
    path("users/", views.UserList.as_view(), name="user-list"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
    path("", views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)