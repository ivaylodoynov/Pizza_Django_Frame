from django import forms

from Pizza_Django_Framework.pizza.models import Pizza

class CreatePizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = '__all__'

class EditPizzaForm(CreatePizzaForm):
    pass

class DeletePizzaForm(CreatePizzaForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'