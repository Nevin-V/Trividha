from django.shortcuts import render , redirect
from .models import events
from .models import school,basic_details
from .models import participant_details
from django.contrib import messages
from home.models import details
from django.core.mail import EmailMessage
from django.db import transaction, IntegrityError


# Create your views here.
def register(request):
    if request.method == 'POST':
        # Debug: Print all POST data
        print("POST data:")
        for key, values in request.POST.lists():
            print(f"('{key}', {values})")
        
        # Get the school (replace with your logic to get current school)

        school_name = request.POST.get("school")
        if not school_name:
            messages.error(request, 'Please provide a school name!')
            event_obj = events.objects.all()
            return render(request, 'form.html', {"events": event_obj})
        
        # Create or get the school OBJECT (not just the string)
        try:
            current_school = school.objects.get(name=school_name)
            # School already exists - show error message
            messages.error(request, f'School "{school_name}" is already registered! if you want to register more participants please contact +91 82898 27930')
            event_obj = events.objects.all()
            return render(request, 'form.html', {"events": event_obj})
        except school.DoesNotExist:
            # School doesn't exist, create new one
            current_school = school.objects.create(name=school_name)
            print(f"New school created: {current_school}")


        part=request.POST.get("participant_no")
        teaching=request.POST.get("non teaching")
        non_veg=request.POST.get("non veg")
        veg=request.POST.get("veg")
        basic_details.objects.create(school=current_school,participants_number=part,staff_number=teaching,veg=veg,non_veg=non_veg)
            
        
        # Process participant data
        saved_count = 0
        for key, values in request.POST.lists():
            if key.startswith('event_') and key.endswith('_participants[]'):
                try:
                    # Extract event ID from key like 'event_1_participants[]'
                    event_id = key.split('_')[1]
                    event = events.objects.get(id=event_id)
                    
                    # Save each participant
                    for participant_name in values:
                        name = participant_name.strip()
                        if name:  # Only save non-empty names
                            participant_details.objects.create(
                                name=name,
                                school=current_school,
                                events=event
                            )
                            saved_count += 1
                            
                except (events.DoesNotExist, IndexError, ValueError) as e:
                    print(f"Error processing {key}: {e}")
                    continue
        
        if saved_count > 0:
            messages.success(request, f'{saved_count} participants added successfully!')
        else:
            messages.warning(request, 'No participants were added!')


        email = EmailMessage(
        subject=f"{school_name} - New registration",
        body=f"Hello \n New school Registered for Trividha : {school_name} \n Total students: {part} \n check participant details at: https://trividha.onrender.com/data_view/ ",
        from_email="trividhaofficial2025@gmail.com",
        to =["siteoftrividha@gmail.com"],  )
        email.send()
        
        return redirect('success')  




    event_obj=events.objects.all
    date=details.objects.first

    return render(request,'form.html',{"events":event_obj,"date":date})


def success(request):
    return render(request,"success.html",)