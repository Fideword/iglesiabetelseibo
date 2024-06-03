from .forms import MiembroForm, ServicioForm, ActividadeForm, SocieForm, MinistForm, Esc_DomForm
from .models import Miembro, Servicio, Actividade, Socie, Minist, Esc_Dom, Edades, Ministerio, Escuela_Dominical
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from .models import Mensaje

# Create your views here.

def es_administrador(user):
    return user.groups.filter(name='Administradores').exists()

administrador_required = user_passes_test(es_administrador)

def index(request):
    return render(request, 'miembros/index.html')

@login_required
def lista_miembros(request):
    query = request.GET.get('query')
    if query:
        miembros = Miembro.objects.filter(Nombres__icontains=query) | Miembro.objects.filter(Apellidos__icontains=query)
    else:
        miembros = Miembro.objects.all()
    return render(request, 'miembros/lista_miembros.html', {'miembros': miembros})

@login_required
def ver_edades(request):
    edades = Edades.objects.all()
    return render(request, 'miembros/ver_edades.html', {'edades': edades})

@login_required
def ver_escuela_dominical(request):
    escuela_dominical = Escuela_Dominical.objects.all()
    return render(request, 'miembros/ver_escuela_dominical.html', {'escuela_dominical': escuela_dominical})

@login_required
def detalle_miembro(request, miembro_id):
    miembro = get_object_or_404(Miembro, pk=miembro_id)
    return render(request, 'miembros/detalle_miembro.html', {'miembro': miembro})

@administrador_required
def registrar_miembro(request):
    if request.method == 'POST':
        form = MiembroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_miembros')
    else:
        form = MiembroForm()
    return render(request, 'miembros/registrar_miembro.html', {'form': form})

@administrador_required
def editar_miembro(request, miembro_id):
    miembro = get_object_or_404(Miembro, pk=miembro_id)
    if request.method == 'POST':
        form = MiembroForm(request.POST, request.FILES, instance=miembro)
        if form.is_valid():
            form.save()
            return redirect('detalle_miembro', miembro_id=miembro_id)
    else:
        form = MiembroForm(instance=miembro)
    return render(request, 'miembros/editar_miembro.html', {'form': form})

@administrador_required
def eliminar_miembro(request, miembro_id):
    miembro = get_object_or_404(Miembro, pk=miembro_id)
    if request.method == 'POST':
        miembro.delete()
        return redirect('lista_miembros')
    return render(request, 'miembros/eliminar_miembro.html', {'miembro': miembro})

@login_required
def miembros_genero(request, genero):
    miembros = Miembro.objects.filter(Genero=genero)
    return render(request, 'miembros/miembros_genero.html', {'miembros': miembros, 'genero': genero})

@login_required
def miembros_fecha_conversion(request, fecha_conversion):
    miembros = Miembro.objects.filter(Fecha_Conversion=fecha_conversion)
    return render(request, 'miembros/miembros_fecha_conversion.html', {'miembros': miembros, 'fecha_conversion':fecha_conversion})

@login_required
def miembros_fecha_bautizo(request, fecha_bautizo):
    miembros = Miembro.objects.filter(Fecha_Bautizo=fecha_bautizo)
    return render(request, 'miembros/miembros_fecha_bautizo.html', {'miembros': miembros, 'fecha_bautizo':fecha_bautizo})

@login_required
def miembros_estatus(request, miembros_estatus):
    miembros = Miembro.objects.filter(Estatus_Miembro=miembros_estatus)
    return render(request, 'miembros/miembros_estatus.html', {'miembros': miembros, 'miembros_estatus': miembros_estatus})

@login_required
def miembros_ministerio(request, ministerio_id):
    ministerio = get_object_or_404(Ministerio, pk=ministerio_id)
    miembros = ministerio.miembros.all()
    return render(request, 'miembros/miembros_ministerio.html', {'ministerio': ministerio, 'miembros': miembros})

@login_required
def miembros_sociedad(request, sociedad):
    miembros = Miembro.objects.filter(Sociedad=sociedad)
    return render(request, 'miembros/miembros_sociedad.html', {'miembros': miembros, 'sociedad':sociedad})

@login_required
def miembros_edades(request, edades_id):
    edades = get_object_or_404(Edades, pk=edades_id)
    miembros = Miembro.objects.filter(Edades=edades)
    return render(request, 'miembros/miembros_edades.html', {'edades': edades, 'miembros': miembros})


@login_required
def miembros_escuela_dominical(request, escuela_dominical_id):
    escuela_dominical = get_object_or_404(Escuela_Dominical, pk=escuela_dominical_id)
    miembros = Miembro.objects.filter(Escuela_Dominical=escuela_dominical)
    return render(request, 'miembros/miembros_escuela_dominical.html', {'escuela_dominical': escuela_dominical, 'miembros': miembros})

def servicio(request):
    servicios = Servicio.objects.all()
    return render(request, 'miembros/servicios.html', {'servicios': servicios})

@administrador_required
def agregar_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('servicio')
    else:
        form = ServicioForm()
    return render(request, 'miembros/agregar_servicio.html', {'form': form})

@administrador_required
def editar_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, pk=servicio_id)
    if request.method == 'POST':
        form = ServicioForm(request.POST, request.FILES, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('servicio')
    else:
        form = ServicioForm(instance=servicio)
    return render(request, 'miembros/editar_servicio.html', {'form': form})

@administrador_required
def eliminar_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, pk=servicio_id)
    if request.method == 'POST':
        servicio.delete()
        return redirect('servicio')
    return render(request, 'miembros/eliminar_servicio.html', {'servicio': servicio})

def actividade(request):
    actividades = Actividade.objects.all()
    return render(request, 'miembros/actividades.html', {'actividades': actividades})

@administrador_required
def agregar_actividade(request):
    if request.method == 'POST':
        form = ActividadeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('actividade')
    else:
        form = ActividadeForm()
    return render(request, 'miembros/agregar_actividade.html', {'form': form})

@administrador_required
def editar_actividad(request, actividade_id):
    actividade = get_object_or_404(Actividade, pk=actividade_id)
    if request.method == 'POST':
        form = ActividadeForm(request.POST, request.FILES, instance=actividade)
        if form.is_valid():
            form.save()
            return redirect('actividade')
    else:
        form = ActividadeForm(instance=actividade)
    return render(request, 'miembros/editar_actividad.html', {'form': form})

@administrador_required
def eliminar_actividad(request, actividade_id):
    actividade = get_object_or_404(Actividade, pk=actividade_id)
    if request.method == 'POST':
        actividade.delete()
        return redirect('actividade')
    return render(request, 'miembros/eliminar_actividad.html', {'actividade': actividade})

def socie(request):
    socie = Socie.objects.all()
    return render(request, 'miembros/socie.html', {'socie': socie})

@administrador_required
def agregar_socie(request):
    if request.method == 'POST':
        form = SocieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('socie')
    else:
        form = SocieForm()
    return render(request, 'miembros/agregar_socie.html', {'form': form})

@administrador_required
def editar_sociedad(request, socie_id):
    socie = get_object_or_404(Socie, pk=socie_id)
    if request.method == 'POST':
        form = SocieForm(request.POST, request.FILES, instance=socie)
        if form.is_valid():
            form.save()
            return redirect('socie')
    else:
        form = SocieForm(instance=socie)
    return render(request, 'miembros/editar_sociedad.html', {'form': form})

@administrador_required
def eliminar_sociedad(request, socie_id):
    socie = get_object_or_404(Socie, pk=socie_id)
    if request.method == 'POST':
        socie.delete()
        return redirect('socie')
    return render(request, 'miembros/eliminar_sociedad.html', {'socie': socie})

def minist(request):
    minist = Minist.objects.all()
    return render(request, 'miembros/minist.html', {'minist': minist})

@administrador_required
def agregar_minist(request):
    if request.method == 'POST':
        form = MinistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('minist')
    else:
        form = MinistForm()
    return render(request, 'miembros/agregar_minist.html', {'form': form})

@administrador_required
def editar_ministerio(request, minist_id):
    minist = get_object_or_404(Minist, pk=minist_id)
    if request.method == 'POST':
        form = MinistForm(request.POST, request.FILES, instance=minist)
        if form.is_valid():
            form.save()
            return redirect('minist')
    else:
        form = MinistForm(instance=minist)
    return render(request, 'miembros/editar_ministerio.html', {'form': form})

@administrador_required
def eliminar_ministerio(request, minist_id):
    minist = get_object_or_404(Minist, pk=minist_id)
    if request.method == 'POST':
        minist.delete()
        return redirect('minist')
    return render(request, 'miembros/eliminar_ministerio.html', {'minist': minist})

def esc_dom(request):
    esc_dom = Esc_Dom.objects.all()
    return render(request, 'miembros/esc_dom.html', {'esc_dom': esc_dom})

@administrador_required
def agregar_esc_dom(request):
    if request.method == 'POST':
        form = Esc_DomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('esc_dom')
    else:
        form = Esc_DomForm()
    return render(request, 'miembros/agregar_esc_dom.html', {'form': form})

@administrador_required
def editar_esc_dom(request, esc_dom_id):
    esc_dom = get_object_or_404(Esc_Dom, pk=esc_dom_id)
    if request.method == 'POST':
        form = Esc_DomForm(request.POST, request.FILES, instance=esc_dom)
        if form.is_valid():
            form.save()
            return redirect('esc_dom')
    else:
        form = Esc_DomForm(instance=esc_dom)
    return render(request, 'miembros/editar_esc_dom.html', {'form': form})

@administrador_required
def eliminar_esc_dom(request, esc_dom_id):
    esc_dom = get_object_or_404(Esc_Dom, pk=esc_dom_id)
    if request.method == 'POST':
        esc_dom.delete()
        return redirect('esc_dom')
    return render(request, 'miembros/eliminar_esc_dom.html', {'esc_dom': esc_dom})

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')

        mensaje_obj = Mensaje(
            nombre=nombre,
            email=email,
            telefono=telefono,
            asunto=asunto,
            mensaje=mensaje
        )
        mensaje_obj.save()

        return redirect(reverse('contacto'))
    return render(request, 'miembros/contacto.html')

@administrador_required
def ver_mensajes(request):
    mensajes = Mensaje.objects.all()
    return render(request, 'miembros/ver_mensajes.html', {'mensajes': mensajes})

@administrador_required
def eliminar_mensaje(request, mensaje_id):
    mensaje = get_object_or_404(Mensaje, pk=mensaje_id)
    if request.method == 'POST':
        mensaje.delete()
        return redirect('ver_mensajes')
    return render(request, 'miembros/eliminar_mensaje.html', {'mensaje': mensaje})

def sobre_nosotros(request):
    return render(request, 'miembros/sobre_nosotros.html')

@login_required
def principal(request):
    return render(request, 'miembros/principal.html')

