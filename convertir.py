"""

Ce programme convertit les chiffres données en ligne de commandes en francais
usage : python3 convertir.py --nombres chiffre1 chiffre2 chiffreN
exemple : python3 convertir.py --nombres 10 18 17 100 101 12568 15616 78000 780001 


"""


import argparse

# Création d'un dictionnaire des nombres de 1 à 16 en français
nombres_fr = {
    0: "Zero",
    1: "Un",
    2: "Deux",
    3: "Trois",
    4: "Quatre",
    5: "Cinq",
    6: "Six",
    7: "Sept",
    8: "Huit",
    9: "Neuf",
    10: "Dix",
    11: "Onze",
    12: "Douze",
    13: "Treize",
    14: "Quatorze",
    15: "Quinze",
    16: "Seize"
}

# Création d'un dictionnaire des nombres par dizaines de 20 à 60 en français
nombres_dizaine = {
    20: "Vingt",
    30: "Trente",
    40: "Quarante",
    50: "Cinquante",
    60: "Soixante"
}


def range_17_20(nombre):
    "traite l'intervalle de 17 à 19"
    unite = nombre % 10
    return nombres_fr[10] + "-" + nombres_fr[unite]


def range80_90(nombre):
    "traite l'intervalle de 80 à 89"
    unite = nombre % 10
    decomposition = nombre // 20
    if unite == 0:
        return nombres_fr[decomposition] + "-" + nombres_dizaine[20]
    else:
        return nombres_fr[decomposition] + "-" + \
            nombres_dizaine[20] + '-' + nombres_fr[unite]


def moins_de_cents(nombre):
    "traite les chiffres de 0 à 99 avec toutes les regles"
    if nombre in nombres_fr:
        return nombres_fr[nombre]

    if nombre in nombres_dizaine:
        return nombres_dizaine[nombre]

    if nombre not in nombres_fr and nombres_dizaine:
        if nombre in range(17, 20):
            return range_17_20(nombre)

        if nombre in range(21, 30):
            unite = nombre % 10
            if unite == 1:
                return nombres_dizaine[20] + '-et-' + nombres_fr[unite]
            else:
                return nombres_dizaine[20] + '-' + nombres_fr[unite]

        if nombre in range(31, 40):
            unite = nombre % 10
            if unite == 1:
                return nombres_dizaine[30] + '-et-' + nombres_fr[unite]
            else:
                return nombres_dizaine[30] + '-' + nombres_fr[unite]

        if nombre in range(41, 50):
            unite = nombre % 10
            if unite == 1:
                return nombres_dizaine[40] + '-et-' + nombres_fr[unite]
            else:
                return nombres_dizaine[40] + '-' + nombres_fr[unite]

        if nombre in range(51, 60):
            unite = nombre % 10
            if unite == 1:
                return nombres_dizaine[50] + '-et-' + nombres_fr[unite]
            else:
                return nombres_dizaine[50] + '-' + nombres_fr[unite]

        if nombre in range(61, 70):
            unite = nombre % 10
            if unite == 1:
                return nombres_dizaine[60] + '-et-' + nombres_fr[unite]
            else:
                return nombres_dizaine[60] + '-' + nombres_fr[unite]

        if nombre in range(70, 80):
            unite = nombre % 10

            if unite == 0:
                return nombres_dizaine[60] + "-" + nombres_fr[nombre - 60]
            else:
                if unite in range(1, 7):
                    return nombres_dizaine[60] + "-" + nombres_fr[nombre - 60]
                else:
                    new_unite = unite + 10
                    return nombres_dizaine[60] + '-' + range_17_20(new_unite)

        if nombre in range(80, 90):
            return range80_90(nombre)

        if nombre in range(90, 100):
            unite = nombre % 10
            decomposition = nombre // 20

            if unite in range(0, 7):
                if unite == 0:
                    f = range80_90(nombre)
                    return f + "-" + nombres_fr[nombre - 80]
                else:
                    return nombres_fr[decomposition] + "-" + \
                        nombres_dizaine[20] + "-" + nombres_fr[nombre - 80]
            else:
                new_unite = nombre - decomposition * 20
                return nombres_fr[decomposition] + "-" + \
                    nombres_dizaine[20] + '-' + range_17_20(new_unite)


def centaine(nombre):
    "fonction pour traiter les centaines"

    unite = nombre % 100
    centaine = nombre // 100
    if centaine == 1:
        if unite != 0:
            return "cent-" + moins_de_cents(unite)
        else:
            return "cent"
    else:
        if centaine == 0:
            return moins_de_cents(unite)
        else:
            if unite == 0:
                return moins_de_cents(centaine) + '-Cent'
            else:
                return moins_de_cents(centaine) + \
                    '-Cent-' + moins_de_cents(unite)


def milliers(nombre):
    "fonction pour traiter les milliers"

    unite = nombre % 1000
    miliers = nombre // 1000
    if miliers == 1:
        if unite != 0:
            return "milles-" + centaine(unite)
        else:
            return "milles"

    if unite // 100 != 0:
        return centaine(miliers) + '-mille-' + centaine(unite)
    if unite == 0:
        return centaine(miliers) + '-milles'
    else:
        return centaine(miliers) + '-mille-' + centaine(unite)


def main():
    " Main du programme avec la definition du parser pour la lignde de commande"

    parser = argparse.ArgumentParser(
        description="Convertir une liste de nombres en texte français")
    parser.add_argument(
        '--nombres',
        type=int,
        nargs='+',
        help="Une liste de nombres entiers entre 0 et 999999",
        required=True
    )
    args = parser.parse_args()

    conversion = {}
    for nombre in args.nombres:
        if nombre // 1000 != 0:
            conversion[nombre] = milliers(nombre)
        elif nombre // 100 != 0:
            conversion[nombre] = centaine(nombre)
        elif nombre // 10 != 0:
            conversion[nombre] = moins_de_cents(nombre)
        else:
            conversion[nombre] = moins_de_cents(nombre)

    print(conversion)


if __name__ == "__main__":
    main()