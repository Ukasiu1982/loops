maxymalna_waga_paczki = 20
maxymalna_waga_elementu = 10
minimalna_waga_elementu = 1
numer_paczki = 0
wyslane_kilogramy = 0
aktualna_waga = 0
waga_najlzejszej_paczki = 20
numer_najlzejszej_paczki = 0
maxymalna_liczba_elementow = int(input("Jaka jest maksymalna liczba elemntów jaka chcesz dodac?: "))

for idx in range(maxymalna_liczba_elementow):
    waga_elementu = int(input("Podaj wage elementu: "))
    if waga_elementu == 0:
        break
    elif waga_elementu < minimalna_waga_elementu or waga_elementu > maxymalna_waga_elementu:
        print("Bledna waga")
        break
    else:
        wyslane_kilogramy += waga_elementu
    if aktualna_waga + waga_elementu <= maxymalna_waga_paczki:
        aktualna_waga += waga_elementu
    else:
        numer_paczki +=1

        if aktualna_waga < waga_najlzejszej_paczki:
            waga_najlzejszej_paczki = aktualna_waga
            numer_najlzejszej_paczki = numer_paczki
        aktualna_waga = waga_elementu

if maxymalna_liczba_elementow == 0:
    print("Liczba paczek to 0")
else:
    numer_paczki +=1

    if aktualna_waga < waga_najlzejszej_paczki:
        waga_najlzejszej_paczki = aktualna_waga
        numer_najlzejszej_paczki = numer_paczki

    puste_kilogramy = numer_paczki * 20 - wyslane_kilogramy
    puste_kilogramy_najlzejsza = 20 - waga_najlzejszej_paczki


    print("Liczba paczek, ktore zostaly wyslane to : {}. Liczba kilogramow wyslanych to: {}."
          "Suma pustych kilogramow to: {}. Paczka, ktora miała najwięcej pustych kilogramów to paczka z numerem: {}. "
          "Sa tam {} puste kilogramy."
          .format(numer_paczki, wyslane_kilogramy, puste_kilogramy,
            numer_najlzejszej_paczki,puste_kilogramy_najlzejsza))



