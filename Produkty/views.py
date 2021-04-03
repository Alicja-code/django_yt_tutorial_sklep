from django.shortcuts import render     # todo funkcja odpowiedzialna za wyswietlane HTML
from django.http import HttpResponse
from .models import Produkty, Kategoria

# Create your views here.


# todo Aby zamiast strony startowej Django wyswietlala sie lista produktow
# todo 'link' do tych widokow jest zapisany w urls.py
def index(request):
    kategorie = Kategoria.objects.all()
    dane = {'kategorie': kategorie}     # todo slownik laczy dane w HTML z obiektami django
    # todo do funkcji render przekazujemy nazwe pliku, ktory ma byc wyswietlany ('szablon') oraz slownik ('dane')
    return render(request, 'szablon.html', dane)


def kategoria(request, id):
    kategoria_user = Kategoria.objects.get(pk=id)
    kategoria_produkt = Produkty.objects.filter(kategoria=kategoria_user)
    kategorie = Kategoria.objects.all()
    dane = {
        'kategoria_user': kategoria_user,
        'kategoria_produkt': kategoria_produkt,
        'kategorie': kategorie,
    }
    return render(request, 'kategoria_produkt.html', dane)


def produkt(request, id):
    produkt_user = Produkty.objects.get(pk=id)
    kategorie = Kategoria.objects.all()
    dane = {'produkt_user': produkt_user, 'kategorie': kategorie}
    return render(request, 'produkt.html', dane)


# todo filtrowanie obiektow z DB - PRZYKLADY:
    # wszystkie = Produkty.objects.all()  # todo SELECT * FROM Produkty [SQL]
    # jeden = Produkty.objects.get(pk=6)  # todo pk - primary key w DB
    # kat = Produkty.objects.filter(kategoria=1)  # todo filter za pomoca dowolnego pola w modelu
    # producent = Produkty.objects.filter(producent=1)
    # kat_name = Kategoria.objects.get(id=1)
    # # todo produkty ktore maja pusta kategorie - trzeba zastosowac lookup
    # null = Produkty.objects.filter(kategoria__isnull=True)
    # # todo produkty ktore w opisie zawieraja fraze 'dysk', niezaleznie od wielkosci znakow - 'i-' w icontains
    # # todo trzeba zastosowac lookup
    # zawiera = Produkty.objects.filter(opis__icontains='dysk')

# todo OLD - anty-przyklad
# todo zmienna w ktorej polaczono kilka pol obiektu Produkt z HTML
    # napis = "<h1>" + str(produkt_user) + "</h1>" + \
    #         "<p>" + str(produkt_user.opis) + "</p>" + \
    #         "<p>" + str(produkt_user.cena) + " </p>"
