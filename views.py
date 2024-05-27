from rest_framework import viewsets, mixins
from rest_framework.response import Response
from .models import Order, AttachedFile
from .serializers import OrderSerializer, OrderCreateSerializer

class OrderViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderCreateSerializer
        return OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)
