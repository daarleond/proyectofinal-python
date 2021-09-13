#Se realizan las importaciones del archivo lifestore_file.py
from lifestore_file import lifestore_searches
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_products
#se importa la libreria para manejar fechas
from datetime import datetime
#Se importa la libreria para realizar delay
import time
#Se importa la librería para formatear los ingresos en moneda
import locale
locale.setlocale( locale.LC_ALL, '' )

#El while funciona para crear un ciclo para poder regresar al ingreso de usuario y contraseña
while True:

  #Se genera una lista de usuarios y contraseñas para poder ingresar al sistema
  lista_usuarios=[["dario","progpython"],["juan","python123"],["david","admin1234"]]

  #Se inicializa variable acceso
  acceso=0

  #Se crea una interfaz de Bienvenida ademas de inputs para guardar en las variables user y contra el usuario y contraseña ingresados
  print("\n::::::::::Bienvenido:::::::::: \n ")
  user=input("Ingrese Usuario: ")
  contra=input("Ingrese Contraseña: ")

  #El ciclo for entra a la lista_usuarios para revisar cada elemento y la sentencia if valida si el usuario y contraseña coinciden con los de la lista_usuarios
  for usuario in lista_usuarios:
    if usuario[0] == user and usuario[1] == contra:
      #Si coincide, la variable acceso cambia a 1
      acceso=1

  #Si acceso es igual a 1, entra a todas las opciones del programa
  if acceso == 1:
    #El ciclo while funciona para crear un ciclo que permitirá regresar al menú principal
    while True:

      #Se crea una interfaz para navegar por las opciones del programa, ademas de una opción de salir a la seleccion de usuarios. El input recibe un valor en la variable seleccion para poder capturar la opcion del usuario que seran validadas mediante sentencias if
      print("\n::::::::::Menú::::::::::")
      print("1. Top 10 productos con mayores ventas\n 2. Top 10 productos con mayores búsquedas\n 3. Top 10 productos con menores ventas (Por categoría)\n 4. Top 10 productos con menores busquedas (Por categoría)\n 5. Top 20 Productos con mejores reseñas\n 6. Top 20 Productos con peores reseñas\n 7. Total de Ingresos Mensuales y Ventas promedio Mensuales\n 8. Total Anual y Meses con más ventas\n 9. Salir...")
      seleccion=input("\nSeleccion: ")

      #Con la sentencia if realiza la validacion para entrar al bloque de instrucciones pertenciente al Top 10 de productos con mayores ventas, si es ingresado el numero 1
      if seleccion == "1":
        #Se inicializa una variable n en 0 que servira de acumulador en el conteo de ventas totales
        n=0
        #Se inicializa una lista para posteriormente añadir los valores finales
        lifestore_productoventa = []
        #El primer ciclo for itera la lista lifestore_products por medio de indices
        for i in range(len(lifestore_products)): 
          #El siguiente ciclo for itera la lista lifestore_sales por medio de indices
          for j in range(len(lifestore_sales)):   
            #Con la sentencia if se realiza una validacion en donde la condicion indica que si en cada elemento 1 de cada sublista de la lista lifestore_sales (id_producto) coincide con el elemento 0 de cada sublista de la lista lifestore_products (id_producto) ejecutara las siguientes instrucciones. Esto para relacionar ambas listas con cada producto y cada venta
            if lifestore_sales[j][1] == lifestore_products[i][0]: 
              #El contador n de ventas totales 
              n=n+1
          #Se añade a la lista los datos que se van a mostrar (Id de cada producto, Nombre de cada producto y su contador de ventas totales )
          lifestore_productoventa.append([lifestore_products[i][0],lifestore_products[i][1],n])
          n=0

        #en una nueva lista, se realiza una funcion sorted, con un valor de reverse=True para ordenar los datos de la lista lifestore_productoventa con filtro en las ventas para obtener los productos con mayores ventas
        lifestore_masvendidos=sorted(lifestore_productoventa, key = lambda x: int(x[2]),reverse=True)

        n=0
        #Este ciclo permite recorrer la lista lifestore_masvendidos previamente ordenada en un rango de 0 a 10 para mostrar solo los 10 productos con mayores ventas 
        for x in lifestore_masvendidos[0:10]:
          #Con el print y los indices de la lista, se organiza de manera que el usuario pueda ver los datos con una mejor representacion
          print("Id Producto:",x[0],"| Nombre: ",x[1]," |No. Ventas: ",x[2])
        #Con esta funcion se realiza una espera de 3 segundos.
        time.sleep(3)

      #------------------------------------------------------
      #Con la sentencia elif realiza la validacion para entrar al bloque de instrucciones pertenciente al Top 10 de productos con mayores busquedas, si es ingresado el numero 2

      elif seleccion == "2":
        #Se inicializa una variable n en 0 que servira de acumulador en el conteo de busquedas totales
        n=0
        #Se inicializa una lista para posteriormente añadir los valores finales
        lifestore_productobusqueda = []
        #El primer ciclo for itera la lista lifestore_products por medio de indices       
        for i in range(len(lifestore_products)): 
          #El siguiente ciclo for itera la lista lifestore_searches por medio de indices
          for j in range(len(lifestore_searches)):
            #Con la sentencia if se realiza una validacion en donde la condicion indica que si en cada elemento 1 de cada sublista de la lista lifestore_searches(id_producto) coincide con el elemento 0 de cada sublista de la lista lifestore_products (id_producto) ejecutara las siguientes instrucciones. Esto para relacionar ambas listas con cada producto y cada venta   
            if lifestore_searches[j][1] == lifestore_products[i][0]:
              #El contador n de busquedas totales
              n=n+1
          #Se añade a la lista los datos que se van a mostrar (Id de cada producto, Nombre de cada producto y su contador de busquedas totales )
          lifestore_productobusqueda.append([lifestore_products[i][0],lifestore_products[i][1],n])
          n=0
        #en una nueva lista, se realiza una funcion sorted, con un valor de reverse=True para ordenar los datos de la lista lifestore_productoventa con filtro en el total de busquedas para obtener los productos con mayores busquedas
        lifestore_masbuscados=sorted(lifestore_productobusqueda, key = lambda x: int(x[2]),reverse=True)

        n=0
        #Este ciclo permite recorrer la lista lifestore_masbuscados previamente ordenada en un rango de 0 a 10 para mostrar solo los 10 productos con mayores busquedas
        for x in lifestore_masbuscados[0:10]:
          #Con el print y los indices de la lista, se organiza de manera que el usuario pueda ver los datos con una mejor representacion
          print("Id Producto:",x[0],"| Nombre: ",x[1]," |No. de Búsquedas: ",x[2])
        #Con esta funcion se realiza una espera de 3 segundos.
        time.sleep(3)

      #------------------------------------------------------
      #Con la sentencia elif realiza la validacion para entrar al bloque de instrucciones pertenciente al Top 10 de productos con menores ventas, si es ingresado el numero 3
      elif seleccion == "3":
        #El ciclo while funciona para crear un ciclo que permitirá regresar al menú principal
        while True:
          #Se crea una interfaz para navegar por las categorias de los productos, ademas de una opción para regresar al menu principal. El input recibe un valor en la variable seleccion para poder capturar la opcion del usuario que seran validadas mediante sentencias if
          print("\nCategorías:\n 1. Procesadores\n 2. Tarjetas de video\n 3. Tarjetas madre\n 4. Discos duros\n 5. Memorias USB\n 6. Pantallas\n 7. Bocinas\n 8. Audifonos\n 9. Regresar")
          seleccioncat=input("\nElegir Categoría (1-9): ")
          #Se inicializa una variable n en 0 que servira de acumulador en el conteo de ventas totales
          n=0
          
          #Se valida si la seleccion del usuario es igual a 1 al 8
          if seleccioncat == "1":
            #Si la seleccion es 1 la variable "var" toma el valor de "procesadores"
            var="procesadores"
          elif seleccioncat == "2":
            #Si la seleccion es 2 la variable "var" toma el valor de "tarjetas de video"
            var="tarjetas de video"
          elif seleccioncat == "3":
            #Si la seleccion es 3 la variable "var" toma el valor de "tarjetas madre"
            var="tarjetas madre"
          elif seleccioncat == "4":
            #Si la seleccion es 4 la variable "var" toma el valor de "discos duros"
            var="discos duros"
          elif  seleccioncat == "5":
            #Si la seleccion es 5 la variable "var" toma el valor de "memorias usb"
            var="memorias usb"
          elif  seleccioncat == "6":
            #Si la seleccion es 6 la variable "var" toma el valor de "pantallas"
            var="pantallas"
          elif seleccioncat == "7":
            #Si la seleccion es 7 la variable "var" toma el valor de "bocinas"
            var="bocinas"
          elif  seleccioncat == "8":
            #Si la seleccion es 8 la variable "var" toma el valor de "audifonos"
            var="audifonos"
          elif seleccioncat == "9":
            #Si la seleccion es 9 se regresa al menu principal
            print("Regresando al menú anterior...")
            time.sleep(3)
            #El break permite salir de este ciclo y regresar al menu anterior
            break
          #El ciclo while funciona para crear un ciclo que permitirá regresar al menú de seleccion de categoria 
          while True:
            #Se inicializa una lista para posteriormente añadir los valores finales
            lifestore_productoventacat = []
            #El primer ciclo for itera la lista lifestore_products por medio de indices
            for i in range(len(lifestore_products)):
              #La sentencia if valida si cada sublista en su posicion 3 es identico a la variable var. Si la categoria es identica a la que el usuario quiere visualizar
              if lifestore_products[i][3] == var:
                #El siguiente ciclo for itera la lista lifestore_sales por medio de indices 
                for j in range(len(lifestore_sales)):   
                  #Con la sentencia if se realiza una validacion en donde la condicion indica que si en cada elemento 1 de cada sublista de la lista lifestore_sales (id_producto) coincide con el elemento 0 de cada sublista de la lista lifestore_products (id_producto) ejecutara las siguientes instrucciones. Esto para relacionar ambas listas con cada producto y cada venta
                  if lifestore_sales[j][1] == lifestore_products[i][0]:
                    n=n+1

                #Se añade a la lista los datos que se van a mostrar (Id de cada producto, Nombre de cada producto, no de ventas y su categoria )
                lifestore_productoventacat.append([lifestore_products[i][0],lifestore_products[i][1],n,lifestore_products[i][3]])
                n=0
            #en una nueva lista, se realiza una funcion sorted, reverse=True para ordenar los datos de la lista lifestore_productoventacat con filtro en las ventas para obtener los productos con menores ventas por cada categoria
            lifestore_menosvendidoscat=sorted(lifestore_productoventacat, key = lambda x: int(x[2]))

            n=0
            
            #Este ciclo permite recorrer la lista lifestore_menosvendidoscat previamente ordenada en un rango de 0 a 10 para mostrar solo los 10 productos con menores ventas
            for x in lifestore_menosvendidoscat[0:10]:
              #Con el print y los indices de la lista, se organiza de manera que el usuario pueda ver los datos con una mejor representacion
              print("Id Producto:",x[0],"| Nombre: ",x[1]," |No. Ventas: ",x[2]," |Categoría: ",x[3])
            
            #Se reinicializan las variables, hay una espera de 3 segundos y posteriormente el break permite salir al menu de eleccion de categoria
            lifestore_menosvendidoscat=[]
            lifestore_productoventacat = []
            time.sleep(3)
            break
      #------------------------------------------------------
      #Con la sentencia elif realiza la validacion para entrar al bloque de instrucciones pertenciente al Top 10 de productos con menores busquedas, si es ingresado el numero 4

      elif seleccion == "4":
        #El ciclo while funciona para crear un ciclo que permitirá regresar al menú principal
        while True:
          #Se crea una interfaz para navegar por las categorias de los productos, ademas de una opción para regresar al menu principal. El input recibe un valor en la variable seleccion para poder capturar la opcion del usuario que seran validadas mediante sentencias if
          print("\nCategorías:\n 1. Procesadores\n 2. Tarjetas de video\n 3. Tarjetas madre\n 4. Discos duros\n 5. Memorias USB\n 6. Pantallas\n 7. Bocinas\n 8. Audifonos\n 9. Regresar")
          seleccioncat=input("\nElegir Categoría (1-9): ")
          #Se inicializa una variable n en 0 que servira de acumulador en el conteo de busquedas totales
          n=0
          
          #Se valida si la seleccion del usuario es igual a 1 al 8 y la variable "var" toma el valor segun sea el caso
          if seleccioncat == "1":
            var="procesadores"
          elif seleccioncat == "2":
            var="tarjetas de video"
          elif seleccioncat == "3":
            var="tarjetas madre"
          elif seleccioncat == "4":
            var="discos duros"
          elif  seleccioncat == "5":
            var="memorias usb"
          elif  seleccioncat == "6":
            var="pantallas"
          elif seleccioncat == "7":
            var="bocinas"
          elif  seleccioncat == "8":
            var="audifonos"
          elif seleccioncat == "9":
            print("Regresando al menú anterior...")
            time.sleep(3)
            #El break permite salir de este ciclo y regresar al menu anterior
            break
          
          #El ciclo while funciona para crear un ciclo que permitirá regresar al menú de seleccion de categoria
          while True:
            #Se inicializa una lista para posteriormente añadir los valores finales
            lifestore_productobuscat = []
            #El primer ciclo for itera la lista lifestore_products por medio de indices
            for i in range(len(lifestore_products)):
              #La sentencia if valida si cada sublista en su posicion 3 es identico a la variable var. Si la categoria es identica a la que el usuario quiere visualizar
              if lifestore_products[i][3] == var: 
                #El siguiente ciclo for itera la lista lifestore_sales por medio de indices
                for j in range(len(lifestore_searches)):   
                   #Con la sentencia if se realiza una validacion en donde la condicion indica que si en cada elemento 1 de cada sublista de la lista lifestore_sales (id_producto) coincide con el elemento 0 de cada sublista de la lista lifestore_products (id_producto) ejecutara las siguientes instrucciones. Esto para relacionar ambas listas con cada producto y cada venta
                  if lifestore_searches[j][1] == lifestore_products[i][0]:
                    n=n+1
                #Se añade a la lista los datos que se van a mostrar (Id de cada producto, Nombre de cada producto, no de busquedas y su categoria )
                lifestore_productobuscat.append([lifestore_products[i][0],lifestore_products[i][1],n,lifestore_products[i][3]])
                n=0
            #en una nueva lista, se realiza una funcion sorted, reverse=True para ordenar los datos de la lista lifestore_productoventacat con filtro en las ventas para obtener los productos con menores busquedas por cada categoria
            lifestore_menosbuscat=sorted(lifestore_productobuscat, key = lambda x: int(x[2]))

            n=0
            #Este ciclo permite recorrer la lista lifestore_menosbuscat previamente ordenada en un rango de 0 a 10 para mostrar solo los 10 productos con menores ventas
            for x in lifestore_menosbuscat[0:10]:
              #Con el print y los indices de la lista, se organiza de manera que el usuario pueda ver los datos con una mejor representacion
              print("Id Producto:",x[0],"| Nombre: ",x[1]," |No. Busquedas: ",x[2]," |Categoría: ",x[3])
            #Se reinicializan las variables, hay una espera de 3 segundos y posteriormente el break permite salir al menu de eleccion de categoria
            lifestore_menosbusscat=[]
            lifestore_productobuscat = []
            time.sleep(3)
            break

      #------------------------------------------------------
      #Con la sentencia elif realiza la validacion para entrar al bloque de instrucciones pertenciente al Top 20 de productos con mejores reseñas, si es ingresado el numero 5
      elif seleccion == "5":
        #Se inicializa una variable n en 0 que servira de acumulador en el conteo de ventas totales.
        n=0
        #Se inicializa una variable suma en 0 que servira de acumulador en el conteo de las calificaciones de cada producto
        suma=0
        #Se inicializa una lista para posteriormente añadir los valores finales
        lifestore_productores = []
        #El primer ciclo for itera la lista lifestore_products por medio de indices       
        for i in range(len(lifestore_products)): 
          #El siguiente ciclo for itera la lista lifestore_searches por medio de indices
          for j in range(len(lifestore_sales)):  
            #Con la sentencia if se realiza una validacion en donde la condicion indica que si en cada elemento 1 de cada sublista de la lista lifestore_searches(id_producto) coincide con el elemento 0 de cada sublista de la lista lifestore_products (id_producto) ejecutara las siguientes instrucciones. Esto para relacionar ambas listas con cada producto y cada venta             
            if lifestore_sales[j][1] == lifestore_products[i][0]: 
              #Se suma 1 al acumulador n y se comienza a hacer la sumatoria de las calificaciones de cada producto
              n=n+1
              suma=suma + lifestore_sales[j][2]
              
          #Se realiza una validacion para que no se hagan divisiones entre 0
          if n > 0:    
            #para sacar el promedio, la sumatoria se divide entre el numero de ventas del producto
            promedio = suma/n
          else:
            promedio = 0

          if promedio > 0:
            #Se añade a la lista los datos que se van a mostrar (Id de cada producto, Nombre de cada producto, ventas totales y promedio de calificacion )
            lifestore_productores.append([lifestore_products[i][0],lifestore_products[i][1],n,round(promedio,2)])
          #Se reinicializan las variables
          n=0
          suma=0
          promedio=0
        #en una nueva lista, se realiza una funcion sorted, para ordenar los datos de la lista lifestore_masranked con filtro en el promedio de cada articulo, con valor reverse=True para visualizar los productos con mejores reseñas de mayor a menor
        lifestore_masranked=sorted(lifestore_productores, key = lambda x: float(x[3]),reverse=True)
        n=0
        #Este ciclo permite recorrer la lista lifestore_masranked previamente ordenada en un rango de 0 a 20 para mostrar solo los 20 productos con mejores reseñas    
        for x in lifestore_masranked[0:20]:
          print("Id Producto:",x[0],"| Nombre: ",x[1]," |No. Ventas: ",x[2]," |Promedio: ",x[3])
        time.sleep(3)

      #------------------------------------------------------
      #Con la sentencia elif realiza la validacion para entrar al bloque de instrucciones pertenciente al Top 20 de productos con peores reseñas, si es ingresado el numero 6
      elif seleccion == "6":
        #Se inicializa una variable n en 0 que servira de acumulador en el conteo de ventas totales.
        n=0
        #Se inicializa una variable suma en 0 que servira de acumulador en el conteo de las calificaciones de cada producto
        suma=0
        #Se inicializa una lista para posteriormente añadir los valores finales
        lifestore_productores = []
        #El primer ciclo for itera la lista lifestore_products por medio de indices       
        for i in range(len(lifestore_products)): 
          #El siguiente ciclo for itera la lista lifestore_searches por medio de indices
          for j in range(len(lifestore_sales)):   
            #Con la sentencia if se realiza una validacion en donde la condicion indica que si en cada elemento 1 de cada sublista de la lista lifestore_searches(id_producto) coincide con el elemento 0 de cada sublista de la lista lifestore_products (id_producto) ejecutara las siguientes instrucciones. Esto para relacionar ambas listas con cada producto y cada venta  
            if lifestore_sales[j][1] == lifestore_products[i][0]: 
              #Se suma 1 al acumulador n y se comienza a hacer la sumatoria de las calificaciones de cada producto
              n=n+1
              suma=suma + lifestore_sales[j][2]
              
          #para sacar el promedio, la sumatoria se divide entre el numero de ventas del producto
          if n > 0:    
            promedio = suma/n
          else:
            promedio = 0

          if promedio > 0:
            #Se añade a la lista los datos que se van a mostrar (Id de cada producto, Nombre de cada producto, ventas totales y promedio de calificacion )
            lifestore_productores.append([lifestore_products[i][0],lifestore_products[i][1],n,round(promedio,2)])
          #Se reinicializan las variables
          n=0
          suma=0
          promedio=0
        #en una nueva lista, se realiza una funcion sorted,  para ordenar los datos de la lista lifestore_menosranked con filtro en el promedio de cada articulo para visualizar los productos con peores reseñas de menor a mayor
        lifestore_menosranked=sorted(lifestore_productores, key = lambda x: float(x[3]))

        n=0
        #Este ciclo permite recorrer la lista lifestore_masranked previamente ordenada en un rango de 0 a 20 para mostrar solo los 20 productos con peores reseñas 
        for x in lifestore_menosranked[0:20]:
          print("Id Producto:",x[0],"| Nombre: ",x[1]," |No. Ventas: ",x[2]," |Promedio: ",x[3])
        time.sleep(3)

      #------------------------------------------------------
      #Con la sentencia elif realiza la validacion para entrar al bloque de instrucciones pertenciente a Total de Ingresos Mensuales y Ventas promedio mensuales, si es ingresado el numero 7
      elif seleccion == "7":
        #Se inicializa una variable n en 0 que servira de acumulador en el conteo de ventas totales del mes
        nmes = 1
        #Se inicializa una variable suma en 0 que servira de acumulador en el conteo de ingresos
        suma=0
        #Se inicializa una variable prom en 0 que servira para guardar el promedio de ingresos de junio.
        prom=0
        
        #Se inicializa una variable "months" con los nombres de cada mes para despues relacionarlos

        months = ("Enero","Febrero","Marzo","Abril","Mayo","Junio", "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
        #Se valida si la seleccion del usuario es igual a 1 al 12 correspondiente a los meses del año y la variable "seleccioncat" toma el valor segun sea el mes elegido. Esto para Homologar el input del usuario con la representacion del mes en Letra
        seleccioncat=input("\nElegir Mes (1-12): ")
        
        if seleccioncat == "1":
          var="Enero"
        elif seleccioncat == "2":
          var="Febrero"
        elif seleccioncat == "3":
          var="Marzo"
        elif seleccioncat == "4":
          var="Abril"
        elif  seleccioncat == "5":
          var="Mayo"
        elif  seleccioncat == "6":
          var="Junio"
        elif seleccioncat == "7":
          var="Julio"
        elif  seleccioncat == "8":
          var="Agosto"
        elif seleccioncat == "9":
          var="Septiembre"
        elif seleccioncat == "10":
          var="Octubre"
        elif seleccioncat == "11":
          var="Noviembre"
        elif seleccioncat == "12":
          var="Diciembre"

        #El primer ciclo for itera la lista lifestore_sales por medio de indices
        for x in range(len(lifestore_sales)):
          #Se formatea en una variable fecha_dt la fecha de cada elemento de cada sublista de lifestore_sale en su posicion 3. De manera que pueda ser manejable
          fecha_dt = datetime.strptime(lifestore_sales[x][3],"%d/%m/%Y")
         #en la variable mes se captura el mes de cada fecha para que se homologue con la representacion del mes en Letra
          mes=months[fecha_dt.month - 1]
          #Se valida si la variable mes es igual a la eleccion del mes del usuario
          if mes == var :
           #la variable nmes se incrementa + 1 para continuar con la sumatoria de los siguientes meses 
            nmes=nmes+1
            #El siguiente ciclo for itera la lista lifestore_products por medio de indices
            for y in range(len(lifestore_products)):
              #Con la sentencia if se realiza una validacion en donde la condicion indica que si en cada elemento 1 de cada sublista de la lista lifestore_sales (id_producto) coincide con el elemento 0 de cada sublista de la lista lifestore_products (id_producto) ejecutara las siguientes instrucciones. Esto para relacionar ambas listas con cada producto y cada venta
              if lifestore_sales[x][1] == lifestore_products[y][0]:
                #En la variable suma se comienza a hacer la sumatoria de los ingresos de todos los productos por mes
                suma=suma+lifestore_products[y][2]
        #Con el print se muestra la variable var (mes en cuestion) y la suma de ingresos de ese mes en una funcion locale.currency para formatearlo en moneda.
        print("Total Ingresos de",var,":", locale.currency(suma,grouping=True))
        #Con el print se muestra la variable var ademas de las ventas totales de cada mes
        print("Ventas de",var,":",nmes - 1)
        #En la variable prom, se guarda el promedio de las ventas del mes en cuestion
        prom=suma/(nmes-1)
        #Y se muestra en un print con formateo de moneda
        print("Ventas promedio de",var,":", locale.currency(prom,grouping=True))
        time.sleep(3)

      #------------------------------------------------------
      #Con la sentencia elif realiza la validacion para entrar al bloque de instrucciones pertenciente a Total Anual y Meses con más ventas, si es ingresado el numero 8
      elif seleccion == "8":
        #Se inicializa una variable n en 0 que servira de acumulador en el conteo de ventas totales.
        n=0
        #Se inicializa una variable suma en 0 que servira de acumulador en el conteo de ingresos mensuales
        suma=0
        #Se inicializa una variable suma_anual en 0 que servira de acumulador en el conteo de ingresos anuales
        suma_anual=0
        #Se inicializa una lista para posteriormente añadir los valores finales
        lifestore_mes = []

        #Se inicializa una variable "months" con los nombres de cada mes para despues relacionarlos
        months = ("Enero","Febrero","Marzo","Abril","Mayo","Junio", "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")

        #El primer ciclo for itera la lista months
        for var in months:
            #El siguiente ciclo for itera la lista lifestore_sales por medio de indices
            for x in range(len(lifestore_sales)):
              #Se formatea en una variable fecha_dt la fecha de cada elemento de cada sublista de lifestore_sale en su posicion 3. De manera que pueda ser manejable
              fecha_dt = datetime.strptime(lifestore_sales[x][3],"%d/%m/%Y")
              #en la variable mes se captura el mes de cada fecha para que se homologue con la representacion del mes en Letra
              mes=months[fecha_dt.month - 1]
              #Se valida si la variable mes es igual a la iteracion de cada mes
              if mes == var:
                #El siguiente ciclo for itera la lista lifestore_products por medio de indices
                
                for y in range(len(lifestore_products)):
                  if lifestore_sales[x][1] == lifestore_products[y][0]:
                    #En la variable suma se comienza a hacer la sumatoria de los ingresos de todos los productos por mes
                    suma=suma+lifestore_products[y][2]                    
                    n=n+1
            #Se añade a la lista los datos que se van a mostrar (mes, Ingresos del mes y ventas )
            lifestore_mes.append([var,suma,n])
            #En la variable suma_anual se incrementa con la suma de cada mes
            suma_anual=suma_anual+suma
            #Se reinicializan las variables en 0
            suma=0
            n=0       

        #en una nueva lista, se realiza una funcion sorted,  para ordenar los datos de la lista lifestore_mesrank con filtro en las ventas de cada mes para visualizar los meses con mas ventas de mayor a menor        
        lifestore_mesrank=sorted(lifestore_mes, key = lambda x: int(x[2]),reverse=True)
       #Se crea un contador para enumerar los meses con mas ventas del mayor a menor
        p=0
        #El siguiente ciclo for itera la lista lifestore_mesrank para visualizar todos los meses
        for m in lifestore_mesrank:
          p+=1
          print(p,"|  Mes:",m[0],"| Ingresos del mes:",locale.currency(m[1],grouping=True),"| Ventas: ",m[2],"|")
       #Finalmente se hace la suma del ingreso de todos los meses, Ademas se vuelve a utilizar la funcion locale.currency para imprimir en formato moneda
        print("--------------------------")
        print("Total anual:",locale.currency(suma_anual,grouping=True))
        time.sleep(3)

      #------------------------------------------------------
      #Con la sentencia elif realiza la validacion para regresar al ingreso de usuario y contraseña si es ingresado el numero 9

      elif seleccion == "9":
        print("Saliendo...")
        time.sleep(3)
        #Con el break se sale del ciclo while para regresal al ingreso de usuario y contraseña
        break
      #------------------------------------------------------
      #Con la sentencia else realiza la validacion para contemplar el ingreso de digitos distintos a las opciones mostradas en el menu
      else:
        print("\nSelecciona una opcion valida\n")
        time.sleep(3)
  #Con la sentencia else realiza la validacion para contemplar el ingreso de usuarios o contraseña erroneos
  else:
    print("\nUsuario o Contraseña Incorrecta. Reintente de nuevo\n")
    time.sleep(3)