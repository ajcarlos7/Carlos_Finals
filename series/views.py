from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser, Series


# HOME
def home(request):
    query = request.GET.get('q')

    if query:
        series_list = Series.objects.filter(
            title__icontains=query
        ).order_by('-release_date')
    else:
        series_list = Series.objects.all().order_by('-release_date')

    return render(request, 'series/home.html', {
        'series_list': series_list,
        'query': query,
    })


# AUTHENTICATION
def signup_view(request):
    if request.method != "POST":
        return redirect('home')

    username = request.POST.get('username')
    email = request.POST.get('email')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')

    if password1 != password2:
        messages.error(request, "Passwords do not match.")
        return redirect('home')

    if CustomUser.objects.filter(username=username).exists():
        messages.error(request, "Username already exists.")
        return redirect('home')

    CustomUser.objects.create_user(
        username=username,
        email=email,
        password=password1
    )

    messages.success(
        request,
        "Account created successfully. Please log in."
    )

    return redirect('home')


def login_view(request):
    if request.method != "POST":
        return redirect('home')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)

    if user:
        auth_login(request, user)
        messages.success(request, f"Welcome back, {username}!")
        return redirect('user_profile', username=username)

    messages.error(request, "Invalid credentials.")
    return redirect('home')


@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('home')


# USER PROFILE
@login_required
def user_profile(request, username):
    profile_user = get_object_or_404(CustomUser, username=username)
    favorites = profile_user.favorites.all()

    return render(request, 'series/user_profile.html', {
        'profile_user': profile_user,
        'favorites': favorites,
    })


# SERIES
def series_info(request, pk):
    series = get_object_or_404(Series, id=pk)

    in_favorites = (
        request.user.is_authenticated and
        series in request.user.favorites.all()
    )

    first_platform = series.streaming.first()

    return render(request, 'series/series_info.html', {
        'series': series,
        'in_favorites': in_favorites,
        'first_platform': first_platform,
    })


def series_list(request):
    series_list = Series.objects.all().order_by('-release_date')
    return render(request, 'series/home.html', {'series_list': series_list})

# GENRES
def genres(request):
    genres_list = Series.objects.values_list('genre', flat=True).distinct()
    return render(request, 'series/genres.html', {
        'genres': genres_list
    })


def genre_detail(request, genre):
    filtered_series = Series.objects.filter(genre__icontains=genre)
    return render(request, 'series/genre_detail.html', {
        'genre': genre,
        'series_list': filtered_series
    })


# FAVORITES
@login_required
def add_favorite(request, series_id):
    series = get_object_or_404(Series, id=series_id)

    if series in request.user.favorites.all():
        messages.info(request, f"{series.title} is already in your favorites.")
    else:
        request.user.favorites.add(series)
        messages.success(request, f"{series.title} added to your favorites!")

    return redirect('series-info', pk=series_id)


@login_required
def remove_favorite(request, series_id):
    series = get_object_or_404(Series, id=series_id)

    if series in request.user.favorites.all():
        request.user.favorites.remove(series)
        messages.success(request, f"{series.title} removed from your favorites.")

    return redirect('user_profile', username=request.user.username)
