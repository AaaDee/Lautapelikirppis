# Loppukatsaus

Projekti on nyt arvioinnin ja aikataulun kannalta paketissa. Sovellus täyttää keskeiset käyttötapaukset, ja taustalla olevat tietokannat pyörivät pääosin niin kuin pitääkin. Projektista jäi kuitenkin muutamia osa-alueita toteuttamatta ja joitakin outouksia jäljelle, joista on hyvä mainita tässä yhteydessä. Lisäksi suhteutan työn arvostelukriteerien minimivaatimuksiin (luonnollisesti ottamatta kantaa itse lopulliseen arvosanaan tai pisteytykseen).

## Puutteet ja outoudet

Ehkä keskeisin sovelluksen puute on tällä hetkellä se, että sen ulkoasu on todella askeettinen. Bootstrap-kirjasto on käytössä yläpalkin osalta, mutta sitä ei ole viety kaikkialle sovellukseen. Toisaalta sovelluksen keskeinen toiminnallisuus on saavutettavissa ja käytettävissä, joten toivottavasti karuus ei ulotu liikaa itse toiminnallisuuden tielle.

Näkymien sivutusta ei myöskään ole valitettavasti vielä toteutettu.

Lisäksi tunnustan, että pelien ja myyntikohteiden yhteys on hieman kummallinen. Halusin toisaalta, että myyntikohteissa voi olla useampi peli, mutta toisaalta, että yksittäisten pelien myyntidatasta pidetään kirjaa. Toteutettu ratkaisu on nyt näiden näkökulmien kompromissi.

Lisäksi myyntikohteiden muokkaaminen on paikoitellen hieman hankalaa, koska sovellus pyrkii välttämään tilanteita, jossa kohteessa ei olisi yhtään peliä. Jatkokehityksessä ajattelin ratkaista ongelman evästepohjaisen ratkaisun avulla, jossa kaikki muutokset kerätään yhteen transaktioon, jonka oikeellisuus tarkastetaan kerralla ja viedään tietokantaan vasta tämän tarkistuksen jälkeen.

## 5-arvosanan minimivaatimukset
Ennen varsinaista pisteytystä sovellus täyttää 5-arvosanan minimiedellytykset seuraavalla tavalla:
- Toimiva tietokantaa käyttävä web-sovellus: On
- Vähintään kolme tietokohdetta: Käyttäjät, pelit ja myyntikohteet
- Käyttäjä yhdistetty tietokohteeseen: Käyttäjällä on omat myyntikohteet
- Vähintään kaksi täyttä CRUD-tietokantaa: Pelit ja myyntikohteet
- Monesta moneen -suhde: Pelit ja myyntikohteet
- Vähintään kaksi monimutkaista yhteenvetokyselyä: Myytyjen pelien keskihinnan ja myyntimäärän selvittäminen eri kriteereillä (kaksi erillistä kyselyä), ja etusivun "tiesitkö että"-kysely.
