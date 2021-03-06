# <H1 align="center">FOOD SWAPPER</h1>

<h4 align="center">A WEB application that allows users to search for healthier food replacements, built with 
<a href="https://www.djangoproject.com/" target="_blank">Django</a>.</h4>

<a href="https://openclassrooms.com/fr/paths/68-developpeur-dapplication-python"><h5 align="center">Programmed for the project 8 of OpenClassrooms Python developper certificate<h5></a>

## Demo

👉 Watch it <a href="https://healthier-food.herokuapp.com/">here</a>.

### Using

Open a navigator and go to the demo URL.
Write in one of the search forms a food nome that you would like to replace with an healthier one.
If healthier replacements are found they will be displayed, you will the be able to look at one food item datas in particular and save it to your favorites if logged-in.
You have the possibility to create a personnal account to be able to retrieve your favorites food items.

## For developers

* Clone the app directory

* Install Python3 on your computer if you are running a Windows environment.

* Install the dependencies with Pipenv from Pipfile

* this project works with a PostGreSQL engine so install it if deployed locally

* update purbeurre.settings with database credentials

* execute manage.py makemigrations followed by manage.py migrate

* execute manage.py populate_db if you want to add data fro open food facts into your PGSQL database

* either run manage.py runserver for debug or deploy elewere as needed (originaly inteded to be deployed with  Heroku)

## Built with

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://github.com/maxogden/menubar)
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/#)
- and a lot more ...!

## Credits

- [All Fodd data provided by Open Food Facts](https://fr.openfoodfacts.org/)
- [website template by ](https://github.com/BlackrockDigital/startbootstrap-creative)
- [home background photo by Kawin Harasai](https://unsplash.com/photos/k60JspcBwKE)
- [nutriscore vectors by vecteezy]("https://fr.vecteezy.com/vecteur-libre/aliment")
- and countless unnamed contributors from the all the Python community without whose this project would not have been possible. Thanks to you all !

## Author

**Paul Girmes** - *Initial work*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details