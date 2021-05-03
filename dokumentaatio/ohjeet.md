# APCA
## Another pong clone again

Pong tyyppinen peli, jossa pelaaja tai pelaajat ohjaavat ruudun reunoilla olevia mailoja ja yrittävät estää ruudulla kimpoilevaa palloa karkaamasta ruudulta. Pelin voittaa se pelaaja, joka saa ensimmäisenä 5 pistettä.

## Asennus

Asenna pelin vaatimat riippuvuudet: 

```poetry install```

Peli käynnistyy komennolla: 

```poetry run invoke start```

## Päävalikko
Päävalikosta valitaan hiirellä kaksinpeli, peli tietokonetta vastaan, "Against the wall" yksinpeli, asetusvalikko tai poistutaan pelistä.

### Asetukset (Settings)
Valitse haluamasi asetukset ja tämän jälkeen valitse "Return to main menu". Asetukset tallentuvat automaattisesti ja ne ladataan, kun peli käynnistetään.

- Sound effects: Voit valita onko ääniefektit päällä tai pois päältä.

- Screen size: Valitse haluamasi peliruudun koko. Yksinpelissä ("Against the wall") jokaisella ruudunkoolla on oma HiScorensa. Mailojen ja pallon koot eivät muutu. Valittavana olevat ruudunkoot ovat:
    - small: 640 x 480 pikseliä
    - medium: 800 x 600 pikseliä
    - large: 1024 x 768 pikseliä
    
- Computer level: Valitse tietokoneen vaikeusaste: helppo- tai keskitaso.

### Pelaaminen
Pelaajan 1 (vasen pelaaja) näppäimet:

 - Q - liikuta mailaa ylöspäin.
 - A - liikuta mailaa alaspäin.
 - S - lyö palloa / laukaise pallo.
 
Pelaajan 2 (oikea pelaaja) näppäimet:

 - Nuoli ylös - liikuta mailaa ylöspäin.
 - Nuoli alas - liikuta mailaa alaspäin.
 - Nuoli vasen - lyö palloa / laukaise pallo.
 
### Kaksinpeli ja peli tietokonetta vastaan
Peli alkaa heti, kun se käynnistetään. Pallo lähtee liikkeelle keskeltä satunnaiseen suuntaan. Pallon päästessä ulos kentältä peli pysähtyy, kunnes pallon päästänyt pelaaja laukaisee pallon takaisin peliin. Palloa voi yrittää lyödä painamalla 's'- tai 'nuoli vasen'-näppäintä. Tämä siirtää mailaa eteenpäin. Mikäli lyönti osuu palloon, lisää se pallon nopeutta. Maila palautuu paikalleen seuraavasta ohjausliikkeestä. Pallon nopeus ja suunta hieman muuttuvat satunnaisesti pallon osuessa mailaan ja pallon nopeus voi myös laskea. Pelin voi keskeyttää sulkemalla ikkunan, jolloin palaudutaan päävalikkoon.
 
Päävalikkoon palaudutaan pelin päätyttyä, kun voittanut pelaaja painaa pallon laukaisunappia. Tietokoneen voittaessa pelin palaudutaan päävalikkoon 3s kuluessa.

### Yksinpeli
Yksinpelissä koitetaan pitää palloa kentällä. Pallon osuessa mailaan saa pisteen. Paras tulos jää muistiin. Pallo voi satunnaisesti hieman muuttaa suuntaa ja nopeutta osuessaan mailaan. Lyöntitoiminto ei ole käytössä yksinpelissä. Peli päättyy, kun pallo pääsee ulos kentältä, jonka jälkeen päävalikkoon palataan painamalla 's'. Pelin voi myös keskeyttää sulkemalla ikkunan, jolloin palataan takaisin päävalikkoon.
 

