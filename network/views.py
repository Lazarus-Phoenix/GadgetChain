from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Network
from .serializers import NetworkSerializer, NetworkCreateUpdateSerializer
from .filters import NetworkFilter


class IsActiveUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_active


class NetworkViewSet(viewsets.ModelViewSet):
    queryset = Network.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NetworkFilter
    permission_classes = [IsActiveUser]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return NetworkCreateUpdateSerializer
        return NetworkSerializer