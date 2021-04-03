from django.db import models

# Create your models here.


class Producent(models.Model):
    def __str__(self):
        return self.nazwa + " "

    nazwa = models.CharField(max_length=60)
    opis = models.TextField(blank=True)

    class Meta:
        verbose_name = "Producent"
        verbose_name_plural = "Producenci"


class Kategoria(models.Model):
    def __str__(self):
        return self.nazwa + " "

    nazwa = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"


class Produkty(models.Model):
    # todo by produkty wyswietlaly sie pod wlascwa nazwa
    def __str__(self):
        return self.nazwa + " "

    # todo by mozna bylo przypisac produkt do producenta
    # todo -> utworzenie relacji miedzy produktem i producentem w DB w modelu - dodanie tzw Klucza Obcego
    # todo Dodatkowe parametry:
    # todo - null=True - zezwolenie na puste pola (w DB istnieja juz produkty, a doszly nowe pola i DB nie wiedzialaby
    # todo czym je wypelnic co skutkowaloby bledami)
    # todo blank=True - pole nie jest obowiazkowe (nie bedzie napisane boldem jak pozostale)
    # todo - on_delete=models.CASCADE - definiuje co sie ma stac kiedy pole zostalyby skasowane
    kategoria = models.ForeignKey(Kategoria, null=True, blank=True, on_delete=models.CASCADE)
    producent = models.ForeignKey(Producent, on_delete=models.CASCADE, null=True)
    nazwa = models.CharField(max_length=100)    # todo = text field [HTML]
    opis = models.TextField(blank=True)  # todo = text area [HTML]
    cena = models.DecimalField(max_digits=12, decimal_places=2)

    # todo by nie tworzyla sie automatycznie angielska liczba mnoga (-s)
    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"
