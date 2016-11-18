from django import forms
from .models import Editorial,Autor,Libro, Prestamos

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamos
        fields = ('fecha_prestamo','fecha_devolucion_prop','fecha_devolucion_real', 'libro', 'usuario',)
        widgets = {
            'libro':forms.SelectMultiple,
            'usuario': forms.Select,
}
