from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .models import Contact
# Create your views here.
def contact(request):
    listing_id = request.POST['listing_id']
    listing = request.POST['listing']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    realtor_email = request.POST['realtor_email']

    if request.user.is_authenticated:
        user_id = request.user.id
        has_contacted = Contact.objects.filter(user_id=user_id, listing_id=listing_id)
        if has_contacted:
            messages.error(request, "You have already made an inquiry for this listing")
            return redirect('/listings/'+listing_id)

    contact = Contact(listing_id=listing_id, listing=listing, name=name, email=email, phone=phone, message=message,
     user_id=user_id)

    contact.save()

    ## Uncomment if you configured mail in settings.py
    '''
    send_mail(
        'Property Listing Inquiry',
        'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
        '<sender mail>@gmail.com',
        [realtor_email, '<your cc mail>@gmail.com'],
        fail_silently=False

    )
    '''

    messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')

    return redirect('/listings/'+listing_id)