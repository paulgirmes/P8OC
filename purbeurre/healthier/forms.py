from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class FoodQuery(forms.Form):

    fooditem=forms.CharField(   
            max_length=30,
            required=True,
            )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.form_id = self.auto_id
        self.helper.form_class = 'form-inline nav-search'
        self.helper.form_method = 'get'
        self.helper.form_action = "healthier:results"
        self.helper.add_input(Submit(self.auto_id, 'chercher'))

