# Arkkitehtuurikuvaus

## Rakenne

Sovelluksen rakenne koostuu kuvassa olevista yhdeksästä luokasta. Näiden luokkien lisäksi sovellus sisältää pelikenttien taustat, pallon ja mailan, sekä äänitiedostot äänitehosteille.


![Luokkakaavio](./kuvat/apca_class_diagram.png)

Käyttöliittymän osia ovat luokat Mmenu ja score. Mmenu sisältää päävalikon, josta valitaan haluttu peli tai poistutaan pelistä. Score luokka hoitaa pisteisiin ja pelin päättymiseen liittyvät ilmoitukset.
 Mainprg luokka käynnistää ohjelman ja luo Mmenun ja huolehtii pelin käynnistämisestä ja alustaa spritet mailoille ja pallolle. Game luokka sisältää pelin pääsilmukan ja huolehtii näppäimistön lukemisesta ja näytön päivittämisestä. Se kutsuu Gamevents luokkaa pelin tapahtumien tarkistamiseksi. SoundEffects luokka huolehtii äänitehosteista Gameventsin pyyntöjen mukaisesti. Computer_ai luokkaa käytetään player vs. computer pelimoodissa, jolloin pelaaja 2 näppäimet ovat poistettu käytöstä.
 
## Toiminta

 Tämä sekvenssi diagrammi kuvaa sovelluksen toimintalogiikka pelaaja vastaan tietokone pelimoodissa.
 
 ![Sekvenssi diagrammi](./kuvat/pvc_seqdiag.png)
 
 
