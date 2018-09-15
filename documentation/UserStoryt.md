# User Story -kuvaukset

Kaikki käyttötapaukset kuvattu sovelluksen käyttäjän näkökulmasta.

SQL-kyselyissä käyttäjän antamia syötteitä ja muita vaihtuvia tietoja tietoja kuvataan johdonmukaisesti muuttujilla x,y,z...

## Haluan selata sivuston tietokannassa olevia pelejä, jotta tiedän että onko peli, jota haluan myydä vielä tietokannassa

Tehty

Hyväksymiskriteerit:
- Game-tietokannan sisältö on selattavissa sivustolla
- Selausmahdollisuus on löydettävissä etusivulta

SQL-kysely:

FROM Game SELECT *

## Haluan lisätä uuden pelin tietokantaan, koska sitä ei ollut tietokannassa

Tehty

Hyväksymiskriteerit:
- Pelien lisääminen Game-tietokantaan mahdollista
- Toiminnallisuus käyttäjän löydettävissä

SQL-kysely:

INSERT INTO Game (name, bgg) VALUES (x, y)

## Haluan muokata/poistaa jo sivustolta löytyviä pelejä, koska tietokannassa on virhe

Tehty

Hyväksymiskriteerit:
- Game-tietokannan rivien muokkaaminen ja poistaminen mahdollista
- Muokkaus ja poisto käyttäjän löydettävissä
- Sivusto päivittyy kuvaamaan tietokannan uutta tilaa

SQL-kysely:

UPDATE Game SET name=x, bgg=y WHERE Game.id = z

## Haluan kirjautua sivustolle, jotta voin myydä pelejäni

Tekemättä

Hyväksymiskriteerit:
- Käyttäjä-tietokanta luotu
- Kirjautumistoiminnallisuus toteutettu sivustolla

## Haluan lisätä pelin myyntiin

Tekemättä

Hyväksymiskriteerit:
- Käyttäjä- ja Myyntikohde -tietokannat luotu
- Pelien lisääminen myyntikohteeseen mahdollista
- Muiden myyntikohteen ominaisuuksien (kuten kuvaus ja hinta) asettaminen mahdollista

