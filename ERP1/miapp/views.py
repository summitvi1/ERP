from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article, Category
from django.db.models import Q
from miapp.forms import FormularioArticulo
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html', {
        'title': 'Inicio',
        'mi_variable': 'Soy un dato que esta en la vista'
    })

def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def pagina(request):
    return render(request, 'pagina.html')

def contacto(request):
    return render(request, 'contacto.html')

#models

def crear_articulo(request):
    articulo = Article(
        title = "Segundo articulo",
        content = "Contenido del articulo",
        public = True
    )
    articulo.save()


    return HttpResponse(f"Usuario creado: ")

# formulario
def save_articulo(request):
    if request.method == 'POST':

        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']

        articulo = Article(
            title = title,
            content = content,
            public = public
        )
        articulo.save() 
        return HttpResponse(f"Articulo creado <strong>{articulo.id}</strong>")
    else:
       return HttpResponse("<h1>No se creo el articulo</h1>")

def create_article(request):
    return render(request, 'create_article.html')

def create_full_article(request):
    if request.method == 'POST':
        formulario = FormularioArticulo(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            title = data_form.get('title')
            content = data_form['content']
            public = data_form['public']
            
            articulo = Article(
                title = title,
                content = content,
                public = public
            )
            articulo.save() 
            
            #crear mensaje flash (sesion que solo se muestra 1 vez)
            messages.success(request, f'Has creado correctamente el articulo {articulo.id}')
            
            return redirect('articulos')
            #return HttpResponse(articulo.title + ' - ' + articulo.content + ' - ' + str(articulo.public))
    else:
        formulario = FormularioArticulo()
    return render(request, 'create_full_article.html', {
        'form': formulario
    })

#endformulario
def articulos(request):

    articulos = Article.objects.order_by('id')[:30]
    return render(request, 'articulos.html', {
        'articulos': articulos
    })