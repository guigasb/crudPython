from django.forms import ModelForm
from cadastro.models import Meususer

class RegistroUsuario(ModelForm):
    class Meta:
        model = Meususer
        fields = ['id', 'nome', 'idade', 'curso', 'periodo']