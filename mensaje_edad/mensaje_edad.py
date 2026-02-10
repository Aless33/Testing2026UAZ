def edad(numero):
    if isinstance(numero, list):
        if numero == []:
            return 'La lista debe de contener al menos un elemento'
        resultados = []
        for i in numero:
            resultados.append(edad(i))
        return resultados

    if isinstance(numero, str) or isinstance(numero, float):
        return 'Solo se admiten numeros enteros'
    if numero < 0:
        return 'No existes'
    if numero < 13:
        return 'Eres un niño'
    if numero < 18:
        return 'Eres un adolescente'
    if numero < 65:
        return 'Eres un adulto'
    if numero < 120:
        return 'Eres un adulto mayor'
    return 'Eres Mumm-Ra'
