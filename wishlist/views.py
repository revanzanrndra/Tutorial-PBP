import datetime
from urllib import response
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from wishlist.models import BarangWishlist
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/wishlist/login/')
def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
    'list_barang': data_barang_wishlist,
    'nama': 'TM Revanza Narendra Pradipta',
    'last_login': request.COOKIES.get('last_login'),
    }
    return render(request, "wishlist.html", context)

def show_xml(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('wishlist:login')
            
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("wishlist:show_wishlist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('wishlist:login'))
    response.delete_cookie('last_login')
    return response

def wishlist_ajax(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
    'list_barang': data_barang_wishlist,
    'nama': 'TM Revanza Narendra Pradipta',
    'last_login': request.COOKIES.get('last_login'),
    }
    return render(request, 'wishlist_ajax.html', context)

def create_wishlist(request):
    if request.method == "POST":
        nama_barang = request.POST.get('nama_barang')
        harga_barang = request.POST.get('nama_barang')
        deskripsi = request.POST.get('deskripsi')

        input_barang = BarangWishlist(
            nama_barang = nama_barang,
            harga_barang = harga_barang,
            deskripsi = deskripsi)
        
        input_barang.save()

        return HttpResponse(serializers.serialize("json", input_barang), content_type="application/json")

        