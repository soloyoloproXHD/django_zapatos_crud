from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Usuario, Zapato

# Create your views here.
class User:
    def login_page(request):
        return render(request, 'login.html')
    
    def register_page(request):
        return render(request, 'register.html')
    
    def validate_user(request):
        if request.method == 'POST':
            email = request.POST.get("email")
            password = request.POST.get("password")
            
            if Usuario.objects.filter(email=email, password=password).exists():
                messages.success(request, 'Usuario autenticado correctamente.')
                return redirect('tabla')
    
    def register_user(request):
        if request.method == 'POST':
            email = request.POST.get("email")
            password = request.POST.get("password")
            
            if Usuario.objects.filter(email=email).exists():
                messages.error(request, 'El email ya se encuentra registrado')
            else:
                usuario = Usuario.objects.create(email=email, password=password)
                usuario.save()
                messages.success(request, 'Usuario registrado correctamente.')
                return redirect('login')
        return render(request, render('register.html'))

class Shoes:
    def zapato_page(request):
        return render(request, 'zapatos.html')
    
    def tabla_page(request):
        zapatos = Zapato.objects.all()
        data = zapatos.values()
        return render(request, 'tabla.html', {'zapatos': data})
    
    def eliminar_zapato(request, id):
        Zapato.objects.filter(id=id).delete()
        messages.success(request, 'Zapato eliminado correctamente.')
        return redirect('tabla')
    
    def actualizar_zapato(request, id):
        zapato = get_object_or_404(Zapato, id=id)
        if request.method == 'POST':
            zapato.marca = request.POST.get('marca')
            zapato.modelo = request.POST.get('modelo')
            zapato.talla = request.POST.get('talla')
            zapato.color = request.POST.get('color')
            zapato.precio = request.POST.get('precio')
            zapato.stock = request.POST.get('stock')
            zapato.descripcion = request.POST.get('descripcion')
            zapato.estado = request.POST.get('estado') == 'on'
            zapato.save()
            messages.success(request, 'Zapato actualizado correctamente.')
            return redirect('tabla')
        return render(request, 'zapatos.html', {'zapato': zapato})
    
    def register_zapato(request):
        if request.method == 'POST':
            marca = request.POST.get("marca")
            modelo = request.POST.get("modelo")
            talla = request.POST.get("talla")
            color = request.POST.get("color")
            precio = request.POST.get("precio")
            stock = request.POST.get("stock")
            descripcion = request.POST.get("descripcion")
            
            Zapato.objects.create(
                marca=marca, 
                modelo=modelo, 
                talla=talla, 
                color=color, 
                precio=precio, 
                stock=stock, 
                descripcion=descripcion,
                estado=True
            )
            messages.success(request, 'Zapato registrado correctamente.')
        return redirect('tabla')
            