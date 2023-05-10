def calcular_error(valores_reales, pronostico):
    pronostico_cortado = pronostico[:-1]
    resultado = 0
    for i in range(len(pronostico_cortado)):
        resultado += abs(valores_reales[i+len(valores_reales)-len(pronostico)] - pronostico_cortado[i])
    divisor = len(pronostico_cortado)
    resultado /= divisor
    return resultado