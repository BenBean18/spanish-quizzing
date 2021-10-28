from copy import deepcopy
import random, os, time

conjugacion_ar_er_ir = ["-e", "-iste", "-o", "-imos", "-isteis", "-ieron"]
conjugacion_j_ar_er_ir = ["-e", "-iste", "-o", "-imos", "-isteis", "-eron"]
pronombres = ["yo", "tú", "él/ella/usted", "nosotros/nosotras", "vosotros/vosotras", "ustedes/ellos/ellas"]

def CONJUGAR(verbo_sin_finalizando: str, _conjugaciones: list[str]):
    conjugaciones = deepcopy(_conjugaciones)
    for indice in range(len(conjugaciones)):
        conjugaciones[indice] = verbo_sin_finalizando.replace("-", "") + conjugaciones[indice].replace("-", "")
    return conjugaciones

SER_Y_IR = ["fui", "fuiste", "fue", "fuimos", "fuisteis", "fueron"]

verbos = {
    # i-stem
    "hacer": ["hice", "hiciste", "hizo", "hicimos", "hicisteis", "hicieron"], # especial
    "querer": CONJUGAR("quis-", conjugacion_ar_er_ir),
    "venir": CONJUGAR("vin-", conjugacion_ar_er_ir),

    # u-stem
    "haber": CONJUGAR("hub-", conjugacion_ar_er_ir),
    "poder": CONJUGAR("pud-", conjugacion_ar_er_ir),
    "poner": CONJUGAR("pus-", conjugacion_ar_er_ir),
    "saber": CONJUGAR("sup-", conjugacion_ar_er_ir),

    # uv-stem
    "andar": CONJUGAR("anduv-", conjugacion_ar_er_ir),
    "estar": CONJUGAR("estuv-", conjugacion_ar_er_ir),
    "tener": CONJUGAR("tuv-", conjugacion_ar_er_ir),

    # j-stem
    "decir": CONJUGAR("dij-", conjugacion_j_ar_er_ir),
    "traer": CONJUGAR("traj-", conjugacion_j_ar_er_ir),
    "conducir": CONJUGAR("conduj-", conjugacion_j_ar_er_ir),

    # weirdos
    "ser": SER_Y_IR,
    "ir": SER_Y_IR,
    "dar": ["di", "diste", "dio", "dimos", "disteis", "dieron"],
    "ver": ["vi", "viste", "vio", "vimos", "visteis", "vieron"]
}

imprimir = print

respuestas_incorrectas = []
verbos_perfectos = []
respuestas = 0
respuestas_correctas = 0

def examen(verbo):
    global respuestas, respuestas_correctas
    incorrectas = 0
    conjugaciones = verbos[verbo]
    imprimir(f"\033[33mConjugar: \033[32;1m{verbo}")
    for conjugacion_índice in range(len(conjugaciones)):
        respuestas += 1
        print("\033[31má\033[33mé\033[32mí\033[36mó\033[34;1mú\033[0m | \033[35mfor copying\033[0m")
        respuesta = input(f"\033[33mConjugación pretérito por {pronombres[conjugacion_índice]}: \033[32;1m")
        if respuesta == conjugaciones[conjugacion_índice]:
            respuestas_correctas += 1
            os.system("printf '\033[0m\033c'")
            print(f"pretérito: \033[33;1m{verbo}")
            print(f"✅ \033[1;32m{respuestas_correctas}\033[0m/\033[0;36m{respuestas}\033[0m")
        else:
            incorrectas += 1
            print(f"\033[31m❌ El conjugación correcto es: {conjugaciones[conjugacion_índice]}")
            time.sleep(2)
            os.system("printf '\033[0m\033c'")
            print(f"pretérito: \033[33;1m{verbo}")
            print(f"❌ \033[1;32m{respuestas_correctas}\033[0m/\033[0;36m{respuestas}\033[0m")
            respuestas_incorrectas.append(f"{verbo}: {pronombres[conjugacion_índice]} != {respuesta}")
    if incorrectas == 0:
        verbos_perfectos.append(verbo)

Cierto = True

verbos_aleatorios = random.sample(list(verbos.keys()), len(verbos))

for verbo in verbos_aleatorios:
    examen(verbo)

print(f"Verbos perfectos: {len(verbos_perfectos)}/{len(verbos)}")
print(f"Respuestas incorrectas: {respuestas_incorrectas}")