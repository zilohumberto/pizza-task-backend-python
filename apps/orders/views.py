from rest_framework.viewsets import ModelViewSet
from base.views import ModelViewSetNSerializer
from rest_framework.permissions import IsAuthenticated
from orders.models import OrderStatus, Order
from orders.serializers import OrderStatusSerializer, OrderSerializer, OrderRestSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse
from commands.controllers import CommandController


class OrderStatusView(ModelViewSet):
    serializer_class = OrderStatusSerializer
    queryset = OrderStatus.objects.all()
    # permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'patch', 'post', 'options',)


class OrderView(ModelViewSetNSerializer):
    serializer_class = OrderSerializer
    rest_serializer_class = OrderRestSerializer
    queryset = None
    http_method_names = ('get', 'patch', 'post', 'options', )

    def get_queryset(self):
        return self._get_queryset(self.request.user, self.request.GET, self.request.data)

    @classmethod
    def _get_queryset(cls, user, _get=dict(), data=dict()):
        model = cls.serializer_class.Meta.model
        pk = model._meta.pk.name
        filter_query = lambda x: {pk: x[pk]}
        if model._meta.pk.name in data:
            data_query = filter_query(data)
        elif model._meta.pk.name in _get:
            data_query = filter_query(_get)
        elif user.is_superuser:
            data_query = {}
        else:
            data_query = {'user': user, 'status_id__gt': 1}
        
        return model.objects.filter(**data_query)

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
                    total += (topping.ingredient_topping.cost * command.amount)

                result_bill["items"].append(
                    {
                        'is_pizza': True,
                        'name': command.pizza_ordered.pizza.name,
                        'units': command.amount,
                        'total': command.pizza_ordered.price,
                        'size': command.pizza_ordered.size.name,
                        'status': command.status.description,
                    }
                )
                result_bill["items"].extend(toppings)
                result_bill['total'] += (command.amount*command.pizza_ordered.price)+total

        return JsonResponse(result_bill, status=200, safe=False)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        response = self.update(request, *args, **kwargs)
        if response.status_code == 200:
            data = response.data
            if data['status'] == 2:
                CommandController.set_cooking(order=response.data['id'])
            if data['status'] == 3:
                CommandController.set_cooked(order=response.data['id'])
        return response
