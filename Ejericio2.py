class Mision:
    def __init__(self, tipo, reino_destino, dios_solicitante):
        self.tipo = tipo
        self.reino_destino = reino_destino
        self.dios_solicitante = dios_solicitante

def asignar_recursos(misiones):
    recursos_asignados = {
        'Valkirias': 0,
        'Unidades': 0
    }
    
    for mision in misiones:
        if mision.dios_solicitante in ['Odín', 'Loki']:
            recursos_asignados['Valkirias'] += 10
            recursos_asignados['Unidades'] += 20
        else:
            if mision.tipo == 'defensa':
                recursos_asignados['Valkirias'] += 5
                recursos_asignados['Unidades'] += 10
            elif mision.tipo == 'exploración':
                recursos_asignados['Valkirias'] += 3
                recursos_asignados['Unidades'] += 5
            elif mision.tipo == 'conquista':
                recursos_asignados['Valkirias'] += 7
                recursos_asignados['Unidades'] += 15
    
    return recursos_asignados

def main():
    misiones = []
    
    while True:
        print("\n--- Nueva Solicitud de Misión ---")
        tipo = input("Tipo de misión (defensa, exploración, conquista): ")
        reino_destino = input("Reino destino: ")
        dios_solicitante = input("Dios que solicita la misión (Odín o Loki): ")
        
        nueva_mision = Mision(tipo, reino_destino, dios_solicitante)
        misiones.append(nueva_mision)
        
        continuar = input("¿Desea agregar otra solicitud de misión? (s/n): ")
        if continuar.lower() != 's':
            break
    
    recursos_asignados = asignar_recursos(misiones)
    print("\nRecursos asignados:")
    print("Valkirias:", recursos_asignados['Valkirias'])
    print("Unidades:", recursos_asignados['Unidades'])

if __name__ == "__main__":
    main()
