/*Toteuta moduuli funktioita, joka toteuttaa nuolifunktiot
- tulostaNelio(sivu, tulostin), joka tulostaa tähtineliön tulostin-funktiolla
- tulostaSuorakulmio(leveys, korkeus, tulostin), joka tulostaa tähtisuorakulmion tulostin-funktiolla
- tulostaKolmio)korkeus, tulostin), joka tulostaa suorakulmaisen tähtikolmion kärki ylöspäin tulostinfunktiolla
- lukusarjanSumma(n), joka palauttaa lukusarjan 1..n summan
- kertoma(n), joka palauttaa luvun n kertoman, siis lukujen 1..n tulon. */

const tulostus = require('./tulostus');



const tulostNelio = (sivu) => {
  for(let i = 0; i < sivu; i++){
      tulostus.tulostaTahtia(sivu)
  }   
}
const tulostaSuorakulmio = (x,y) => {
    for(let i = 0; i < y; i++){
        tulostus.tulostaTahtia(x)
    }
}

const tulostaKolmio = (x) => {
    for(let i = 1; i <= x; i++){
        tulostus.tulostaTahtia(i)
    }
}
const lukusarjanSumma = (x) => {
    let result = x - (x/2);
    let parsed = result.toString();
    output = parsed + parsed;
    tulostus.tulostaTulos(output);
}

const kertoma = (x) => {
    let result = x * x;
    let parsed = result.toString();
    tulostus.tulostaTulos(parsed);
}


kertoma(20);
lukusarjanSumma(100);     
tulostNelio(10);
tulostaSuorakulmio(5,3);
tulostaKolmio(3);


module.exports = {
kertoma,
lukusarjanSumma,     
tulostNelio,
tulostaSuorakulmio,
tulostaKolmio,

  }