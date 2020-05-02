from rest_framework.viewsets import ModelViewSet
from base.views import ModelViewSetNSerializer
from rest_framework.permissions import IsAuthenticated
from orders.models import OrderStatus, Order
from orders.serializers import OrderStatusSerializer, OrderSerializer, OrderRestSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse


class OrderStatusView(ModelViewSet):
    serializer_class = OrderStatusSerializer
    queryset = OrderStatus.objects.all()
    # permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'patch', 'post', 'options',)


class OrderView(ModelViewSetNSerializer):
    serializer_class = OrderSerializer
    rest_serializer_class = OrderRestSerializer
    queryset = None
    permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'patch', 'post', 'options', )

    def get_queryset(self):
        return self._get_queryset(self.request.user, self.request.GET)

    @classmethod
    def _get_queryset(cls, user, data):
        model = cls.serializer_class.Meta.model
        if user.is_superuser:
            queryset = model.objects.all()
        elif model._meta.pk.name in data:
            pk = model._meta.pk.name
            queryset = model.objects.filter(
                **{pk: data[pk]}
            )
        else:
            queryset = model.objects.filter(user=user)
        return queryset

    @staticmethod
    @api_view(['POST'])
    def bill(request):
        data = request.data
        orders = OrderView._get_queryset(request.user, data)
        result_bill = dict(items=[], total=0.0)
        if orders:
            order = orders.first()
            for command in order.command_set.all():
                toppings = []
                total = 0.0
                for topping in command.toppings.all():
                    toppings.append({
                        'is_pizza': False,
                        'name': topping.ingredient_topping.name,
                        'total': topping.amount,
                        'units': 1,
                        'status': ""
                    })
                    total += topping.amount

                result_bill["items"].append(
                    {
                        'is_pizza': True,
                        'name': command.pizza_ordered.pizza.name,
                        'units': 1,
                        'total': command.pizza_ordered.price,
                        'size': command.pizza_ordered.size.name,
                        'status': command.status.description,
                    }

                )
                result_bill["items"].extend(toppings)
                result_bill['total'] += command.pizza_ordered.price+total

        return JsonResponse(result_bill, status=200, safe=False)
