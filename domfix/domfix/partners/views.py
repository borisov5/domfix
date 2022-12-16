from django.shortcuts import render, redirect

from domfix.partners.forms import PartnerCreateForm, DeletePartnerForm, PartnerForm
from domfix.partners.models import Partner


def show_partners(request):
    partners = Partner.objects.all()
    context = {
        'partners': partners,
    }
    return render(request, 'partners/partners-page.html', context)


def add_partner(request):
    if request.method == 'GET':
        form = PartnerCreateForm()
    else:
        form = PartnerCreateForm(request.POST)
        if form.is_valid():
            partner = form.save(commit=True)
        return redirect('show partners')

    context = {
        'form': form,
    }

    return render(request, 'partners/partner-add-page.html', context)


def details_partner(request, pk):
    partner = Partner.objects.get(id=pk)
    context = {
        'partner': partner,
    }
    return render(request, 'partners/partner-details-page.html', context)


def edit_partner(request, pk):
    partner = Partner.objects.get(id=pk)
    if request.method == "GET":
        context = {
            'form': PartnerForm(initial=partner.__dict__),
        }
        return render(request, 'partners/partner-edit-page.html', context)

    else:
        form = PartnerForm(request.POST, instance=partner)

        if form.is_valid():
            form.save()
            return redirect('show partners')
        else:
            context = {
                'form': form,
            }
    return render(request, 'partners/partner-edit-page.html', context)


def delete_partner(request, pk):
    partner = Partner.objects.get(id=pk)

    if request.method == 'POST':
        partner.delete()
        return redirect('show partners')

    form = DeletePartnerForm(instance=partner)
    context = {
        'form': form,
    }

    return render(request, 'partners/partner-delete-page.html', context)
