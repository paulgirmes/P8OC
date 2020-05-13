from django import forms

class FoodQuery(forms.Form):
    fooditem=forms.CharField(
        label="query",
        widget=forms.TextInput(attrs={'class': 'form-control'}),   
        max_length=30,
        required=True,
        empty_value="aliment à remplacer"
        )
