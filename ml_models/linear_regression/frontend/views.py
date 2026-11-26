import json
from urllib.error import URLError
from urllib.request import Request, urlopen

from django import forms
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


class ViviendaForm(forms.Form):
    superficie = forms.FloatField(
        label='Superficie (m²)', min_value=70, max_value=150,
        help_text='Rango del modelo: 70 a 150 m². Ejemplo: 100.',
    )


@require_http_methods(['GET', 'POST'])
def inicio(request):
    formulario = ViviendaForm(request.POST if request.method == 'POST' else None)
    precio = None

    if formulario.is_valid():
        try:
            consulta = Request(
                f'{settings.BACKEND_URL}/predecir',
                data=json.dumps(formulario.cleaned_data).encode('utf-8'),
                headers={'Content-Type': 'application/json'},
                method='POST',
            )
            with urlopen(consulta, timeout=5) as respuesta:
                precio = json.load(respuesta)['precio_estimado_cop']
        except (URLError, TimeoutError, ValueError, KeyError):
            formulario.add_error(None, 'No se pudo obtener la predicción. Intenta de nuevo.')

    return render(request, 'inicio.html', {
        'formulario': formulario,
        'precio': precio,
        'swagger_url': f'{settings.BACKEND_URL}/docs',
    })
