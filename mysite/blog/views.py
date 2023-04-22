from django.views import generic
from .models import MaleMeasurement
from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        measurment_height = request.POST['height']
        measurment_age = request.POST['age']
        measurment_weight = request.POST['weight']
        measurment_waist = request.POST['waist']

        # check if the measurement already exists
        existing_measurement = MaleMeasurement.objects.filter(height=measurment_height, age=measurment_age, weight=measurment_weight, waist=measurment_waist)
        if existing_measurement:
            return render(request, 'index.html', {'error_message': 'Your measurment already exists.'})
        else:
            male_measurement = MaleMeasurement(height=measurment_height, age=measurment_age, weight=measurment_weight, waist=measurment_waist)
            male_measurement.save()
            return render(request, 'index.html', {'error_message': 'Your new measurment is saved succesfully.'})
            

    return render(request, 'index.html')  

def register(request):
    measurements = MaleMeasurement.objects.all()
    context = {'measurements': measurements}
    return render(request, 'register.html', context)      

	


class PostList(generic.ListView):
    model = MaleMeasurement
    template_name = 'index.html'



