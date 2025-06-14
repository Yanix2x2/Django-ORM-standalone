from datacenter.models import Passcard
from django.shortcuts import render


def active_passcards_view(request):
    context = {
        'active_passcards': Passcard.objects.filter(is_active=True),
    }
    
    return render(request, 'active_passcards.html', context)
