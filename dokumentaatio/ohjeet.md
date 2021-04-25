# APCA
## Another pong clone again


### Asennus

Asenna pelin vaatimat riippuvuudet: 

```poetry install```

Peli käynnistyy komennolla: 

```poetry run invoke start```

## päävalikko
Päävalikossa valitaan hiirellä kaksinpeli, peli tietokonetta vastaan, against wall yksinpeli tai poistutaan pelistä.

## Pelaaminen
Pelaajan 1 (vasen pelaaja) näppäimet:

 - q - liikuta mailaa ylöspäin.
 - a - liikuta mailaa alaspäin.
 - s - lyö palloa / laukaise pallo.
 
Pelaajan 2 (oikea pelaaja) näppäimet:

 - Nuoli ylös - liikuta mailaa ylöspäin.
 - Nuoli alas - liikuta mailaa alaspäin.
 - Nuoli vasen - lyö palloa / laukaise pallo.
 
### kaksinpeli ja peli tietokonetta vastaan
Peli alkaa heti kun se käynnistetään. Pallo lähtee liikkeelle keskeltä satunnaiseen suuntaan. Pallon päästessä ulos kentältä peli pysähtyy, kunnes pelaaja, jonka päästä pallo karkasi, laukaisee pallon takaisin peliin. Palloa voi yrittää lyödä painamalla 's'- tai 'nuoli vasen'-näppäintä. Tämä siirtää mailaa eteenpäin. Mikäli lyönti osuu palloon, lisää se pallon nopeutta. Maila palautuu paikalleen seuraavasta ohjausliikkestä. Pallon nopeus ja suunta aina hieman satunnaisesti voi muuttua pallon osuessa mailaan.
 
Pelin päätyttyä, päävalikkoon palaudutaan, kun voittanut pelaaja painaa pallon laukaisunappia. Tietokoneen voittaessa pelin palaudutaan päävalikkoon 3s kuluessa.

### Yksinpeli
Yksinpelissä koitetaan pitää palloa kentällä. Pallon osuessa mailaan saa pisteen. Paras tulos jää muistiin. Pallo voi satunnaisesti hieman muuttaa suuntaa ja nopeutta osuessaan mailaan. Lyöntitoiminto ei ole käytössä yksinpelissä. Peli päättyy, kun pallo pääsee ulos kentältä.
 

