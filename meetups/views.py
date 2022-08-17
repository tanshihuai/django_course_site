from django.shortcuts import render, redirect

from .models import Meetup, Participant

from .forms import RegistrationForm

# Create your views here.

def index(request):
    meetups = Meetup.objects.all()

    return render(request, 'meetups/index.html', {'meetups': meetups})


def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        print(selected_meetup)
        if request.method == "GET":
            form = RegistrationForm()                                   # creates an object(a row in the data base basically)
        else:
            form = RegistrationForm(request.POST)                       # creates an object(a row in the data base basically)
            if form.is_valid():
                entered_email = form.cleaned_data['email']              # cleaned data is a dictionary of all the date entered in the form
                participant, was_created = Participant.objects.get_or_create(email=entered_email)
                selected_meetup.participants.add(participant)
                return redirect('/meetups/success')

        return render(request, 'meetups/meetup-details.html', {
                    'selected_meetup': selected_meetup, 
                    'meetup_found': True, 
                    'form': form
                })

    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', {'meetup_found': False})

def confirm_registration(request):
    return render(request, 'meetups/registration-success.html')