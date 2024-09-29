from django import forms
from .models import Producto, Cliente, Venta, Proveedor, Categoria

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'proveedor', 'precio', 'stock']

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio < 0:
            raise forms.ValidationError('El precio no puede ser negativo.')
        return precio

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'correo', 'telefono', 'direccion']


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['producto', 'cliente', 'cantidad']


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise forms.ValidationError('El nombre no puede quedar vacio.')
        if len(nombre) <= 3:
            raise forms.ValidationError('el nombre debe tener al menos 3 caracteres.')
        return nombre
    

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'contacto', 'direccion']

    def clean_contacto(self):
        contacto = self.cleaned_data.get('contacto')
        if not contacto.isdigit():
            raise forms.ValidationError('el numero de telefono debe contener solo digitos.')
        return contacto