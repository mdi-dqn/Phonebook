from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Contact, Phone
from .forms import contactForm, phoneForm

@login_required
def index(request):
    contacts = Contact.objects.filter(user=request.user)
    paginator = Paginator(contacts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'contacts' : page_obj
    }
    return  render(request, 'phonebook/index.html', context)

@login_required
def addContact(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/')
    else:
        form = contactForm()
    return render(request, 'phonebook/addContact.html', {'form':form})

@login_required
def editContact(request, id):
    contact = Contact.objects.get(id=id)
    if request.method=='POST':
        form = contactForm(request.POST, request.FILES ,instance=contact)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = contactForm(instance=contact)
    return render(request, 'phonebook/editContact.html', {'form':form})

@login_required
def deleteContact(request, id):
    Contact.objects.get(id=id).delete()
    return redirect('/')

@login_required
def detailsContact(request, id):
    contact = Contact.objects.get(id=id)
    return render(request, 'phonebook/detailsContact.html', {'contact':contact})

#########################################################################################

@login_required
def indexPhone(request, id_c):
    phones = Phone.objects.filter(contact_id=id_c)
    contact = Contact.objects.get(id=id_c)
    return render(request, 'phonebook/indexPhone.html', {'phones':phones, 'contact' : contact})

@login_required
def addPhone(request, id_c):
    if request.method == 'POST':
        form = phoneForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.contact = Contact.objects.get(id=id_c)
            instance.save()
            return redirect('phonebook:indexPhone',id_c)
    else:
        form = phoneForm()
    return render(request,'phonebook/addPhone.html', {'form':form, 'id_c':id_c})

@login_required
def deletePhone(request, id_p):
    phone = Phone.objects.get(id=id_p)
    id_c = phone.contact_id
    phone.delete()
    return redirect('phonebook:indexPhone', id_c)

@login_required
def editPhone(request, id_p):
    phone = Phone.objects.get(id=id_p)
    if request.method == 'POST':
        form = phoneForm(request.POST, instance=phone)
        if form.is_valid():
            form.save()
            return redirect('phonebook:indexPhone', phone.contact_id)
    else:
        form = phoneForm(instance=phone)
    return render(request, 'phonebook/editPhone.html', {'form':form})

#####################################################################################