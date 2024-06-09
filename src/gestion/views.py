from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Aeroport, Piste, Compagnie, TypeAvion, Avion, Vol
from .forms import AeroportForm, PisteForm, CompagnieForm, TypeAvionForm, AvionForm, VolForm
from datetime import datetime
from django.contrib import messages
import csv
from django.db.models import Q
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph


# Vue pour la page d'accueil
def home(request):
    return render(request, 'gestion/home.html')

# Vues pour les aéroports
def list_aeroports(request):
    aeroports = Aeroport.objects.all()
    return render(request, 'gestion/aeroports/list_aeroports.html', {'aeroports': aeroports})

def create_aeroport(request):
    if request.method == 'POST':
        form = AeroportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_aeroports')
    else:
        form = AeroportForm()
    return render(request, 'gestion/aeroports/form_aeroport.html', {'form': form})

def update_aeroport(request, pk):
    aeroport = get_object_or_404(Aeroport, pk=pk)
    if request.method == 'POST':
        form = AeroportForm(request.POST, instance=aeroport)
        if form.is_valid():
            form.save()
            return redirect('list_aeroports')
    else:
        form = AeroportForm(instance=aeroport)
    return render(request, 'gestion/aeroports/form_aeroport.html', {'form': form})

def delete_aeroport(request, pk):
    aeroport = get_object_or_404(Aeroport, pk=pk)
    aeroport.delete()
    return redirect('list_aeroports')

def detail_aeroport(request, pk):
    aeroport = get_object_or_404(Aeroport, pk=pk)
    return render(request, 'gestion/aeroports/detail_aeroport.html', {'aeroport': aeroport})

# Vues pour les pistes

def list_pistes(request):
    pistes = Piste.objects.all()
    return render(request, 'gestion/pistes/list_pistes.html', {'pistes': pistes})

def create_piste(request):
    if request.method == 'POST':
        form = PisteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_pistes')
    else:
        form = PisteForm()
    return render(request, 'gestion/pistes/form_piste.html', {'form': form})

def update_piste(request, pk):
    piste = get_object_or_404(Piste, pk=pk)
    if request.method == 'POST':
        form = PisteForm(request.POST, instance=piste)
        if form.is_valid():
            form.save()
            return redirect('list_pistes')
    else:
        form = PisteForm(instance=piste)
    return render(request, 'gestion/pistes/form_piste.html', {'form': form})

def delete_piste(request, pk):
    piste = get_object_or_404(Piste, pk=pk)
    piste.delete()
    return redirect('list_pistes')

def detail_piste(request, pk):
    piste = get_object_or_404(Piste, pk=pk)
    return render(request, 'gestion/pistes/detail_piste.html', {'piste': piste})

# Vues pour les compagnies
def list_compagnies(request):
    compagnies = Compagnie.objects.all()
    return render(request, 'gestion/compagnies/list_compagnies.html', {'compagnies': compagnies})

def create_compagnie(request):
    if request.method == 'POST':
        form = CompagnieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_compagnies')
    else:
        form = CompagnieForm()
    return render(request, 'gestion/compagnies/form_compagnie.html', {'form': form})

def update_compagnie(request, pk):
    compagnie = get_object_or_404(Compagnie, pk=pk)
    if request.method == 'POST':
        form = CompagnieForm(request.POST, instance=compagnie)
        if form.is_valid():
            form.save()
            return redirect('list_compagnies')
    else:
        form = CompagnieForm(instance=compagnie)
    return render(request, 'gestion/compagnies/form_compagnie.html', {'form': form})

def delete_compagnie(request, pk):
    compagnie = get_object_or_404(Compagnie, pk=pk)
    compagnie.delete()
    return redirect('list_compagnies')

def detail_compagnie(request, pk):
    compagnie = get_object_or_404(Compagnie, pk=pk)
    return render(request, 'gestion/compagnies/detail_compagnie.html', {'compagnie': compagnie})

# Vues pour les types d'avions

def list_types_avions(request):
    type_avions = TypeAvion.objects.all()
    return render(request, 'gestion/types_avions/list_type_avions.html', {'type_avions': type_avions})

def create_type_avion(request):
    if request.method == 'POST':
        form = TypeAvionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_types_avions') 
    else:
        form = TypeAvionForm()
    return render(request, 'gestion/types_avions/form_type_avion.html', {'form': form})

def update_type_avion(request, pk):
    type_avion = get_object_or_404(TypeAvion, pk=pk)
    if request.method == 'POST':
        form = TypeAvionForm(request.POST, request.FILES, instance=type_avion)
        if form.is_valid():
            form.save()
            return redirect('list_types_avions')
    else:
        form = TypeAvionForm(instance=type_avion)
    return render(request, 'gestion/types_avions/form_type_avion.html', {'form': form, 'type_avion': type_avion})

def delete_type_avion(request, pk):
    type_avion = get_object_or_404(TypeAvion, pk=pk)
    type_avion.delete()
    return redirect('list_types_avions')

def detail_type_avion(request, pk):
    type_avion = get_object_or_404(TypeAvion, pk=pk)
    return render(request, 'gestion/types_avions/detail_type_avion.html', {'type_avion': type_avion})

# Vues pour les avions
def list_avions(request):
    avions = Avion.objects.all()
    return render(request, 'gestion/avions/list_avions.html', {'avions': avions})

def create_avion(request):
    if request.method == 'POST':
        form = AvionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_avions')
    else:
        form = AvionForm()
    return render(request, 'gestion/avions/form_avion.html', {'form': form})

def update_avion(request, pk):
    avion = get_object_or_404(Avion, pk=pk)
    if request.method == 'POST':
        form = AvionForm(request.POST, instance=avion)
        if form.is_valid():
            form.save()
            return redirect('list_avions')
    else:
        form = AvionForm(instance=avion)
    return render(request, 'gestion/avions/form_avion.html', {'form': form})

def delete_avion(request, pk):
    avion = get_object_or_404(Avion, pk=pk)
    avion.delete()
    return redirect('list_avions')

def detail_avion(request, pk):
    avion = get_object_or_404(Avion, pk=pk)
    return render(request, 'gestion/avions/detail_avion.html', {'avion': avion})

# Vues pour les vols

def list_vols(request):
    vols = Vol.objects.all()
    return render(request, 'gestion/vols/list_vols.html', {'vols': vols})

def create_vol(request):
    if request.method == 'POST':
        form = VolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_vols')
    else:
        form = VolForm()
    return render(request, 'gestion/vols/form_vol.html', {'form': form})

def update_vol(request, pk):
    vol = get_object_or_404(Vol, pk=pk)
    if request.method == 'POST':
        form = VolForm(request.POST, instance=vol)
        if form.is_valid():
            form.save()
            return redirect('list_vols')
    else:
        form = VolForm(instance=vol)
    return render(request, 'gestion/vols/form_vol.html', {'form': form})

def delete_vol(request, pk):
    vol = get_object_or_404(Vol, pk=pk)
    vol.delete()
    return redirect('list_vols')

def detail_vol(request, pk):
    vol = get_object_or_404(Vol, pk=pk)
    return render(request, 'gestion/vols/detail_vol.html', {'vol': vol})

# import des vols 

def import_vols(request):
    if request.method == 'POST':
        try:
            myfile = request.FILES['myfile']
        except MultiValueDictKeyError:
            messages.error(request, "Veuillez sélectionner un fichier avant de soumettre.")
            return redirect('list_vols')

        decoded_file = myfile.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        
        required_fields = ['avion_id', 'pilote', 'aeroport_depart_id', 'date_heure_depart', 'aeroport_arrivee_id', 'date_heure_arrivee']
        
        for row in reader:
            missing_fields = [field for field in required_fields if field not in row]
            if missing_fields:
                messages.error(request, f"Le fichier CSV ne contient pas toutes les colonnes nécessaires. Manquantes: {', '.join(missing_fields)}")
                return redirect('list_vols')
            
            try:
                avion = Avion.objects.get(id=row['avion_id'])
                aeroport_depart = Aeroport.objects.get(id=row['aeroport_depart_id'])
                aeroport_arrivee = Aeroport.objects.get(id=row['aeroport_arrivee_id'])
                date_heure_depart = datetime.fromisoformat(row['date_heure_depart'])
                date_heure_arrivee = datetime.fromisoformat(row['date_heure_arrivee'])

                Vol.objects.create(
                    avion=avion,
                    pilote=row['pilote'],
                    aeroport_depart=aeroport_depart,
                    date_heure_depart=date_heure_depart,
                    aeroport_arrivee=aeroport_arrivee,
                    date_heure_arrivee=date_heure_arrivee
                )
            except (Avion.DoesNotExist, Aeroport.DoesNotExist) as e:
                messages.error(request, f"Erreur d'importation: {e}")
                return redirect('list_vols')
            except ValueError as e:
                messages.error(request, f"Erreur de format de date: {e}")
                return redirect('list_vols')

        messages.success(request, "Les vols ont été importés avec succès.")
        return redirect('list_vols')
    else:
        messages.error(request, "Erreur lors de l'importation. Veuillez réessayer.")
        return redirect('list_vols')

def vol_fiche(request):
    aeroport_depart_id = request.GET.get('aeroport_depart_id')
    aeroport_arrivee_id = request.GET.get('aeroport_arrivee_id')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    export = request.GET.get('export')

    vols = Vol.objects.all()
    if aeroport_depart_id:
        vols = vols.filter(aeroport_depart_id=aeroport_depart_id)
    if aeroport_arrivee_id:
        vols = vols.filter(aeroport_arrivee_id=aeroport_arrivee_id)
    if start_date and end_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        vols = vols.filter(date_heure_depart__range=[start_date, end_date])

    if export == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="vols.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['avion_id', 'pilote', 'aeroport_depart_id', 'date_heure_depart', 'aeroport_arrivee_id', 'date_heure_arrivee'])
        
        for vol in vols:
            writer.writerow([vol.avion.id, vol.pilote, vol.aeroport_depart.id, vol.date_heure_depart.isoformat(), vol.aeroport_arrivee.id, vol.date_heure_arrivee.isoformat()])
        
        return response
    
    if export == 'pdf':
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="vols.pdf"'
        
        doc = SimpleDocTemplate(response, pagesize=A4)
        elements = []
        
        styles = getSampleStyleSheet()
        title = Paragraph("Fiche des Vols", styles['Title'])
        elements.append(title)
        
        data = [['Avion', 'Pilote', 'Départ', 'Arrivée', 'Date de Départ', 'Date d\'Arrivée']]
        for vol in vols:
            data.append([
                vol.avion.nom,
                vol.pilote,
                vol.aeroport_depart.nom,
                vol.aeroport_arrivee.nom,
                vol.date_heure_depart.strftime('%Y-%m-%d %H:%M'),
                vol.date_heure_arrivee.strftime('%Y-%m-%d %H:%M')
            ])
        
        table = Table(data, hAlign='CENTER')
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        elements.append(table)
        
        doc.build(elements)
        return response
    
    aeroports = Aeroport.objects.all()
    return render(request, 'gestion/vols/vol_fiche.html', {'vols': vols, 'aeroports': aeroports})

    