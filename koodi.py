import json


# Funktio kysyy luettavan tiedoston nimeä, ja lukee halutun tiedoston.
# Funktio tallentaa tiedoston muuttujaan, ja palauttaa muuttujan myöhempää käsittelyä varten.
def lue_tiedosto():
    tiedosto_nimi = input('tiedosto: ')
    with open(tiedosto_nimi) as tiedosto:
        tilastot = json.loads(tiedosto.read())
    print(f'luettiin {len(tilastot)} pelaajan tiedot')

    return tilastot


#Funktio tulostaa ohjelman suorituksen alussa komento-listan.
def komennot():
    print('Komennot: ')
    print('0 Lopeta')
    print('1 Hae pelaaja')
    print('2 Joukkueet')
    print('3 Maat')
    print('4 Joukkueen pelaajat')
    print('5 Maan pelaajat')
    print('6 Eniten pisteitä')
    print('7 Eniten maaleja')
    print()


# Funktio tulostaa pelaajien tiedot jäsentäen tulostuksen siistiksi.
def tulosta(pelaaja: dict):
    nimi = pelaaja['name']
    joukkue = pelaaja['team']
    maalit = pelaaja['goals']
    syotot = pelaaja['assists']
    pisteet = maalit + syotot
    print(f'{nimi:21}{joukkue:>2}{maalit:>4} + {syotot:>2} = {pisteet:>3}')


# Funktio kysyy tietyn pelaajan nimeä, hakee sen listalta ja välittää sen tulostusfunktiolle tulostettavaksi.
def hae_nimen_perusteella(tilastot: list):
    nimi = input('nimi: ')
    for pelaaja in tilastot:
        if pelaaja['name'] == nimi:
            tulosta(pelaaja)


# Funktio tulostaa kaikki tilaston joukkueet aakkosjärjestyksessä.
def hae_joukkueet(tilastot: list):
    joukkueet = set([pelaaja['team'] for pelaaja in tilastot])  # Set, koska ei haluta päällekkäisyyksiä
    print('\n'.join(sorted(joukkueet)))


# Funktio tulostaa kaikki tilaston maat aakkosjärjestyksessä.
def hae_maat(tilastot: list):
    maat = set([pelaaja['nationality'] for pelaaja in tilastot])  # Set, koska ei haluta päällekkäisyyksiä
    print('\n'.join(sorted(maat)))


# Funktio kysyy tietyn joukkueen nimeä ja tulostaa joukkueen pelaajat pistejärjestyksessä.
def hae_joukkueen_pelaajat(tilastot: list):
    joukkue = input('joukkue: ')
    pelaajat = [pelaaja for pelaaja in tilastot if pelaaja['team'] == joukkue]
    pelaajat.sort(key=lambda pelaaja: (pelaaja['goals'] + pelaaja['assists']), reverse=True)  # Järjestetään lista pistejärjestykseen.
    for pelaaja in pelaajat:
        tulosta(pelaaja)


# Funktio kysyy tietyn maan nimeä ja tulostaa maan pelaajat pistejärjestyksessä.
def hae_maan_pelaajat(tilastot: list):
    maa = input('maa: ')
    maat = [pelaaja for pelaaja in tilastot if pelaaja['nationality'] == maa]
    maat.sort(key=lambda pelaaja: (pelaaja['goals'] + pelaaja['assists']), reverse=True)  # Järjestetään lista pistejärjestykseen.
    for pelaaja in maat:
        tulosta(pelaaja)


# Funktio tulostaa halutun lukumäärän parhaiten pisteitä tehneitä pelaajia.
# Jos samat pistemäärät pelaajilla, maalien määrä ratkaisee järjestyksen. 
def eniten_pisteita(tilastot: list):
    lkm = int(input('kuinka monta: '))
    tilastot.sort(key=lambda pelaaja: (pelaaja['goals'] + pelaaja['assists'], pelaaja['goals']), reverse=True)  # Järjestetään lista pistejärjestykseen.
    for pelaaja in tilastot:
        if tilastot.index(pelaaja) < lkm:
            tulosta(pelaaja)


# Funktio tulostaa halutun lukumäärän eniten maaleja tehneitä pelaajia.
# Jos sama maalimäärä pelaajilla, pelatut ottelut ratkaisevat.
def eniten_maaleja(tilastot: list):
    lkm = int(input('kuinka monta: '))
    tilastot.sort(key=lambda pelaaja: (pelaaja['goals'], pelaaja['goals'] - pelaaja['games']), reverse=True)
    for pelaaja in tilastot:
        if tilastot.index(pelaaja) < lkm:
            tulosta(pelaaja)
    

# Ohjelman varsinainen käyttöliittymä.
# Luetaan tiedosto.
# Tulostetaan komennot.
# Aloitetaan interaktiivinen ohjelma jossa käyttäjä syöttää komentoja. 
def kayttoliityma():
    tilastot = lue_tiedosto()
    komennot()

    while True:
        komento = input('komento: ')
        if komento == '0':
            break
        elif komento == '1':
            hae_nimen_perusteella(tilastot)
        elif komento == '2':
            hae_joukkueet(tilastot)
        elif komento == '3':
            hae_maat(tilastot)
        elif komento == '4':
            hae_joukkueen_pelaajat(tilastot)
        elif komento == '5':
            hae_maan_pelaajat(tilastot)
        elif komento == '6':
            eniten_pisteita(tilastot)
        elif komento == '7':
            eniten_maaleja(tilastot)
            

if __name__ == '__main__':
    pass
kayttoliityma()
