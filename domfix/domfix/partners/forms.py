from django import forms

from domfix.partners.models import Partner


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = '__all__'


class PartnerCreateForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ('name', 'description', 'photo')


class DeletePartnerForm(PartnerForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
