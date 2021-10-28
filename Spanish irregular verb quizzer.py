from copy import deepcopy
import random, os, time

conjugacion_ar = ["-o", "-as", "-a", "-amos", "-áis", "-an"]
conjugacion_er = ["-o", "-es", "-e", "-emos", "-éis", "-en"]
conjugacion_ir = ["-o", "-es", "-e", "-imos", "-ís", "-en"]
índices = ["yo", "tú", "él/ella/usted", "nosotros/nosotras", "vosotros/vosotras", "ustedes/ellos/ellas"]

def CONJUGAR(verbo: str, _conjugaciones: list[str]):
    conjugaciones = _conjugaciones
    for indice in range(len(conjugaciones)):
        conjugaciones[indice] = verbo[:-2] + conjugaciones[indice].replace("-", "")
    return conjugaciones

def CONJUGACION_REGULAR_POR(verbo: str):
    if verbo.endswith("ar"):
        c = deepcopy(conjugacion_ar)
        return c
    elif verbo.endswith("er"):
        c = deepcopy(conjugacion_er)
        return c
    elif verbo.endswith("ir"):
        c = deepcopy(conjugacion_ir)
        return c

def YO_GO(verbo: str):
    c = CONJUGACION_REGULAR_POR(verbo)
    c[0] = "-go"
    conjugaciones_del_verbo = CONJUGAR(verbo, c)
    if verbo == "hacer":
        conjugaciones_del_verbo[0] = "hago"
    return conjugaciones_del_verbo

def traer():
    c = deepcopy(conjugacion_er)
    c[0] = "-igo"
    return CONJUGAR("traer", c)

def E_IE(verbo: str):
    verbo_cambiado = verbo.replace("e", "ie", 1) # esta línea reemplaza la primera ocurrencia de la letra "e" en el verbo. casos especiales como "pref*e*rir" que reemplazan la segunda ocurrencia de la letra "e" deben ser manejado de manera diferente.
    c = CONJUGAR(verbo_cambiado, CONJUGACION_REGULAR_POR(verbo_cambiado))
    c[3] = c[3].replace(verbo_cambiado[:-2], verbo[:-2]) # nosotros/nosotras
    c[4] = c[4].replace(verbo_cambiado[:-2], verbo[:-2]) # vosotros/vosotras
    return c

def E_IE_BUT_STARTS_WITH_E(verbo: str):
    verbo = "ë" + verbo.removeprefix("e")
    verbo_cambiado = verbo.replace("e", "ie", 1).replace("ë", "e")
    c = CONJUGAR(verbo_cambiado, CONJUGACION_REGULAR_POR(verbo_cambiado))
    verbo = verbo.replace("ë", "e")
    c[3] = c[3].replace(verbo_cambiado[:-2], verbo[:-2]) # nosotros/nosotras
    c[4] = c[4].replace(verbo_cambiado[:-2], verbo[:-2]) # vosotros/vosotras
    return c

def preferir():
    verbo = "preferir"
    verbo_cambiado = "prefierir"
    c = CONJUGAR(verbo_cambiado, CONJUGACION_REGULAR_POR(verbo_cambiado))
    c[3] = c[3].replace(verbo_cambiado[:-2], verbo[:-2]) # nosotros/nosotras
    c[4] = c[4].replace(verbo_cambiado[:-2], verbo[:-2]) # vosotros/vosotras
    return c

def YO_GO_E_IE(verbo: str):
    c = E_IE(verbo)
    c[0] = YO_GO(verbo)[0]
    return c

def decir():
    c = E_IE("decir")
    c[0] = YO_GO("decir")[0]
    return c

def O_UE(verbo: str):
    verbo_cambiado = verbo.replace("o", "ue", 1)
    c = CONJUGAR(verbo_cambiado, CONJUGACION_REGULAR_POR(verbo_cambiado))
    c[3] = c[3].replace(verbo_cambiado[:-2], verbo[:-2]) # nosotros/nosotras
    c[4] = c[4].replace(verbo_cambiado[:-2], verbo[:-2]) # vosotros/vosotras
    return c

def YO_IRREGULAR(verbo: str, yo_conjugacion: str):
    c = CONJUGAR(verbo, CONJUGACION_REGULAR_POR(verbo))
    c[0] = yo_conjugacion
    return c

verbos = {
    "hacer": YO_GO("hacer"),
    "poner": YO_GO("poner"),
    "salir": YO_GO("salir"),
    "traer": traer(),

    "decir": ["digo", "dices", "dice", "decimos", "decís", "dicen"],
    "venir": YO_GO_E_IE("venir"),
    "tener": YO_GO_E_IE("tener"),

    "conocer": YO_IRREGULAR("conocer", "conozco"),
    "dar": YO_IRREGULAR("dar", "doy"),
    "saber": YO_IRREGULAR("saber", "sé"),
    "ver": YO_IRREGULAR("ver", "veo"),

    "querer": E_IE("querer"),
    "cerrar": E_IE("cerrar"),
    "pensar": E_IE("pensar"),
    "empezar": E_IE_BUT_STARTS_WITH_E("empezar"),
    "entender": E_IE_BUT_STARTS_WITH_E("entender"),
    "preferir": preferir(),

    "poder": O_UE("poder"),
    "dormir": O_UE("dormir"),
    "almorzar": O_UE("almorzar"),
    "costar": O_UE("costar"),
    "encontrar": O_UE("encontrar"),
    "volver": O_UE("volver"),

    "servir": ["sirvo", "sirves", "sirve", "servimos", "servís", "sirven"],
    "pedir": ["pido", "pides", "pide", "pedimos", "pedís", "piden"]
}

imprimir = print
# imprimir(verbos)

respuestas_incorrectas = []
verbos_perfectos = []

def examen(verbo):
    incorrectas = 0
    conjugaciones = verbos[verbo]
    imprimir(f"Conjugar: {verbo}")
    for conjugacion_índice in range(len(conjugaciones)):
        if input(f"Conjugacion por {índices[conjugacion_índice]}: ") == conjugaciones[conjugacion_índice]:
            os.system("printf '\033c'")
            print(verbo)
            print("✅")
        else:
            print(f"❌ El conjugación correcto es: {conjugaciones[conjugacion_índice]}")
            time.sleep(2)
            os.system("printf '\033c'")
            print(verbo)
            print("❌")
            respuestas_incorrectas.append(f"{verbo}: {índices[conjugacion_índice]}")
            incorrectas += 1
    if incorrectas == 0:
        verbos_perfectos.append(verbo)

Cierto = True

verbos_aleatorios = random.sample(list(verbos.keys()), len(verbos))

for verbo in verbos_aleatorios:
    examen(verbo)

print(f"Verbos perfectos: {len(verbos_perfectos)}/{len(verbos)}")
print(f"Respuestas incorrectas: {respuestas_incorrectas}")