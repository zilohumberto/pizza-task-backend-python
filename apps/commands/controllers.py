from commands.models import Command, CommandStatus


class CommandController:
    COOKING = CommandStatus.objects.get(name='cooking')

    @classmethod
    def set_cooking(cls, order):
        Command.objects.filter(order_id=order).update(**{'status': cls.COOKING})

