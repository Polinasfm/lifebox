# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings

from cadastro.models import Equipamento, Caixa, Hospital, Viagem
from cadastro.forms import EquipamentoForm, CaixaForm, HospitalForm, ViagemForm

###################################################################################################
# Cadastro de Equipamentos:
@login_required
def equipamento_pesquisar(request):    
    # Filtra os equipamentos:
    try:
        search = request.GET.get('search')
        equipamentos_list = Equipamento.objects.filter(nome__contains=search)
    except ValueError:
        equipamentos_list = Equipamento.objects.all()
    
    # Cria um paginador e seleciona a página que será exibida:
    paginator = Paginator(equipamentos_list, settings.CUSTOM_ITENS_POR_PAGINAS_TABELAS)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    
    # Retorna os itens da página correta:
    try:
        equipamentos = paginator.page(page)
    except (EmptyPage, InvalidPage):
        equipamentos = paginator.page(paginator.num_pages)
        
    return render(request,
                  'equipamento/pesquisa.html',
                  {'equipamentos': equipamentos})


@login_required
def equipamento_criar(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            equipamento = form.save(commit=False)
            equipamento.save()
            return redirect('equipamento_pesquisar')
    else:
        form = EquipamentoForm()
    return render(request, 'equipamento/formulario.html', {'form': form})

@login_required
def equipamento_editar(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == "POST":
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            equipamento = form.save(commit=False)
            equipamento.save()
            return redirect('equipamento_pesquisar')
    else:
        form = EquipamentoForm(instance=equipamento)
    return render(request, 'equipamento/formulario.html', {'form': form})


###################################################################################################
# Cadastro de Caixas:
@login_required
def caixa_pesquisar(request):
    # Filtra as caixas:
    try:
        search = request.GET.get('search')
        caixas_list = Caixa.objects.filter(informacaoAdicional__contains=search)
    except ValueError:
        caixas_list = Caixa.objects.all()
    
    # Cria um paginador e seleciona a página que será exibida:
    paginator = Paginator(caixas_list, settings.CUSTOM_ITENS_POR_PAGINAS_TABELAS)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    
    # Retorna os itens da página correta:
    try:
        caixas = paginator.page(page)
    except (EmptyPage, InvalidPage):
        caixas = paginator.page(paginator.num_pages)
        
    return render(request,
                  'caixa/pesquisa.html',
                  {'caixas': caixas})


@login_required
def caixa_criar(request):
    if request.method == 'POST':
        form = CaixaForm(request.POST)
        if form.is_valid():
            caixa = form.save(commit=False)
            caixa.save()
            return redirect('caixa_pesquisar')
    else:
        form = CaixaForm()
    return render(request, 'caixa/formulario.html', {'form': form})


@login_required
def caixa_editar(request, pk):
    caixa = get_object_or_404(Caixa, pk=pk)
    if request.method == "POST":
        form = CaixaForm(request.POST, instance=caixa)
        if form.is_valid():
            caixa = form.save(commit=False)
            caixa.save()
            return redirect('caixa_pesquisar')
    else:
        form = CaixaForm(instance=caixa)
    return render(request, 'caixa/formulario.html', {'form': form})

###################################################################################################
# Cadastro de Hospitais:
@login_required
def hospital_pesquisar(request):
    # Filtra os hospitais:
    try:
        search = request.GET.get('search')
        hospitais_list = Hospital.objects.filter(nome__contains=search)
    except ValueError:
        hospitais_list = Hospital.objects.all()
    
    # Cria um paginador e seleciona a página que será exibida:
    paginator = Paginator(hospitais_list, settings.CUSTOM_ITENS_POR_PAGINAS_TABELAS)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    
    # Retorna os itens da página correta:
    try:
        hospitais = paginator.page(page)
    except (EmptyPage, InvalidPage):
        hospitais = paginator.page(paginator.num_pages)
        
    return render(request,
                  'hospital/pesquisa.html',
                  {'hospitais': hospitais})


@login_required
def hospital_criar(request):
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('hospital_pesquisar')
    else:
        form = HospitalForm()
    return render(request, 'hospital/formulario.html', {'form': form})

@login_required
def hospital_editar(request, pk):
    item = get_object_or_404(Hospital, pk=pk)
    if request.method == "POST":
        form = HospitalForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('hospital_pesquisar')
    else:
        form = HospitalForm(instance=item)
    return render(request, 'hospital/formulario.html', {'form': form})

###################################################################################################
# Cadastro de Viagens:
@login_required
def viagem_pesquisar(request):
    viagens = Viagem.objects.all()
    return render(request, 'viagem/pesquisa.html', {'viagens': viagens})


@login_required
def viagem_criar(request):
    if request.method == 'POST':
        form = ViagemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('viagem_pesquisar')
    else:
        form = ViagemForm()
    return render(request, 'viagem/formulario.html', {'form': form})

@login_required
def viagem_editar(request, pk):
    item = get_object_or_404(Viagem, pk=pk)
    if request.method == "POST":
        form = ViagemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('viagem_pesquisar')
    else:
        form = ViagemForm(instance=item)
    return render(request, 'viagem/formulario.html', {'form': form})
