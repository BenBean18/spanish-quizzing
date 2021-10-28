import random, os, time

conjugaciones_ar = {"yo": "-aba",
                    "tú": "-abas",
                    "usted/él/ella": "-aba",
                    "nosotros(as)": "-ábamos",
                    "vosotras(os)": "-abais",
                    "ustedes/ellos(as)": "-aban"}

conjugaciones_er_o_ir = {"yo": "-ía",
                         "tú": "-ías",
                         "usted/él/ella": "-ía",
                         "nosotros(as)": "-íamos",
                         "vosotras(os)": "-íais",
                         "ustedes/ellos(as)": "-ían"}

conjugaciones = {"-ar": conjugaciones_ar,
                 "-er": conjugaciones_er_o_ir,
                 "-ir": conjugaciones_er_o_ir}

pronombres = list(conjugaciones_ar.keys())

# I heard a pileated woodpecker around 1:30pm Monday, Oct 4 in literature class as I was working on this (since I finished classwork)

respuestas = 0
respuestas_correctas = 0

while True:
    pronoun = random.choice(pronombres)
    ending = random.choice(list(conjugaciones.keys()))
    respuesta_correcta = conjugaciones[ending][pronoun]
    print("\033[31má\033[33mé\033[32mí\033[36mó\033[34;1mú\033[0m | \033[35mfor copying\033[0m")
    respuesta = input(f"\033[33mThe imperfect conjugation for [verb]{ending}, {pronoun} is: \033[32;1m[verb]-")
    respuestas += 1
    if "-" + respuesta.replace("-", "") == respuesta_correcta:
        respuestas_correctas += 1
        os.system("printf '\033[0m\033c'")
        print(f"✅ \033[1;32m{respuestas_correctas}\033[0m/\033[0;36m{respuestas}\033[0m")
    else:
        print(f"\033[31m❌ El conjugación correcto es: {respuesta_correcta}")
        time.sleep(2)
        os.system("printf '\033[0m\033c'")
        print(f"❌ \033[1;32m{respuestas_correctas}\033[0m/\033[0;36m{respuestas}\033[0m")