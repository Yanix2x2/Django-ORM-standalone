import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    passcard_amount = Passcard.objects.count()
    active_passcard = Passcard.objects.filter(is_active=True).count()
    print('Всего пропусков: ', passcard_amount)
    print('Активных пропусков: ', active_passcard)
