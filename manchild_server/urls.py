from django.urls import path
from .views import (
    CollectionListCreateView, CollectionDetailView,
    CollectionItemListCreateView, CollectionItemDetailView
)

urlpatterns = [
    # Collections
    path("collections/", CollectionListCreateView.as_view(), name="collection-list"),
    path("collections/<int:pk>/", CollectionDetailView.as_view(), name="collection-detail"),

    # Collection Items
    path("collections/<int:collection_id>/items/", CollectionItemListCreateView.as_view(), name="item-list"),
    path("collections/<int:collection_id>/items/<int:pk>/", CollectionItemDetailView.as_view(), name="item-detail"),
]