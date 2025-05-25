from django.shortcuts import render

from .forms import RealEstateForm
from .models import RealEstate, CharacteristicRealEstate


# Create your views here.

def index(request):
    houses = RealEstate.objects.filter(is_sold=False, area__gte=100).all()
    real_estate_context = []
    for house in houses:
        price = 0
        house_characteristics = CharacteristicRealEstate.objects.filter(real_estate=house)
        for house_char in house_characteristics:
            price += house_char.characteristic.value
        real_estate_context.append({'house': house, 'price': price})

    return render(request, 'index.html', {'houses': real_estate_context})


def edit(request, house_id):
    instance = RealEstate.objects.filter(id=house_id).first()

    if request.method == "POST":
        form = RealEstateForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return index(request)  # Or use redirect('index') if appropriate
    else:
        form = RealEstateForm(instance=instance)

    return render(request, 'edit.html', {'form': form})
