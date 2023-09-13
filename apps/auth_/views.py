from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Importe o formulário de registro apropriado
from .forms import RegisterForm, PostForm
from .models import Post

@login_required(login_url='/login')
def home(request):
    posts = Post.objects.all()

    if request.method == 'POST':
        post_id = request.POST.get('post-id')
        user_id = request.POST.get('user-id')

        if post_id:
            post = Post.objects.filter(id=post_id).first()
            if post and (post.author == request.user or request.user.has_perm('auth_.delete_post')):
                post.delete()
        elif user_id:
            user = User.objects.filter(id=user_id).first()
            if user and request.user.is_staff:
                try:
                    group = Group.objects.get(name='default')
                    group.user_set.remove(user)
                except Group.DoesNotExist:
                    pass  # Lidar com a situação em que o grupo não existe

                try:
                    group = Group.objects.get(name='mod')
                    group.user_set.remove(user)
                except Group.DoesNotExist:
                    pass  # Lidar com a situação em que o grupo não existe

    return render(request, 'main/home.html', {'posts': posts})

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


