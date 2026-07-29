def sumaPolinomios(p, q):
    grado = max(len(p), len(q))
    resultado = [0] * grado

    for i in range(grado):
        coef_p = p[i] if i < len(p) else 0
        coef_q = q[i] if i < len(q) else 0
        resultado[i] = coef_p + coef_q

    return resultado


def restaPolinomios(p, q):
    grado = max(len(p), len(q))
    resultado = [0] * grado
    for i in range(grado):
        coef_p = p[i] if i < len(p) else 0
        coef_q = q[i] if i < len(q) else 0
        resultado[i] = coef_p - coef_q
    return resultado


def multiplicacionConst(p, c):
    resultado = []
    for coef in p:
        resultado.append(coef * c)
    return resultado


def multiplicar_xMenos_valor(p, a):
    resultado = [0] * (len(p) + 1)

    for i in range(len(p)):
        resultado[i] += -a * p[i]
        resultado[i + 1] += p[i]
    return resultado

def imprimirPolinomio(p):
    terminos = []

    for i in range(len(p)):
        coef = p[i]

        if coef == 0:
            continue

        # Para evitar cosas como 1.0 o 2.0
        if coef == int(coef):
            coef = int(coef)

        if i == 0:
            termino = str(abs(coef))
        elif i == 1:
            if abs(coef) == 1:
                termino = "x"
            else:
                termino = str(abs(coef)) + "x"
        else:
            if abs(coef) == 1:
                termino = "x^" + str(i)
            else:
                termino = str(abs(coef)) + "x^" + str(i)

        if len(terminos) == 0:
            if coef < 0:
                terminos.append("-" + termino)
            else:
                terminos.append(termino)
        else:
            if coef < 0:
                terminos.append(" - " + termino)
            else:
                terminos.append(" + " + termino)

    if len(terminos) == 0:
        return "0"

    return "".join(terminos)
