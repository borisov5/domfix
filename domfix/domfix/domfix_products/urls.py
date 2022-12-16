from django.urls import include, path

from domfix.domfix_products.views import add_product, details_product, edit_product, delete_product

urlpatterns = (
    path('add/', add_product, name='add product'),
    path('<int:pk>/', include([
        path('details/', details_product, name='details product'),
        path('edit/', edit_product, name='edit product'),
        path('delete/', delete_product, name='delete product'),
    ]))
)