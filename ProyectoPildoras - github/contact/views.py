from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    formulario_contacto = FormularioContacto()
    if request.method == 'POST':
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            #inf_form = formulario_contacto.cleaned_data
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')
            email = EmailMessage(
                    subject='mensaje desde APP DJANGO', 
                    body='El usuario con nombre {} con la dirección {} escribe lo siguiente: \n\n {}'.format(nombre, email, contenido),
                    from_email='',
                    to=['informatica@cebollastara.com'],
                    reply_to=[email],)
            try:
                email.send()
                #pasamos una variable valido a la pagina de contacto.html
                return redirect("/contact/?valido")
            except:
                return redirect("/contact/?novalido")        
    return render(request, "contact/contacto.html", {'mi_formulario': formulario_contacto})