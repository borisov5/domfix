from django import forms

from domfix.domfix_products.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'description', 'availability', 'item_code', 'price', 'photo', 'manufacturer')


class DeleteProductForm(ProductForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
