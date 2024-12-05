import pymysql

# Conexión a la base de datos MariaDB/MySQL
# Reemplaza 'localhost', 'root' y 'Eynar2805' por los valores correspondientes osea mi usuario y contra

conn = pymysql.connect(
    host='localhost',  # Host donde se encuentra la base de datos (en este caso, es local)
    user='root',  # colocas tu usuario
    password='Eynar2805',  # Contraseña de mi usuario  ''
    database='libro_recetas'  # Nombre de la base de datos a la que se conectara
)

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear tabla 'recetas' si no existe ya en la base de datos
# Esta tabla tiene 4 columnas: id (clave primaria), los nombres, los ingredientes, y los pasos pasos
cursor.execute('''CREATE TABLE IF NOT EXISTS recetas (
                    id INT AUTO_INCREMENT PRIMARY KEY,  # id autoincremental para cada receta
                    nombre VARCHAR(255) NOT NULL,  # nombre de la receta, no puede ser nulo
                    ingredientes TEXT NOT NULL,  # ingredientes de la receta, tipo TEXT
                    pasos TEXT NOT NULL  # pasos de la receta, tipo TEXT
                )''')

# Función para agregar una nueva receta a la base de datos
def agregar_receta():

    # Se solicita al usuario los datos de la nueva receta
    nom = input("Nombre de la receta: ")
    ingredientes = input("Ingredientes (separados por comas): ")
    pasos = input("Pasos para la receta: ")

    # Insertar la nueva receta en la tabla 'recetas'
    cursor.execute("INSERT INTO recetas (nombre, ingredientes, pasos) VALUES (%s, %s, %s)",
                   (nom, ingredientes, pasos))

    # Guardar los cambios en la base de datos
    conn.commit()
    print("Receta agregada con éxito.")


# Función para actualizar una receta existente en la base de datos
def actualizar_receta():

    # Solicitar al usuario el ID de la receta que quiere actualizar
    receta_id = input("ID de la receta a actualizar: ")
    # Solicitar nuevos datos para la receta
    nom = input("Nuevo nombre de la receta: ")
    ingredientes = input("Nuevos ingredientes (separados por comas): ")
    pasos = input("Nuevos pasos: ")

    # Actualizar los datos de la receta en la base de datos
    cursor.execute("UPDATE recetas SET nombre = %s, ingredientes = %s, pasos = %s WHERE id = %s",
                   (nom, ingredientes, pasos, receta_id))

    # Guardar los cambios en la base de datos
    conn.commit()
    print("Receta actualizada con éxito.")

# Función para eliminar una receta de la base de datos
def eliminar_receta():

    # Solicitar al usuario el ID de la receta que quiere eliminar
    receta_id = input("ID (número al lado izquierdo de la receta) de la receta a eliminar: ")

    # Eliminar la receta de la base de datos utilizando su ID
    cursor.execute("DELETE FROM recetas WHERE id = %s", (receta_id,))
    # Guardar los cambios en la base de datos
    conn.commit()
    print("Receta eliminada con éxito.")

# Función para mostrar todas las recetas en la base de datos
def ver_recetas():
    # Ejecutar una consulta para obtener todas las recetas (solo id y nombre)

    cursor.execute("SELECT id, nombre FROM recetas")
    recetas = cursor.fetchall()  # Obtener todos los resultados de la consulta

    # Si hay recetas, se muestran, si no, se indica que no hay
    if recetas:
        print("Listado de recetas:")
        for receta in recetas:
            print(f"{receta[0]}: {receta[1]}")  # Mostrar el id y el nombre de la receta
    else:
        print("No hay recetas disponibles.")

# Función para buscar una receta por nombre y mostrar sus detalles
def buscar_receta():
    # Solicitar al usuario el nombre de la receta que quiere buscar
    nombre = input("Nombre de la receta a buscar: ")

    # Ejecutar la consulta para buscar la receta por nombre
    cursor.execute("SELECT ingredientes, pasos FROM recetas WHERE nombre = %s", (nombre,))
    resultado = cursor.fetchone()  # Obtener el primer resultado (debería ser único)

    # Si se encuentra la receta, mostrar sus ingredientes y pasos; si no, indicar que no se encontró
    if resultado:
        print(f"Ingredientes: {resultado[0]}")
        print(f"Pasos: {resultado[1]}")
    else:
        print("Receta no encontrada.")

# Función principal para mostrar el menú y manejar las opciones
def menu():

    while True:  # Ciclo infinito que mantiene el menú hasta que el usuario elige salir
        print("\n--- Libro de Recetas ---")
        print("1. Agregar nueva receta")
        print("2. Actualizar receta existente")
        print("3. Eliminar receta")
        print("4. Ver listado de recetas")
        print("5. Buscar ingredientes y pasos de receta")
        print("6. Salir")

        # Solicitar al usuario una opción del menú
        opcion = input("Selecciona una opción: ")

        # Según la opción, se llama a la función correspondiente
        if opcion == '1':
            agregar_receta()
        elif opcion == '2':
            actualizar_receta()
        elif opcion == '3':
            eliminar_receta()
        elif opcion == '4':
            ver_recetas()
        elif opcion == '5':
            buscar_receta()
        elif opcion == '6':
            print("Saliendo...")
            break  # Salir del ciclo y terminar el programa
        else:
            print("Opción no válida. Inténtalo de nuevo.")  # Manejar opción inválida

# Punto de entrada del programa
if __name__ == '__main__':
    # Ejecutar el menú principal
    menu()

# Cerrar la conexión a la base de datos cuando termine el programa
conn.close()







