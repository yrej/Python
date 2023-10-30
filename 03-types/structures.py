def charFrequency(Veta):
    pocetZnaku = {}
    for znak in Veta:
        if znak == ' ':
            continue
        if znak in pocetZnaku:
            pocetZnaku[znak] += 1
        else:
            pocetZnaku[znak] = 1
    serazenyPocetZnaku = sorted(pocetZnaku.items(), key=lambda x: x[1], reverse=True)
    return serazenyPocetZnaku
veta = "Tři sta třicet tři stříbrných stříkaček přestříkalo přes tři sta třicet tři stříbrných střech."

vysledek = charFrequency(veta)
print("Věta:", veta)
print("Četnost výskytu písmen:")
print("-----------------------")
for znak, pocet in vysledek:
    print(f"('{znak}', {pocet}),")