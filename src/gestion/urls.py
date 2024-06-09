from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    
    path('aeroports/', views.list_aeroports, name='list_aeroports'),
    path('aeroports/add/', views.create_aeroport, name='add_aeroport'),
    path('aeroports/edit/<int:pk>/', views.update_aeroport, name='edit_aeroport'),
    path('aeroports/delete/<int:pk>/', views.delete_aeroport, name='delete_aeroport'),
    path('aeroports/view/<int:pk>/', views.detail_aeroport, name='view_aeroport'),

    path('pistes/', views.list_pistes, name='list_pistes'),
    path('pistes/add/', views.create_piste, name='add_piste'),
    path('pistes/edit/<int:pk>/', views.update_piste, name='edit_piste'),
    path('pistes/delete/<int:pk>/', views.delete_piste, name='delete_piste'),
    path('pistes/view/<int:pk>/', views.detail_piste, name='view_piste'),
    
    path('compagnies/', views.list_compagnies, name='list_compagnies'),
    path('compagnies/add/', views.create_compagnie, name='add_compagnie'),
    path('compagnies/edit/<int:pk>/', views.update_compagnie, name='edit_compagnie'),
    path('compagnies/delete/<int:pk>/', views.delete_compagnie, name='delete_compagnie'),
    path('compagnies/view/<int:pk>/', views.detail_compagnie, name='view_compagnie'),
    
    path('types_avions/', views.list_types_avions, name='list_types_avions'),
    path('types_avions/add/', views.create_type_avion, name='add_type_avion'),
    path('types_avions/edit/<int:pk>/', views.update_type_avion, name='edit_type_avion'),
    path('types_avions/confirm_delete/<int:pk>/', views.delete_type_avion, name='delete_type_avion'),
    path('types_avions/view/<int:pk>/', views.detail_type_avion, name='view_type_avion'),
    
    path('avions/', views.list_avions, name='list_avions'),
    path('avions/add/', views.create_avion, name='add_avion'),
    path('avions/edit/<int:pk>/', views.update_avion, name='edit_avion'),
    path('avions/delete/<int:pk>/', views.delete_avion, name='delete_avion'),
    path('avions/view/<int:pk>/', views.detail_avion, name='view_avion'),

    path('vols/', views.list_vols, name='list_vols'),
    path('vols/add/', views.create_vol, name='add_vol'),
    path('vols/edit/<int:pk>/', views.update_vol, name='edit_vol'),
    path('vols/delete/<int:pk>/', views.delete_vol, name='delete_vol'),
    path('vols/view/<int:pk>/', views.detail_vol, name='view_vol'),
    
    path('vol_fiche/', views.vol_fiche, name='vol_fiche'),    
    path('import_vols/', views.import_vols, name='import_vols'),
]

