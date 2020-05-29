from random import choice
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.models import User
from django.contrib.auth import  password_validation, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.db.utils import IntegrityError
from django.forms import ModelForm, ValidationError
from .models import Food_item
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist

class FoodQuery(forms.Form):

    name=forms.CharField(
            required=True,
            )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_id = self.auto_id
        self.helper.form_class = 'col-xs-10 col-sm-8 col-md-6 justify-content-center form-inline nav-search'
        self.helper.form_method = 'get'
        self.helper.form_action = "healthier:results"
        self.helper.add_input(Submit(self.auto_id, "chercher"))
        self.helper.form_error_title = "Oooops!"
        self.food_item = None
        self.replacement_foods = None

    class Meta():
        model = Food_item
        fields = ['name',]

    def get_searched_food_Item(self):
        if self.is_valid():
            Items_found = self.search()
            if Items_found == 1:
                if self.replace():
                    return 1
                else:
                    self.add_error(None, "il n'existe pas d'aliments de remplacement plus sain dans notre base de donnée")
                    return False
            elif Items_found > 1:
                self.add_error(None, "Il existe " + str(Items_found)+
                                " aliments contenant '"+self.cleaned_data.get("name")+"'"
                                " merci de préciser votre recherche"
                                )
                return Items_found
            elif Items_found == 0:
                self.add_error(None, self.cleaned_data.get("name") + " est introuvable dans notre liste d'aliments ! Merci de renouveller votre recherche")
                return False
        else:
            self.add_error(None,"Champ Invalide")
            return False

    def search(self):
        try:
            f = Food_item.objects.get(name__icontains=self.cleaned_data.get("name"))
            self.food_item = f
            return 1
        except MultipleObjectsReturned:
            f = Food_item.objects.filter(name__icontains=self.cleaned_data.get("name"))
            self.food_item = f
            return f.all().count()
        except ObjectDoesNotExist:
            try:
                f = Food_item.objects.get(name__istartswith=self.cleaned_data.get("name").split()[0])
                self.food_item = f
                return 1
            except MultipleObjectsReturned:
                f = Food_item.objects.filter(name__istartswith=self.cleaned_data.get("name").split()[0])
                self.food_item = f
                return f.all().count()
            except ObjectDoesNotExist:
                return 0

  
    def replace(self):
        categories = list(self.food_item.categories.all())

        replacements = {Food_item.objects.filter(categories__name=category,
                                                nutri_score_fr__lt=self.food_item.nutri_score_fr,
                                                nova_grade__lt=self.food_item.nova_grade,
                                                ).order_by("nutri_score_fr", "nova_grade") for category in categories}
        query=[]
        {query.append(replacement) for replacement in replacements if replacement.exists()}
        cat_number = len(query)
        results=[]
        if cat_number > 0:
            self.replacement_foods = query[0]
            if cat_number > 1:
                i=0
                while i < cat_number-2:
                    intersect=query[i].intersection(query[i+1])
                    if intersect.exists():
                        results.append(intersect)
                    i+=1
                if len(results) > 0:
                    self.replacement_foods=results[0]
                    x = 0
                    results_choices=[]
                    if len(results) > 1:
                        while x < len(results)-2:
                            result=results[x].intersection(results[x+1])
                            if result.exists():
                                results_choices.append(result)
                            x+=1
                        if len(results_choices) > 0:
                                self.replacement_foods = choice(results_choices)
                                return True
                        else:
                            return True
                    else:
                        return True
                else:
                    return True   
            else:
                return True
        else:
            return False
        

                    
            

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

