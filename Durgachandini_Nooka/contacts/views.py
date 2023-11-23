from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm

def list_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'list.html', {'contacts': contacts})

def detail_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    return render(request, 'detail.html', {'contact': contact})

def create_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_contacts')
    else:
        form = ContactForm()
    return render(request, 'forms.html', {'form': form, 'form_title': 'Add New Contact'})

def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('list_contacts')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'forms.html', {'form': form, 'form_title': 'Edit Contact'})

def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == "POST":
        contact.delete()
        return redirect('list_contacts')
    return render(request, 'confirm_delete.html', {'contact': contact})
