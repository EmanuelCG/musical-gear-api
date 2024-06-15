from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import OrderStatus, CustomerOrder
from .serializers import CustomerOrderSerializer, OrderStatusSerializer

class OrderStatusViewSet(viewsets.ModelViewSet):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer

class CustomerOrderViewSet(viewsets.ModelViewSet):
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)

        customer_order = serializer.save(user_id = request.user)

        self.perform_create(serializer)
        return Response(CustomerOrderSerializer(customer_order).data, status=status.HTTP_201_CREATED)





