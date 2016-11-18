from django.shortcuts import render,redirect
from .forms import PrestamoForm

# Create your views here.
def ingreso_prestamo(request):
    if request.method=="POST":
        formulario = PrestamoForm(request.POST)
        if formulario.is_valid():
            prestamo = formulario.save(commit=False)
            prestamo.save()
            return redirect('/prestamos')
    else:
        formulario=PrestamoForm()
    return render(request, 'blog/prestamos.html', {'formulario':formulario})
