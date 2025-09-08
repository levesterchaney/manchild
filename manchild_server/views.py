from rest_framework import generics, permissions
from .models import Collection, CollectionItem
from .serializers import CollectionSerializer, CollectionItemSerializer

# Collection Views
class CollectionListCreateView(generics.ListCreateAPIView):
    serializer_class = CollectionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.collections.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CollectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CollectionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.collections.all()


# Collection Item Views
class CollectionItemListCreateView(generics.ListCreateAPIView):
    serializer_class = CollectionItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CollectionItem.objects.filter(collection__user=self.request.user,
                                             collection_id=self.kwargs["collection_id"])

    def perform_create(self, serializer):
        serializer.save(collection_id=self.kwargs["collection_id"])

class CollectionItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CollectionItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CollectionItem.objects.filter(collection__user=self.request.user)
