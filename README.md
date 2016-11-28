# misel-dneva

## Opis:

#### Bistvo aplikacije:
Misel Dneva je spletna aplikacija, ki omogoča uporabnikom preko videja deliti svoje misli.

#### Povzetek:
Ljudje smo misleča bitja in vsem se na dan porodi tisoč in ena misel. Večino njih zadržimo zase in s svojimi najbljižjimi. A za nekatere se nam zdi dobro, če bi jih lahko delili tudi z drugimi. Z raznimi socialnimi omrežji to v večji meri naredimo zelo neosebno, v obliki teksta, ki ga lahko ob neustreznem slovničnem zapisu razume vsak po svoje. Ali pa napišemo, posnamemo daljše video bloge, v katerih se pogosto zgubimo in pozabimo na tisto bistvo, ki smo ga hoteli izpostaviti. <br> Vsemu temu lahko naredimo konec tako, da bistvo svoje misli povzamemo v kratkem videju. S tem damo večjo vrednost temu kar resnično mislimo in želimo izpostaviti, pa naj bodo to bodisi dobre želje, nastveti, podpore ljudem, našo trenutno občutje, kaj zabavnega ali zgolj filozofiranje. V končni fazi je misel tista, ki žene napredek in kot je Descartes rekel:

> "Mislim, torej sem"

## Lastnosti:

#### Glavne lastnosti:
1. Strani:
   * Uvodna spletna stran oglašuje najbolj priljubljene video misli dneva
   * Iskalna spletna stran omogoča prikaz in hitro iskanje med priljubljenimi video misilimi
   * Uporabnikova spletna stran vsebuje ustrezne opcije za pregled in ustvarjanje video misli
   * Administratorjeva spletna stran vsebujejo ustrezne opcije za upravljanje uporabnikov
   * Video misli vsebujejo svojo stran, kjer lahko uporabniki debaritrajo
   * Strani vsebujejo spletni obrazec za prijavo uporabnika
   * Strani so odzivne glede na velikost zaslona
2. Administracija:
   * Administrator lahko daje opozorila, onemogoča in briše uporabnike
   * Administrator lahko po potrebni onemogoči ali zbriše video misel uporabnika
   * Administrator lahko po potrebi zbriše kometarje uporabnikov
3. Uporabniki:
   * Uporabnik si ustvari svoj lasten profil
   * Uporabnik preko spletne kamere posname svojo video misel in jo shrani/naloži na strežnik
   * Uporabnik svojo video misel *(pred objavo)* ustrezno imenuje in označi *(doda ključne besede ter ali je misel vidna javno ali privatno ← samo preko povezave)*
   * Uporabnik ima pregled na svojimi video mislimi, kjer jih lahko poljubno ureja, vidi statistiko in po potrebi odstrani
   * Uporabnik lahko išče med posameznimi video mislimi, glede na ključne besede
   * Uporabniki lahko objavljene video misli ocenjujejo, komentirajo, označijo kot neprimerne ter jih posredujejo preko drugih socialnih omrežij

## Ciljna publika in naprave:

#### Publika:
Ciljna publika ni omejena, vendar se aplikacija izgledno bolj posveča ljudem starim med 18 in 30 let.

#### Podprte naprave:

| Osebni računalnik | Laptop | Tablica | Pametni telefon |
| ----------------- | ------ | ------- | --------------- |
| Da | Da | Načeloma (odvisno od brskalnika) | Načeloma (odvisno od brskalnika) |
 
#### Podprti brskalniki:

| Chrome | Firefox | Opera | Safari | Edge | IE |
| ------ | ------- | ----- | ------ | ---- | -- |
| Da (ver. 49+) | Da (ver. 30+) | (? Ơ ?) | (? ѽ ?) | Deloma (brez videja) | Ne (zastarelo) |

## Tehnologija:

* HTML5
* CSS3
* Javascript
* ...

## Povzetki:

#### Nekompatibilnosti:

* Chrome:
   * Trenutno ni vidnih nekompatibilnosti oz so le te odpravljene z ustreznim CSS-jem.
* Firefox:
   * Pri video_id.html ne upošteva paddinga, ki ga trenutni element povozi in gumba za ocenjevanje misli ne poveča pravilno. Če se ročno trenutni padding izklopi, da upošteva privzetega za gumb, potem razširi pravilno. Če pa se nastavi padding da privzame privzetega, ga ne upošteva in gumb je še vedno tanek.
   * Submit gumb ima zaradi "dodatnega" teksta (pošlji poizvedbo) večjo velikost, kot recimo enak gumb pri Chromu (pošlji). Zato mu je potrebno zagotoviti dodaten prostor.
* Edge:
   * Enako kot pri firefoxu pri video_id.html ne upošteva paddinga, in ga ne poveča ustrezno s CSS zahtevami, zato so gumbi pretanki.
   * Submit gumb ima zaradi "dodatnega" teksta (submit query) večjo velikost, kot recimo enak gumb pri Chromu (pošlji). Zato mu je potrebno zagotoviti dodaten prostor.
   * Ne podpira zapisov videa .webm, katere se tako nalaga na stran in s katerimi se shrani video.
   * Kjer bi moral biti video, se kljub temu, da ni videja, njegovo okno ne poveča ustrezno in ga ni mogoče nikakor drugače povečati.
   * Nima še dodane podpore za snemanje videja preko kamere.
* Ostalo:
   * HTML validator priporoča, da se ne uporablja inputa tipa date, saj ni podprt v vseh brskalnikih in vrže ven error. Popolno protislovje, glede na to, da večina stvari ni podprtih povsod in je priporočeno, da se uporablja nove tipe zato, da ko bodo podprte, da bodo že delovale.

#### Zmogljivosti in gradniki:

* Veliko truda je bilo vloženega v sam izgled strani, da je stran kolikor se le da smiselno odzivna ne glede na velikost zaslona naprave.
* Vsi gumbi so oblikovani s CSS-jem, da zgledajo v vseh brskalnikih kolikor se da enako.

#### Komentarji in problemi:

* Potrebno bi bilo iti v več iteracij razvoja, da bi se preverilo delovanje aplikacije.
* Stran je trenotno v delovanju predogleda ogrodja (template-a) in vsebuje delno nedelujoče elemente (jih ni smiselno nastavljati v 1. Fazi), ki jih je potrebno še ustrezno nastaviti glede na funkcionalnost izgled 2. Faze.
* Dobro bi bilo imeti spletnega dizajnerja za načrtovanje strani v primerih odzivnega delovanja na več napravah, ki bi reševal problem kaj narediti v določenih primerih, ko zaradi neskladnosti zaslonov pride do odvečnega praznega prostora
* Določenih delov spletne strani/aplikacije se ne da uporabljati v večino drugih brskalnikih, z izjemo Chroma in Firefoxa, saj so ti le enostavno preveč zaostali za trenutnim razvojem Web 3.0.
* Z zadnjimi varnostnimi popravki je dostop do spletne kamere in zvoka naprave omogočen samo, če imamo veljaven certifikat in stran podpira https.