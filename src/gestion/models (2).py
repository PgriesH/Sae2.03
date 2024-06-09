from django.db import models
from django.utils import timezone
from datetime import timedelta

class Aeroport(models.Model):
    id_aeroport = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=100)
    pays = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nom} ({self.pays})"

class Piste(models.Model):
    numero = models.IntegerField(primary_key=True)
    aeroport = models.ForeignKey(Aeroport, on_delete=models.CASCADE)
    longueur = models.IntegerField()

    def __str__(self):
        return f"Piste {self.numero} - {self.aeroport.nom}"

class Compagnie(models.Model):
    id_compagnie = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=100)
    description = models.TextField()
    pays_attache = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

class TypeAvion(models.Model):
    id_type_avion = models.IntegerField(primary_key=True)
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    description = models.TextField()
    longueur_piste_necessaire = models.IntegerField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f"{self.marque} {self.modele}"

class Avion(models.Model):
    id_avion = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=100)
    compagnie = models.ForeignKey(Compagnie, on_delete=models.CASCADE)
    modele = models.ForeignKey(TypeAvion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Vol(models.Model):
    id_vols = models.CharField(max_length=255, primary_key=True)
    avion = models.ForeignKey(Avion, on_delete=models.CASCADE)
    pilote = models.CharField(max_length=100)
    aeroport_depart = models.ForeignKey(Aeroport, related_name='depart_vols', on_delete=models.CASCADE)
    date_heure_depart = models.DateTimeField()
    aeroport_arrivee = models.ForeignKey(Aeroport, related_name='arrivee_vols', on_delete=models.CASCADE)
    date_heure_arrivee = models.DateTimeField()

    def __str__(self):
        return f"Vol de {self.aeroport_depart.nom} à {self.aeroport_arrivee.nom} le {self.date_heure_depart}"

    def piste_disponible(self):
        pistes = Piste.objects.filter(aeroport=self.aeroport_arrivee)
        for piste in pistes:
            vols = Vol.objects.filter(aeroport_arrivee=self.aeroport_arrivee, date_heure_arrivee__gte=self.date_heure_arrivee - timedelta(minutes=10), date_heure_arrivee__lte=self.date_heure_arrivee + timedelta(minutes=10))
            if not vols.exists():
                return piste
        return None

    def proposer_nouvel_horaire(self):
        increment = timedelta(minutes=10)
        nouvelle_date_heure_arrivee = self.date_heure_arrivee + increment
        while True:
            vols = Vol.objects.filter(aeroport_arrivee=self.aeroport_arrivee, date_heure_arrivee__gte=nouvelle_date_heure_arrivee - timedelta(minutes=10), date_heure_arrivee__lte=nouvelle_date_heure_arrivee + increment)
            if not vols.exists():
                return nouvelle_date_heure_arrivee
            nouvelle_date_heure_arrivee += increment
            
