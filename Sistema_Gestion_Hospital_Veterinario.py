# Sistema de gestión hospital veterinario 
# Autores: Norman Raúl Aya, Laura Camila Parra
# Fecha: 15 de abril de 2026
# =============================================================
from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento= documento

    @abstractmethod
    def mostrar_rol(self):
        pass

class Recepcionista(Persona):
    def __init__(self, nombre, documento, turno):
        super().__init__(nombre, documento)
        self.turno = turno

    def mostrar_rol(self):
        print(f"Recepcionista: {self.nombre}, Turno: {self.turno}")
    
class Veterinario(Persona):
    def __init__(self, nombre, documento, especialidad):
        super().__init__(nombre, documento)
        self.especialidad = especialidad

    def mostrar_rol(self):
        print(f"Veterinario: {self.nombre}, Especialidad: {self.especialidad}")

class Cliente(Persona):
    def __init__(self, nombre, documento, celular, direccion):
        super().__init__(nombre, documento)
        self.celular = celular
        self.direccion = direccion
        self.mascotas = []
        
    def mostrar_rol(self):
        print(f"Cliente: {self.nombre}, Documento: {self.documento}, Celular: {self.celular}, Dirección: {self.direccion}")
        
    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)
        
    def mostrar_mascotas(self):
        if not self.mascotas:
            print("El cliente no tiene mascotas registradas.")
            return
        for i, mascota in enumerate(self.mascotas, start=1):
            print(f"{i}. ", end="")
            mascota.mostrar_info()

class Mascota:
    def __init__(self, nombre, especie, raza, edad, peso):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.peso = peso

    def mostrar_info(self):
        print(f"Mascota: {self.nombre} de especie {self.especie} y raza {self.raza} con una edad de {self.edad} años y un peso de {self.peso} kg.")

class Tratamiento:
    def __init__(self, nombre, costo, duracion_dias, recomendaciones):
        self.nombre = nombre
        self.costo = costo 
        self.duracion_dias = duracion_dias
        self.recomendaciones = recomendaciones
    
    def mostrar_tratamiento(self):
        print(f"Tratamiento: {self.nombre}")
        print(f"- Costo: ${self.costo:,.0f}")
        print(f"- Duración: {self.duracion_dias} días")
        print(f"- Recomendaciones: {self.recomendaciones}")
    
class Consulta:
    def __init__(self, mascota, veterinario, motivo):
        self.mascotas = mascota
        self.veterinario = veterinario
        self.motivo = motivo
        self.diagnostico = ""
        self.tratamiento = []
    
    def crear_tratamiento(self, nombre, costo, duracion, recomendaciones):
        agregar_tratamientos = Tratamiento(nombre, costo, duracion, recomendaciones)
        self.tratamiento.append(agregar_tratamientos)
    
    def costo_Consulta(self):
        costo_Consulta = sum(tratamiento.costo for tratamiento in self.tratamiento)
        return costo_Consulta
    
    def mostrar_resumen(self):
        print("====================== DETALLES DE LA CONSULTA ======================")
        print(f"Consulta para {self.mascotas.especie} de nombre {self.mascotas.nombre}")
        print(f"Con el veterinario {self.veterinario.nombre}")
        print(f"Motivo: {self.motivo}")
        if self.diagnostico:
            print(f"- Diagnóstico : {self.diagnostico}")
        if self.tratamiento:
            for tratamiento in self.tratamiento:
                tratamiento.mostrar_tratamiento()
        else:
            print("- Tratamientos: No se ha registrado tratamiento aún")
        print(f"\n  Total : ${self.costo_Consulta():,.0f}")
        print("=====================================================================")

class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto):
        pass

class PagoEfectivo(MetodoPago):
    def procesar_pago(self, monto):
        print(f"  Pago en EFECTIVO procesado: ${monto:,.0f}")

class PagoTarjeta(MetodoPago):
    def __init__(self, ultimos_digitos):
        self.ultimos_digitos = ultimos_digitos

    def procesar_pago(self, monto):
        print(f"  Pago con TARJETA (****{self.ultimos_digitos}) procesado: ${monto:,.0f}")

class PagoTransferencia(MetodoPago):
    def __init__(self, banco):
        self.banco = banco

    def procesar_pago(self, monto):
        print(f"  Transferencia via {self.banco} procesada: ${monto:,.0f}")

class Factura:
    IMPUESTO = 0.19

    def __init__(self, consulta):
        self.consulta = consulta
        self.subtotal = 0
        self.impuesto = 0
        self.total = 0

    def calcular_total(self):
        self.subtotal = self.consulta.costo_Consulta() - self.consulta.costo_Consulta() * self.IMPUESTO
        self.impuesto = self.consulta.costo_Consulta() * self.IMPUESTO
        self.total = self.subtotal + self.impuesto
        return self.total

def solo_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("¡Este campo no puede estar vacío. Intenta de nuevo!")

def solo_numero(mensaje, tipo=float):
    while True:
        try:
            valor = tipo(input(mensaje).strip())
            if valor <= 0:
                print("¡El valor debe ser mayor a cero!")
                continue
            return valor
        except ValueError:
            print("¡No es un número válido. Intenta de nuevo!")

def seleccionar_opcion(mensaje, opcion_valida):
    while True:
        valor = input(mensaje).strip()

        if valor == "":
            continue

        elif not valor.isdigit():
            print("¡Debes escribir solo números!")

        elif valor in opcion_valida:
            return valor

        else:
            print(f"¡Opción inválida. Elige entre: {', '.join(opcion_valida)}!")

def encabezado(opcion_elegida):
    print()
    print("=====================================================================")
    print(f"                 {opcion_elegida}")
    
def listar(coleccion, etiqueta):
    if not coleccion:
        print(f"  (no hay {etiqueta} registrados aún)")
        return False
    for i, item in enumerate(coleccion, 1):
        print(f"  {i}. ", end="")
        if hasattr(item, 'mostrar_rol'):
            item.mostrar_rol()
        elif hasattr(item, 'mostrar_info'):
            item.mostrar_info()
        elif hasattr(item, 'mostrar_resumen'):
            item.mostrar_resumen()
    return True

def elegir_de_lista(coleccion, etiqueta):
   
    if not listar(coleccion, etiqueta):
        return None
    while True:
        try:
            num_elegido = int(input(f" Elige el número de {etiqueta}: ").strip())
            if 1 <= num_elegido <= len(coleccion):
                return coleccion[num_elegido - 1]
            print(f"¡Número fuera de rango (1-{len(coleccion)})!")
        except ValueError:
            print("¡Escribe solo el número!")

def registrar_veterinario(veterinarios):
    encabezado("DATOS DEL VETERINARIO\n")
    nombre = solo_texto("Nombre del veterinario: ")
    documento = solo_texto("Número de documento: ")
    especialidad = solo_texto("Especialidad: ")
    vet = Veterinario(nombre, documento, especialidad)
    veterinarios.append(vet)
    print(f"\nVeterinario '{nombre}' registrado correctamente.")

def ver_veterinarios(veterinarios):
    encabezado("LISTA DE VETERINARIOS\n")
    listar(veterinarios, "veterinarios")

def registrar_cliente(clientes):
    encabezado("DATOS DEL CLIENTE\n")
    nombre = solo_texto("Nombre del cliente: ")
    documento = solo_texto("Número de documento: ")
    telefono  = solo_texto("Teléfono: ")
    direccion = solo_texto("Dirección:")
    cliente = Cliente(nombre, documento, telefono, direccion)
    clientes.append(cliente)
    print(f"\nCliente '{nombre}' registrado correctamente.")

def ver_clientes(clientes):
    encabezado("CLIENTES REGISTRADOS\n")
    listar(clientes, "clientes")

def registrar_mascota(clientes):
    encabezado("DATOS DE LA MASCOTA\n")
    if not clientes:
        print("¡Primero debes registrar al menos un cliente!")
        return

    print("¿A qué cliente pertenece la mascota?")
    cliente= elegir_de_lista(clientes,  "cliente")
    if not cliente:
        return

    nombre = solo_texto("Nombre de la mascota:")
    especie = solo_texto("Especie (Perro, gato, etc): ")
    raza = solo_texto("Raza: ")
    edad = solo_numero("Edad en años: ", tipo=int)
    peso = solo_numero("Peso en kg: ", tipo=float)

    mascota = Mascota(nombre, especie, raza, edad, peso)
    cliente.agregar_mascota(mascota)
    print(f"\nMascota '{nombre}' agregada a la cuenta de {cliente.nombre}.")

def ver_mascotas_de_cliente(clientes):
    encabezado("VER MASCOTAS DE UN CLIENTE\n")
    if not clientes:
        print("¡No hay clientes registrados!")
        return
    cliente = elegir_de_lista(clientes, "cliente")
    if cliente:
        print(f"\nMascotas de {cliente.nombre}:")
        cliente.mostrar_mascotas()

def registrar_consulta(clientes, veterinarios, consultas):
    encabezado("REGISTRAR LA CONSULTA:\n")
    if not clientes:
        print("Primero registra un cliente.")
        return
    if not veterinarios:
        print("Primero registra un veterinario.")
        return

    print("Selecciona el cliente:")
    cliente = elegir_de_lista(clientes, "cliente")
    if not cliente:
        return

    if not cliente.mascotas:
        print(f"{cliente.nombre} no tiene mascotas registradas.")
        return

    print(f"\nMascotas de {cliente.nombre}:")
    mascota = elegir_de_lista(cliente.mascotas, "mascota")
    if not mascota:
        return

    print("\nSelecciona el veterinario:")
    vet = elegir_de_lista(veterinarios, "veterinario")
    if not vet:
        return

    motivo = solo_texto("\nMotivo de la consulta: ")
    diagnostico = solo_texto("Diagnóstico: ")

    consulta = Consulta(mascota, vet, motivo)
    consulta.diagnostico = diagnostico
    consultas.append(consulta)

    # vet.atender_mascota(mascota)
    print(f"\nConsulta registrada para {mascota.nombre}.")

    print("\nAhora agrega los tratamientos (mínimo 1).")
    agregar_tratamientos(consulta)

def agregar_tratamientos(consulta):
    while True:
        encabezado("INFORMACIÓN DEL TRATAMIENTO\n")
        nombre = solo_texto("Nombre del tratamiento: ")
        costo = solo_numero("Costo : $", tipo=float)
        duracion = solo_numero("Duración(días): ", tipo=int)
        recomendaciones = solo_texto("Recomendaciones: ")

        consulta.crear_tratamiento(nombre, costo, duracion, recomendaciones)
        print(f"Tratamiento '{nombre}' agregado.")

        while True:
            otro = input("\n¿Agregar otro tratamiento? (s/n): ").strip().lower()
            if otro in ["s", "n"]:
                break
            print("¡Opción inválida. Escribe 's' o 'n'.\n")

        if otro == "n":
            break

def ver_consultas(consultas):
    encabezado("CONSULTAS REGISTRADAS\n")
    if not consultas:
        print("¡No hay consultas registradas!")
        return
    for i, c in enumerate(consultas, 1):
        print(f"\nConsulta #{i}")
        c.mostrar_resumen()

def generar_factura(consultas):
    encabezado("GENERAR FACTURA Y PAGAR\n")

    if not consultas:
        print("  No hay consultas registradas.")
        return

    con_tratamientos = [c for c in consultas if c.tratamiento]

    if not con_tratamientos:
        print("  Ninguna consulta tiene tratamientos aún.")
        return

    print("  Selecciona la consulta a facturar:")
    for i, c in enumerate(con_tratamientos, 1):
        print(f"  {i}. {c.mascotas.nombre} - {c.motivo} (${c.costo_Consulta():,.0f})")

    while True:
        try:
            num = int(input("\n  Elige el número de consulta: ").strip())
            if 1 <= num <= len(con_tratamientos):
                consulta = con_tratamientos[num - 1]
                break
            print(f"  ¡Número fuera de rango (1-{len(con_tratamientos)})!")
        except ValueError:
            print("  ¡Escribe solo el número!")

    factura = Factura(consulta)
    factura.calcular_total()

    print()
    print("=====================================================================")
    print("                   FACTURA - HOSPITAL VETERINARIO")
    print("=====================================================================")
    print(f"  Paciente  : {consulta.mascotas.nombre}")
    print(f"  Subtotal  : ${factura.subtotal:,.0f}")
    print(f"  IVA (19%) : ${factura.impuesto:,.0f}")
    print(f"  TOTAL     : ${factura.total:,.0f}")
    print("=====================================================================")

    while True:
        print()
        print("  Métodos de pago disponibles:")
        print("  1. Efectivo")
        print("  2. Tarjeta")
        print("  3. Transferencia")

        opcion = seleccionar_opcion("  Elige el método (1/2/3): ", ["1", "2", "3"])

        if opcion == "1":
            metodo = PagoEfectivo()
            nombre_metodo = "Efectivo"
        elif opcion == "2":
            digitos = solo_texto("  Últimos 4 dígitos de la tarjeta: ")
            metodo = PagoTarjeta(digitos)
            nombre_metodo = "Tarjeta"
        else:
            banco = solo_texto("  Nombre del banco: ")
            metodo = PagoTransferencia(banco)
            nombre_metodo = "Transferencia"

        print(f"\n  Método seleccionado: {nombre_metodo}")
        print("  1. Confirmar y pagar")
        print("  2. Cambiar método de pago")

        decision = seleccionar_opcion("  ¿Qué deseas hacer? (1/2): ", ["1", "2"])

        if decision == "1":
            metodo.procesar_pago(factura.total)
            print("  ¡Pago exitoso. Hasta la próxima!")
            break
        else:
            print("\n  Volviendo a los métodos de pago...")
   
def menu_principal():
    veterinarios = []
    clientes     = []
    consultas    = []

    while True:
        print()
        print("=====================================================================")
        print("            SISTEMA DE GESTIÓN - HOSPITAL VETERINARIO")
        print("=====================================================================")

        print("  1. Registrar veterinario")
        print("  2. Ver veterinarios")
        print("  3. Registrar cliente")
        print("  4. Ver clientes")
        print("  5. Agregar mascota a un cliente")
        print("  6. Ver mascotas de un cliente")
        print("  7. Registrar consulta (con tratamientos)")
        print("  8. Ver consultas")
        print("  9. Generar factura y pagar")
        print("  0. Salir")
        print("=====================================================================")


        opcion = seleccionar_opcion("  Elige una opción: ",
                              ["0","1","2","3","4","5","6","7","8","9"])

        if opcion == "1":
            registrar_veterinario(veterinarios)
        elif opcion == "2":
            ver_veterinarios(veterinarios)
        elif opcion == "3":
            registrar_cliente(clientes)
        elif opcion == "4":
            ver_clientes(clientes)
        elif opcion == "5":
            registrar_mascota(clientes)
        elif opcion == "6":
            ver_mascotas_de_cliente(clientes)
        elif opcion == "7":
            registrar_consulta(clientes, veterinarios,  consultas)
        elif opcion == "8":
            ver_consultas(consultas)
        elif opcion == "9":
            generar_factura(consultas)
        elif opcion == "0":
            print("\n  Sesión terminada\n")
            break

if __name__ == "__main__":
    menu_principal()