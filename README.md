# Ohjemointitekniikan harjoitustyö

## APCA eli Another pong clone again

Sovellus on klassisen pong pelin klooni. Pelissä pelaajat ohjaavat mailoja, joilla he koittavat pitää pallon kentällä. Mikäli pallo lentää vastustajan päästä ulos, saa pelaaja pisteen. Voit pelata kaksinpeliä tai tietokonetta vastaan. 

### Pelin asennus

Lataa uusin julkaisu: 

 - [Viikko6 release](https://github.com/vulpecula78/ohte_harjoitustyo/releases/tag/Viikko6)
 
tai kloonaa repositorio.

Suorita riippuvuuksien asennus komennolla:

```
poetry install
```

Peli käynnistyy komennolla:

```
poetry run invoke start
```

Sovellus on tehty ja testattu python 3.8.8 versiolla. Sovellusta on myös testattu python versiolla 3.6.9.

### Pelaaminen
Pelissä on tällä hetkellä mahdollisuus kaksinpeliin tai tietokonetta vastaan. Vasen pelaaja ohjaa mailaa näppäimistä q ja z. Oikea pelaajaa ohjaa mailaa nuolinäppäimistä. Tietokone on aina oikeanpuoleinen pelaaja. Pallon lentäessä ulos kentältä, peli pysähtyy, kunnes pelaaja, jonka päästä pallo lensi ulos, laukaisee pallon takaisin kentälle. Vasen pelaaja näppäimestä a ja oikea pelaaja näppäimestä nuoli vasemmalle. Pallon nopeus ja suunta voivat muuttua aina mailaan osuessaan. Peli päättyy kun jompikumpi pelaaja saa 5 pistettä. Takaisin päävalikkoon pääsee painamalla laukaisunappia (a tai nuoli vas.). Pelin asetuksia (ruudunkoko, äänet ja vaikeusaste) voi muuttaa.

### Dokumentaatio
 1. [Pelin ohjeet](https://github.com/vulpecula78/ohte_harjoitustyo/blob/master/dokumentaatio/ohjeet.md)
 1. [Määrittelydokumentti](https://github.com/vulpecula78/ohte_harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
 1. [Arkkitehtuurikuvaus](https://github.com/vulpecula78/ohte_harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
 1. [Työaikakirjanpito](https://github.com/vulpecula78/ohte_harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
 1. [Sovelluksen testaus](https://github.com/vulpecula78/ohte_harjoitustyo/blob/master/dokumentaatio/Sovelluksen_testaus.md)

### Testaus

Sovelluksen testit ajetaan komennolla:

```
poetry run invoke test
```

Testiraportti tulostuu komennolla:

```
poetry run invoke coverage-report
```

Testiraportin voi myös tehdä selaimella tarkasteltavaksi komennolla:

```
poetry run invoke coverage-html
```

Tämä luo raportin hakemistoon htmlcov.

```coverage-report ``` tai ```coverage-html``` suoritettaessa ei ole tarvetta suorittaa ```"poetry run invoke test"``` erikseen.

### Koodin tarkastus

 Pylint tarkastukset suoritetaan komennolla:

```
poetry run invoke lint
```

pylint: disable=no-member käytetty mmenu, mainprg ja game.py sellaisilla riveillä, joissa luetaan näppäimistöä tai hiirtä, sekä pygame.init(). Wait.py rivillä 3 pylint: disable=no-name-in-module. Pylint ei nähtävästi osaa käsitellä näitä rivejä.
