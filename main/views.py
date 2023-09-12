from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Importe o formulário de registro apropriado
from .forms import RegisterForm, PostForm

@login_required(login_url='/login')
def home(request):
    return render(request, 'main/home.html')

@login_required(login_url='/login')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Defina o autor do post como o usuário autenticado
            post.save()
            return redirect('home')  # Redirecione para a página inicial ou outra página apropriada após a criação do post

    else:
        form = PostForm()

    return render(request, 'main/create_post.html', {'form': form})



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
