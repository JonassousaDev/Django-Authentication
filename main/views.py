from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm  # Importe o formulário de registro apropriado

@login_required(login_url='/login')
def home(request):
    return render(request, 'main/home.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Salve o usuário
            login(request, user)  # Faça login automaticamente após o registro
            return redirect('home')  # Redirecione para a página inicial ou para onde você desejar

    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {'form': form})
