from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'), 
    path('index/', views.index, name='index'),
    path('lista_miembros/', views.lista_miembros, name='lista_miembros'),
    path('ver_edades/', views.ver_edades, name='ver_edades'),
    path('ver_escuela_dominical/', views.ver_escuela_dominical, name='ver_escuela_dominical'),
    path('detalle_miembro/<int:miembro_id>/', views.detalle_miembro, name='detalle_miembro'),
    path('registrar_miembro/', views.registrar_miembro, name='registrar_miembro'),
    path('editar_miembro/<int:miembro_id>/', views.editar_miembro, name='editar_miembro'),
    path('eliminar_miembro/<int:miembro_id>/', views.eliminar_miembro, name='eliminar_miembro'),
    path('miembros_genero/<str:genero>/', views.miembros_genero, name='miembros_genero'),
    path('miembros_fecha_conversion/<str:fecha_conversion>/', views.miembros_fecha_conversion, name='miembros_fecha_conversion'),
    path('miembros_fecha_bautizo/<str:fecha_bautizo>/', views.miembros_fecha_bautizo, name='miembros_fecha_bautizo'),
    path('miembros_estatus/<str:miembros_estatus>/', views.miembros_estatus, name='miembros_estatus'),
    path('miembros_ministerio/<int:ministerio_id>/', views.miembros_ministerio, name='miembros_ministerio'),
    path('miembros_sociedad/<str:sociedad>/', views.miembros_sociedad, name='miembros_sociedad'),
    path('miembros_edades/<int:edades_id>/', views.miembros_edades, name='miembros_edades'),
    path('miembros_escuela_dominical/<int:escuela_dominical_id>/', views.miembros_escuela_dominical, name='miembros_escuela_dominical'),
    path('servicio/', views.servicio, name='servicio'),
    path('agregar_servicio/', views.agregar_servicio, name='agregar_servicio'),
    path('editar_servicio/<int:servicio_id>/', views.editar_servicio, name='editar_servicio'),
    path('servicio/<int:servicio_id>/eliminar/', views.eliminar_servicio, name='eliminar_servicio'),
    path('actividade/', views.actividade, name='actividade'),
    path('agregar_actividade/', views.agregar_actividade, name='agregar_actividade'),
    path('editar_actividade/<int:actividade_id>/', views.editar_actividad, name='editar_actividad'),
    path('actividade/<int:actividade_id>/eliminar/', views.eliminar_actividad, name='eliminar_actividad'),
    path('socie/', views.socie, name='socie'),
    path('agregar_socie/', views.agregar_socie, name='agregar_socie'),
    path('editar_socie/<int:socie_id>/', views.editar_sociedad, name='editar_sociedad'),
    path('socie/<int:socie_id>/eliminar/', views.eliminar_sociedad, name='eliminar_sociedad'),
    path('minist/', views.minist, name='minist'),
    path('agregar_minist/', views.agregar_minist, name='agregar_minist'),
    path('editar_minist/<int:minist_id>/', views.editar_ministerio, name='editar_ministerio'),
    path('minist/<int:minist_id>/eliminar/', views.eliminar_ministerio, name='eliminar_ministerio'),
    path('esc_dom/', views.esc_dom, name='esc_dom'),
    path('agregar_esc_dom/', views.agregar_esc_dom, name='agregar_esc_dom'),
    path('editar_esc_dom/<int:esc_dom_id>/', views.editar_esc_dom, name='editar_esc_dom'),
    path('esc_dom/<int:esc_dom_id>/eliminar/', views.eliminar_esc_dom, name='eliminar_esc_dom'),
    path('contacto/', views.contacto, name='contacto'),
    path('ver_mensajes/', views.ver_mensajes, name='ver_mensajes'),
    path('mensaje/<int:mensaje_id>/eliminar/', views.eliminar_mensaje, name='eliminar_mensaje'),
    path('sobre_nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
    path('principal/', views.principal, name='principal'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),       
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
