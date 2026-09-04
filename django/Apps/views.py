from django.shortcuts import render
from .models import ChaiVarity
from django.shortcuts import get_list_or_404
from .forms import ChaiVarityForm
# Create your views here.

def books(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'Apps/all_apps.html', {'chais':chais})


def chai_detail(request, chai_id):
    chai = get_list_or_404(ChaiVarity, pk=chai_id)
    return render(request, 'Apps/chai_details.html', {'chai':chai})

def chai_sotre_view(request):
    stores = None
    if request.method =='POST' :
        form = ChaiVarityForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_varity']
            Store = Store.objects.filter(chai_varites = chai_variety)
            
        else:
            form = ChaiVarityForm()
        return render(request, ' Apps/chai_sotores.html',
                    {'stores': stores, 'form': form}
                      )    