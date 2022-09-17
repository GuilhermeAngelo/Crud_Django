from django.forms import ModelForm
from app.models import Carro

# Create the form class.
class CarrosForm(ModelForm):
    class Meta:
        model = Carro
        fields = ['nome', 'marca', 'cor']