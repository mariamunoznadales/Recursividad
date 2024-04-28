def organizar_fichas(fichas):
    # Contadores para el número de fichas de cada color
    num_rojas = 0
    num_verdes = 0
    num_azules = 0
    
    # Recorremos las fichas y contamos cuántas hay de cada color
    for ficha in fichas:
        if ficha == 'roja':
            num_rojas += 1
        elif ficha == 'verde':
            num_verdes += 1
        elif ficha == 'azul':
            num_azules += 1
    
    # Índices para la próxima ficha de cada color
    proxima_roja = 0
    proxima_verde = num_rojas
    proxima_azul = num_rojas + num_verdes
    
    # Organizamos las fichas
    for ficha in fichas:
        if ficha == 'roja':
            # Colocamos la próxima ficha roja en su posición correspondiente
            fichas[proxima_roja] = 'roja'
            proxima_roja += 1
        elif ficha == 'verde':
            # Colocamos la próxima ficha verde en su posición correspondiente
            fichas[proxima_verde] = 'verde'
            proxima_verde += 1
        elif ficha == 'azul':
            # Colocamos la próxima ficha azul en su posición correspondiente
            fichas[proxima_azul] = 'azul'
            proxima_azul += 1
    
    return fichas

# Ejemplo de uso
fichas = ['roja', 'azul', 'verde', 'verde', 'roja', 'roja', 'azul', 'verde', 'roja', 'azul', 'azul', 'azul', 'verde', 'roja', 'verde', 'roja', 'roja']
fichas_organizadas = organizar_fichas(fichas)
print(fichas_organizadas)
