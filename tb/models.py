from django.db.models import Model as M
from django.db.models import PositiveIntegerField, TextField, BooleanField

class TelegramUser(M):
    external_id = PositiveIntegerField(
        verbose_name="ИД",
    )

    name = TextField(
        verbose_name="Имя"
    )

    is_admin = BooleanField(
        default=False,
        verbose_name="Администратор"
    )

    class Meta:
        verbose_name = 'Пользователь Telegram'
        verbose_name_plural = 'Пользователи Telegram'