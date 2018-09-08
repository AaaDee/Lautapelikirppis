# Lautapelikirppis
An online marketplace for buying and selling board games. Coursework project (in Finnish).

Kuvaus:

Tällä hetkellä käytettyjä lautapelejä ostetaan ja myydään lähinnä tätä tarkoitusta varten tehdyllä Facebook-sivulla. Sivun kankeus ja toiminnallisuuden puute häiritsee monia, joten eräs peliharrastaja päättää alkaa kehittelemään erillistä Lautapelikirppis-sivustoa kaupankäyntiä varten. Sivuston keskeisiä vaatimuksia ovat myyntikohteiden helppo listaaminen ja selaaminen, tietyn pelin hakeminen myyntiluettelosta, ja toteutuneiden kauppojen pohjalta muodostetun tilastotiedon hakeminen.

Sovelluksen päänäkymän muodostaa listaus myynnissä olevista kohteista. Kohteet voivat olla joko yksittäisiä pelejä, tai isompia pelipaketteja. Tyypillinen paketti koostuu pelistä ja sen lisäosista, koska myyjä ei tyypillisesti halua myydä peliä ilman lisäosia tai toisinpäin. Yksittäisen myyntikohteen tietoja ovat myynnissä oleva(t) peli(t), hinta, kohteen sijainti, myyjän yhteystiedot ja lyhyt vapaamuotoinen kuvaus. Lisäksi pelistä voi olla tiedossa sen tunnus ulkopuolisella BoardGameGeek.com (BGG)–sivustolla, jonka avulla käyttäjät voivat tutustua peleihin tarkemmin, ja jota hyödynnetään pelien tunnistamiseksi tilastoinnissa. Sivustolla ei ole erillistä pikaviestimahdollisuutta, vaan kaupanteon yksityiskohdat sovitaan yhteystietojen avulla sivuston ulkopuolella..

Lisäksi käyttäjät voivat asettaa omia pelejään tai pakettejaan myytäväksi. Myyntikohteeseen lisätään myytävät pelit, niiden hinta, sijainti, vapaamuotoinen kuvaus ja vapaaehtoisesti myös BGG-tunnus. Myyjän tiedot lisätään kohteeseen automaattisesti, eli niitä ei tarvitse erikseen kirjata jokaiseen kohteeseen.

Käyttäjillä on myös mahdollisuus muokata ja poistaa ilmoituksiaan. Lisäksi kohde voidaan merkitä myydyksi, jolloin se kirjautuu toteutuneena kauppana sivuston tilastoon.

Tilastopuolella sivusto tarjoaa kahta eri ominaisuutta: Etusivulla on tarjolla yleisiä tilastoja, kuten myytyjen pelien määrän, aktiivisimmat kauppakaupungit ja muuta tällaista. Lisäksi yksittäisestä pelistä voi selvittää joitakin hintatietoja, kuten pelin keskihinnan toteutuneissa kaupoissa. Viihdearvon lisäksi tilastojen tarkoitus on auttaa käyttäjiä esimerkiksi sopivan myyntihinnan arvioinnissa.

Toiminnallisuus

- Sivustolle kirjautuminen
- Myyntikohteiden lisäys, muokkaus ja poisto
- Myyntikohteiden selaaminen ja haku
- Pelin lisääminen sivuston tietokantaan (tilastointia varten)
- Yleisen tilastotiedon lukeminen
- Pelikohtaisen tilastotiedon lukeminen
