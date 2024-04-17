from django.urls import path
from .views import home, eventos, exit, signup, create_event, delete_event, edit_event, rendimiento, inscripcion, actualizar_usuario_ins

urlpatterns = [
    path('', home, name='home'),
    path('eventos/', eventos, name='eventos'),
    path('logout/', exit, name='exit'),
    path('signup/', signup, name='signup'),
    path('new_event/', create_event, name='create_event'),
    path('delete_event/<int:id>', delete_event, name="delete_event"),
    path('edit_event/<int:id>', edit_event, name="edit_event"),
    # path('cargar_user/<str:codigo>', cargar_user, name="cargar_user"),
    path('rendimiento/',rendimiento,name="rendimiento"),
    path('inscripcion/',inscripcion,name="inscripcion"),
    path('actualizar_usuario_ins/',actualizar_usuario_ins,name="actualizar_usuario_ins"),



] 