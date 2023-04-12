from inicio.models import Persona
from django.shortcuts import render, redirect
from inicio.forms import AltaAgenteFormulario, BuscarAgente


def mi_vista(request):
    return render(request, 'inicio/index.html')

def crear_agente(request):
    
    if request.method == "POST":
        formulario = AltaAgenteFormulario(request.POST)
        
        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data
        
            agente = Persona(nombre=datos_correctos['nombre'], apellido=datos_correctos['apellido'],
                             legajo=datos_correctos['legajo'],fecha_nacimiento=datos_correctos['fecha_nacimiento'] )
            agente.save()

            return redirect('inicio:listar_agente')
    
    formulario = AltaAgenteFormulario()
    return render(request, 'inicio/crear_agente.html', {'formulario': formulario})


def lista_agentes(request):
    nombre_a_buscar = request.GET.get('nombre', None)
    
    if nombre_a_buscar:
        agentes = Persona.objects.filter(apellido__icontains=nombre_a_buscar)
    else:
        agentes = Persona.objects.all()
    formulario_busqueda = BuscarAgente()
    return render(request, 'inicio/lista_agentes.html', {'agentes': agentes, 'formulario': formulario_busqueda})
