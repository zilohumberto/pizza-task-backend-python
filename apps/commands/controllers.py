from commands.models import Command, CommandStatus


class CommandController:
    COOKING = CommandStatus.objects.get(name='cooking')
    COOKED = CommandStatus.objects.get(name='cooked')

    @classmethod
    def set_cooking(cls, order):
        cls._update_status(order, cls.COOKING)

    @classmethod
    def set_cooked(cls, order):
        cls._update_status(order, cls.COOKED)

    @staticmethod
    def _update_status(order, status):
        Command.objects.filter(order_id=order).update(**{'status': status})
