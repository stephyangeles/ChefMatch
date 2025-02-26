from django.shortcuts import render
from .models import GeneralLedger

def ledger_list(request):
    ledger_entries = GeneralLedger.objects.all()
    return render(request, 'ledger_list.html', {'ledger_entries': ledger_entries})
