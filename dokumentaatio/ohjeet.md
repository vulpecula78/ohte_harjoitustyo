# APCA
## Another pong clone again


### Asennus

Asenna pelin vaatimat riippuvuudet: 

```poetry install```

Peli käynnistyy komennolla: 

```poetry run invoke start```

### päävalikko
Päävalikossa valitaan hiirellä kaksinpeli, peli tietokonetta vastaan, against wall yksinpeli tai poistutaan pelistä.

### Pelaaminen
Pelaajan 1 (vasen pelaaja) näppäimet:

 - q - liikuta mailaa ylöspäin.
 - a - liikuta mailaa alaspäin.
 - s - lyö palloa / laukaise pallo.
 
Pelaajan 2 (oikea pelaaja) näppäimet:

 - Nuoli ylös - liikuta mailaa ylöspäin.
 - Nuoli alas - liikuta mailaa alaspäin.
 - Nuoli vasen - lyö palloa / laukaise pallo.
 
 Tällä hetkellä peli alkaa heti kun se käynnistetään. Pallon päästessä ulos kentältä peli pysähtyy, kunnes pelaaja, jonka päästä pallo karkasi, laukaisee pallon takaisin peliin. Palloa voi yrittää lyödä painamalla 's'- tai 'nuoli vasen'-näppäintä. Tämä siirtää mailaa eteenpäin. Mikäli lyönti osuu palloon, lisää se pallon nopeutta. Maila palautuu paikalleen seuraavasta ohjausliikkestä. 
 
Pelin päätyttyä, päävalikkoon palaudutaan, kun voittanut pelaaja painaa pallon laukaisunappia. Tietokoneen voittaessa pelin palaudutaan päävalikkoon 3s kuluessa.

Yksinpelissä pisteet lasketaan pallon osuessa mailaan. Parhaat pisteet jää muistiin. Yksin pelissä pallon lyönti toiminto ei ole käytössä. Peli päättyy, mikäli pallo pääsee ulos kentältä.
 

