from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.lista_eventos),
    path('', RedirectView.as_view(url='/agenda/')),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('register/', views.register_user),
    path('register/submit', views.submit_register),
    path('logout/', views.logout_user),
    path('agenda/evento/', views.evento),
    path('agenda/evento/submit/', views.submit_evento),
    path('agenda/evento/delete/<int:id_evento>/', views.delete_evento),
    path('agenda/lista/', views.json_lista_evento),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)