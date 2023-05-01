from django.core.management.base import BaseCommand

from tgcore.management.commands.bot import tg_bot


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        tg_bot.infinity_polling()