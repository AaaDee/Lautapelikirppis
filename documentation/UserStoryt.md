# User Story -kuvaukset

Kaikki käyttötapaukset kuvattu sovelluksen käyttäjän näkökulmasta.

SQL-kyselyissä käyttäjän antamia syötteitä ja muita vaihtuvia tietoja tietoja kuvataan johdonmukaisesti muuttujilla x,y,z...

## Haluan selata myynnissä olevia kohteita, joita mahdollisesti haluan ostaa

Tehty

Hyväksymiskriteerit
- Item-tietokannan sisältö selattavissa sivustolla
- Selausmahdollisuus löydettävissä etusivulta
- Näkyvissä vain ei-myydyt pelit

SQL-kysely:

(kohteen tiedot)
FROM Item SELECT name, description price, account_id;

(käyttäjän tiedot, linkitetty sqlalchemyn avulla)
FROM Account SELECT location, email WHERE account_id = x;

## Haluan selata sivuston tietokannassa olevia pelejä, jotta tiedän että onko peli, jota haluan myydä vielä tietokannassa

Tehty

Hyväksymiskriteerit:
- Game-tietokannan sisältö on selattavissa sivustolla
- Selausmahdollisuus on löydettävissä etusivulta

SQL-kysely:

FROM Game SELECT *;

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

UPDATE Game SET name=x, bgg=y WHERE Game.id = z;

## Haluan kirjautua sivustolle, jotta voin myydä pelejäni

Tehty

Hyväksymiskriteerit:
- Käyttäjä-tietokanta luotu
- Kirjautumistoiminnallisuus toteutettu sivustolla

## Haluan lisätä pelin myyntiin

Tehty

Hyväksymiskriteerit:
- Käyttäjä- ja Myyntikohde -tietokannat luotu
- (tekemättä) Pelien lisääminen myyntikohteeseen mahdollista 
- Muiden myyntikohteen ominaisuuksien (kuten kuvaus ja hinta) asettaminen mahdollista

## Haluan rekisteröityä sivustolle

Tehty

Hyväksymiskriteerit
- Rekisteröitymislomake tehty
- Linkki rekisteröitymiseen löydettävissä etusivulta

## Haluan muokata/poistaa omia myyntikohteitani, koska olen myynyt ne tai niissä on virhe

Tehty

Hyväksymiskriteerit
- Myyntikohteissa täysi CRUD
- Tämän lisäksi myös kohteen pelien muokkaaminen myyntikohteessa on mahdollista
- Muokkauksen käyttöliittymä toteutettu selaimessa

## Haluan tietää pelin aiempien myyntien keskihinnan, jotta osaan määritellä oman pelini hinnan

Tehty

Hyväksymiskriteerit
- Hinnan muodostava yhteenvetokysely tehty
- Kyselyt eriytetty yksittäisille peleille ja pelipaketeille (jottei pelipaketin hinta sotke yksittäisen pelin hintaa)
- Hintatiedot nähtävissä pelin sivulla

SQL-kysely (yksittäiskappaleille):

SELECT COUNT(Game_item.game_id) AS totalAmount,  
AVG(Item.price) AS avgPrice, Game_item.item_id,  
Item.sold, Temp.itemAmount as itemAmount  
FROM Game_item  
LEFT JOIN ITEM ON Item.id = Game_item.item_id 

LEFT JOIN (  
            SELECT count(*) AS itemAmount, item_id   
           FROM Game_item   
           GROUP BY item_id   
           )

AS Temp ON Temp.item_id = Game_item.item_id  
WHERE (game_id = x AND Item.sold AND itemAmount = 1)  
GROUP BY Game_item.game_id;





