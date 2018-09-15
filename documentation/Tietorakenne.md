# Tietorakenteen kuvaus

Tässä dokumentissa kuvataan Lautapelikirppis-sivuston tietokantarakennetta ja sen teknistä toteutusta.

## Tietokantakaavio

Sovelluksen hyödyntämä tietokanta on kuvattu allaolevassa kaaviossa:

![Tietokantakaavio](https://github.com/AaaDee/Lautapelikirppis/tree/master/documentation/Tietokantakaavio.png "Tietokantakaavio")

Tietokanta muodostuu kolmesta tietosisältöä kuvaavasta taulusta (Myyntikohde, Käyttäjä ja Peli) sekä yhdestä liitostaulusta (Pelimyynti).

## Tietokantataulut

### Peli

Peli-taulussa ilmeisiä kenttiä ovat id-tunniste ja pelin nimi. Lisäksi mukana on pelin tunnus Boardgamegeek.com-sivustolla (BGG), joka mahdollistaa linkin lisäämisen kyseiselle sivustolle.

Peleihin liittyvä tietokantataulu on pidetty tarkoituksella mahdollisimman minimalistisena kahdesta syystä: Ensinnäkin, tämän sivuston tarkoitus on toimia kauppapaikkana eikä pelitietokantana, joten ylimääräisen tiedon kerääminen on sivuston ydintoiminnan kannalta toissijaista ja vaatii ylläpitäjältä tai käyttäjiltä ylimääräistä panostusta. Toiseksi BGG-sivusto tarjoaa jo nyt erittäin kattavasti tietoa lautapeleistä ja sillä on erittäin vakiintunut asema lautapeliyhteisössä, joten sivuston kokoamien tietojen hyödyntäminen on tässä yhteydessä tarkoituksenmukaisempaa toisteisen tai kilpailevan tietokokoelman kokoamisen sijaan.

### Käyttäjä

Kirjautumista varten käyttäjästä tarvitaan tieto nimimerkistä ja salasanasta (asiallisesti suojattuna). Kaupankäyntiä ja yhteydenpitoa varten tietokantaan lisätään myös käyttäjän sijainti ja sähköpostiosoite. Lisäksi mukana on tieto käyttäjän admin-statuksesta.

### Myyntikohde

Myyntikohteen keskeisiä tietoja ovat myyntihinta ja kohteen vapaamuotoinen kuvaus (joka voi sisältää tietoa esimerkiksi peli(e)n kunnosta tai toimitusehdoista). Mukana on myös tieto kohteen myyjästä viiteavaimen avulla.

Lisäksi kohteista pidetään yllä jonkin verran hallintatietoa: Mukana on tieto kohteen luomispäivästä ja sen mahdollisesta myyntipäivästä (joka on myymättömän kohteen tapauksessa tyhjä). Lisäksi pelin myyntistatuksesta (myyty/ei myyty) pidetään selkeyden vuoksi kirjaa erillisellä boolean-arvolla, vaikka tämän toki saisi selville myös myyntipäivän olemassaolon perusteella.

### Pelimyynti

Liitostaulu, jolla pelit ja myyntikohteet yhdistetään toisiinsa.



## CREATE TABLE -lausekkeet

### Peli

CREATE TABLE game (
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	bgg INTEGER NOT NULL, 
	PRIMARY KEY (id)
)


