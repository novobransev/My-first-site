from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('biology/', views.biology, name='biology'),
    path('chemistry/', views.chemistry, name='chemistry'),
    path('english/', views.english, name='english'),
    path('history/', views.history, name='history'),
    path('information/', views.information, name='information'),
    path('literature/', views.literature, name='literature'),
    path('math/', views.math, name='math'),
    path('OBZ/', views.obz, name='OBZ'),
    path('OID/', views.oid, name='OID'),
    path('physics/', views.physics, name='physics'),
    path('russian_language/', views.russian_language, name='russian_language'),
    path('social_studies/', views.social_studies, name='social_studies'),
]

urlpatterns += static(settings.MEDIA_URL_ABS, document_root=settings.MEDIA_ROOT_ABS)