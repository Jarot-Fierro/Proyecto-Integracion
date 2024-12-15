from django import forms

class RegisterForm(forms.Form):
    nombre_producto = forms.CharField(label = 'Producto',
                                min_length=4, 
                                max_length=50, 
                                widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'id': 'nameProducto',
                               }))
    precio = forms.IntegerField(label = 'Precio',
                                    widget=forms.NumberInput(attrs={
                                   'class': 'form-control',
                                   'id': 'precioProducto',
                               }))
    stock = forms.IntegerField(label = 'Stock',
                                    widget=forms.NumberInput(attrs={
                                   'class': 'form-control',
                                   'id': 'stockProducto',
                               }))
    fecha_compra = forms.DateField(label = 'Fecha de Compra',widget=forms.DateTimeInput(attrs={
                                   'class': 'form-control',
                                   'id': 'fechaCompra',
                                   'placeholder': 'Mes/día/Año',
                               }))