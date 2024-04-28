def vive_en(ciudad: str, clientes: list) -> int:
    """
    Devuelve el índice del primer cliente que vive en la ciudad especificada,
    o AUSENTE si no se encuentra ninguno.
    """
    # Índices mínimo y máximo de la tabla de clientes
    i_min = 0
    i_max = len(clientes) - 1
    
    # Índice del siguiente cliente a observar
    i = i_min
    
    # Inicialización del resultado
    resultado = -1  # AUSENTE
    
    # Bucle de búsqueda
    while i <= i_max and resultado == -1:
        # Si el número del cliente no está vacío y vive en la ciudad especificada
        if clientes[i]["número"] != "" and clientes[i]["p"]["dirección"]["ciudad"] == ciudad:
            resultado = i
        else:
            i += 1
    
    return resultado

# Ejemplo de uso
clientes = [
    {"número": "1", "p": {"dirección": {"ciudad": "TOLEDO"}}},
    {"número": "2", "p": {"dirección": {"ciudad": "MADRID"}}},
    {"número": "3", "p": {"dirección": {"ciudad": "TOLEDO"}}},
    {"número": "4", "p": {"dirección": {"ciudad": "BARCELONA"}}},
]

ciudad_buscada = "TOLEDO"
indice_cliente = vive_en(ciudad_buscada, clientes)

if indice_cliente != -1:
    print(f"El primer cliente que vive en {ciudad_buscada} tiene el número {clientes[indice_cliente]['número']}.")
else:
    print(f"No se encontraron clientes que vivan en {ciudad_buscada}.")
