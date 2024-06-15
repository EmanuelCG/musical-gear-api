from rest_framework import serializers
from .models import CustomerOrder,OrderStatus, OrderItem
from items.models import Item


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['item_id', 'quantity']

class CustomerOrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, write_only=True)  # Cambiar read_only a write_only para recibir datos de entrada
    order_status_id = OrderStatusSerializer(read_only=True)
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())  # Usar HiddenField para asignar el usuario automáticamente

    class Meta:
        model = CustomerOrder
        fields = ['id', 'user_id', 'order_status_id', 'order_time', 'time_paid', 'time_canceled', 'time_completed', 'total_price', 'order_items']
        read_only_fields = ['total_price', 'order_status_id']

    def create(self, validated_data):
        # Extraer los datos de order_items de validated_data
        order_items_data = self.initial_data.get('order_items', [])

        # Calcular el total_price basado en order_items_data
        total_price = 0
        for order_item_data in order_items_data:
            item = Item.objects.get(id=order_item_data['item_id'])
            quantity = order_item_data['quantity']
            price = item.price * quantity
            total_price += price

        order_status_id, created = OrderStatus.objects.get_or_create(status_name='order_placed')

        # Crear la instancia de CustomerOrder
        customer_order = CustomerOrder.objects.create(
            user_id=validated_data['user_id'],  # Usar el usuario autenticado
            order_status_id=order_status_id,
            total_price=total_price,
            active=validated_data.get('active', True),
            time_paid=None,
            time_canceled=None,
            time_completed=None
        )

        # Crear las instancias de OrderItem asociadas al CustomerOrder
        for order_item_data in order_items_data:
            OrderItem.objects.create(
                customer_order_id=customer_order,
                item_id=Item.objects.get(id=order_item_data['item_id']),
                quantity=order_item_data['quantity'],
                price=Item.objects.get(id=order_item_data['item_id']).price * order_item_data['quantity']
            )

        return customer_order