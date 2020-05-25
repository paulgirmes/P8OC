from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.models import User
from django.contrib.auth import  password_validation, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.db.utils import IntegrityError
from django.forms import ModelForm, ValidationError
from .models import Food_item

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
        self.helper.add_input(Submit(self.auto_id, "chercher"))
        self.searched_food_item = False

    class Meta:
        model = Food_item
        fields = ("name")
    def get_searched_food_Item(self):
        self.cleaned_data.get("food_item")

class Signin(UserCreationForm):
    

    first_name = forms.CharField(required=True, label="prénom",widget=forms.TextInput())
    email = forms.EmailField(required=True, label="email")

    def __init__(self, request=None,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.form_action = "healthier:login"
        self.helper.add_input(Submit("Signin", "Créer Mon Compte"))
        self.user = None
        self.request = request

    class Meta:
        model = User
        fields = ["first_name", "email"]
    
    def save(self, commit=True):
        try:
            self.is_valid()
            self.clean_password2()
            user = super().save(commit=False)
        except:
            return self.errors
        user.username = user.email
        user.set_password(self.cleaned_data["password1"])
        try:
            if commit:
                user.save()
                self.user = user
                login(self.request, self.user)
                return True
        except IntegrityError:
            self.add_error('email', self.data["email"]+" est déjà utilisé par un autre compte, merci d'en utiliser un autre")
            return self.errors
        
    



class Login(AuthenticationForm):

    username = UsernameField(label="email",widget=forms.TextInput(attrs={'autofocus': True}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'GET'
        self.helper.form_action = "healthier:login"
        self.helper.add_input(Submit("Login", "Se connecter"))


    def log_user(self):
        try:
            self.is_valid()
            self.clean()
            login(self.request, self.get_user())
        except ValidationError as e:
            raise ValidationError("E-mail et/ou mot de passe invalides " +"("+str(e)+")")

