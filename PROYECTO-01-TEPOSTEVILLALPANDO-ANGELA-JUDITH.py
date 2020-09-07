#CODIGO DE ANALISIS DE DATOS ANUAL DE TIENDA .
#PROYECTO 1. DATA SCIENCIE: FUNDAMENTOS DE PYTHON

#Librerías
# para poder bloquear la contraseña 
import getpass

#INFORMACION DE contacto de ADMINISTRADOR
NOMBREADMI= "Teposte Villalpando Angela"
CORREO=' teposte.villalpa@gmail.com'
TEL="3217349274813743"

#IMPORTADO DE ARCHIVOS DE LA TIENDA
from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_searches

#SECUENCIA PARA ACOMODO POR MESES
#contadores
busque=0     #contador
v=0          #contador
estrellas=0  #contador
devolu=0     #contador

#definir arreglos para guardar informacion por meses
enero=[]
febrero=[]
marzo=[]
abril=[]
mayo=[]
junio=[]
julio=[]
agosto=[]
septiembre=[]
octubre=[]
noviembre=[]
diciembre=[]

#SECUENCIA PARA ACOMODO POR CATEGORÍA
for ventas in lifestore_sales:   #iteracion sobre ventas para contarlas
   if '01' == ventas[3][3:5]: #Busca coincidencia en el mes
       for producto in lifestore_products:
         if producto[0] == ventas[1]:   #producto con venta
           v+=1      
           stock=producto[4]
           nombre=producto[1]
           clave=producto[0]
           precio=producto[2]           
           estrellas+=ventas[2]          #conteo de score
           if ventas[4]==1:  #condicional si hubo devolucion
             devolu+=1                 #conteo devoluciones
       for search in lifestore_searches:
         if search[1] == ventas[1]:    
           busque+=1                     #conteo busquedas
       ingrexm=precio*v
       #Sub formato 
       en= [v,estrellas,devolu,busque,stock,clave,nombre,ingrexm]
       enero.append(en)            #guardado de datos
       #reinicio de contadores
       v=0
       devolu=0
       busque=0
       estrellas=0

   elif '02' == ventas[3][3:5]:
       for producto in lifestore_products:
         if producto[0] == ventas[1]:
           v+=1
           stock=producto[4]
           nombre=producto[1]
           clave=producto[0]
           precio=producto[2]     
           estrellas+=ventas[2]
           if ventas[4]==1:
             devolu+=1  
       for search in lifestore_searches:
         if search[1] == ventas[1]:
           busque+=1
       ingrexm=precio*v
       feb= [v,estrellas,devolu,busque,stock,clave,nombre,ingrexm]
       febrero.append(feb) 
       v=0
       devolu=0
       busque=0
       estrellas=0
   elif '03' == ventas[3][3:5]:
       for producto in lifestore_products:
         if producto[0] == ventas[1]:
           v+=1
           stock=producto[4]
           nombre=producto[1]
           clave=producto[0]
           precio=producto[2]     
           estrellas+=ventas[2]
           if ventas[4]==1:
             devolu+=1  
       for search in lifestore_searches:
         if search[1] == ventas[1]:
           busque+=1
       ingrexm=precio*v
       mar= [v,estrellas,devolu,busque,stock,clave,nombre,ingrexm]
       marzo.append(mar) 
       v=0
       devolu=0
       busque=0
       estrellas=0
   elif '04' == ventas[3][3:5]:
       for producto in lifestore_products:
         if producto[0] == ventas[1]:
           v+=1
           stock=producto[4]
           nombre=producto[1]
           clave=producto[0]
           precio=producto[2]     
           estrellas+=ventas[2]
           if ventas[4]==1:
             devolu+=1  
       for search in lifestore_searches:
         if search[1] == ventas[1]:
           busque+=1
       ingrexm=precio*v
       abr= [v,estrellas,devolu,busque,stock,clave,nombre,ingrexm]
       abril.append(abr) 
       v=0
       devolu=0
       busque=0
       estrellas=0
   elif '05' == ventas[3][3:5]:
       for producto in lifestore_products:
         if producto[0] == ventas[1]:
           v+=1
           stock=producto[4]
           nombre=producto[1]
           clave=producto[0]
           precio=producto[2]     
           estrellas+=ventas[2]
           if ventas[4]==1:
             devolu+=1  
       for search in lifestore_searches:
         if search[1] == ventas[1]:
           busque+=1
       ingrexm=precio*v
       may= [v,estrellas,devolu,busque,stock,clave,nombre,ingrexm]
       mayo.append(may) 
       v=0
       devolu=0
       busque=0
       estrellas=0
   elif '06' == ventas[3][3:5]:
       for producto in lifestore_products:
         if producto[0] == ventas[1]:
           v+=1
           stock=producto[4]
           nombre=producto[1]
           clave=producto[0]
           precio=producto[2]     
           estrellas+=ventas[2]
           if ventas[4]==1:
             devolu+=1  
       for search in lifestore_searches:
         if search[1] == ventas[1]:
           busque+=1
       ingrexm=precio*v
       jun= [v,estrellas,devolu,busque,stock,clave,nombre,ingrexm]
       junio.append(jun) 
       v=0
       devolu=0
       busque=0
       estrellas=0
   elif '07' == ventas[3][3:5]:
       for producto in lifestore_products:
         if producto[0] == ventas[1]:
           v+=1
           stock=producto[4]
           nombre=producto[1]
           clave=producto[0]
           precio=producto[2]     
           estrellas+=ventas[2]
           if ventas[4]==1:
             devolu+=1  
       for search in lifestore_searches:
         if search[1] == ventas[1]:
           busque+=1
       ingrexm=precio*v
       jul= [v,estrellas,devolu,busque,stock,clave,nombre,ingrexm]
       julio.append(jul) 
       v=0
       devolu=0
       busque=0
       estrellas=0
   elif '08' == ventas[3][3:5]:
       for producto in lifestore_products:
         if producto[0] == ventas[1]:
           v+=1
           stock=producto[4]
           nombre=producto[1]
           clave=producto[0]
           precio=producto[2]     
           estrellas+=ventas[2]
           if ventas[4]==1:
             devolu+=1  
       for search in lifestore_searches:
         if search[1] == ventas[1]:
           busque+=1
       ingrexm=precio*v
       agt= [v,estrellas,devolu,busque,stock,clave,nombre,ingrexm]
       agosto.append(agt) 
       v=0
       devolu=0
       busque=0
       estrellas=0
   elif '09' == ventas[3][3:5]:
       for producto in lifestore_products:
         if producto[0] == ventas[1]:
           v+=1
           stock=producto[4]
           nombre=producto[1]
           clave=producto[0]
           precio=producto[2]     
           estrellas+=ventas[2]
           if ventas[4]==1:
             devolu+=1  
       for search in lifestore_searches:
         if search[1] == ventas[1]:
           busque+=1
       ingrexm=precio*v
       sep= [v,estrellas,devolu,busque,stock,clave,nombre,ingrexm]
       septiembre.append(sep) 
       v=0
       devolu=0
       busque=0
       estrellas=0
   elif '10' == ventas[3][3:5]:
       for producto in lifestore_products:
         if producto[0] == ventas[1]:
           v+=1
           stock=producto[4]
           nombre=producto[1]
           clave=producto[0]
           precio=producto[2]     
           estrellas+=ventas[2]
           if ventas[4]==1:
             devolu+=1  
       for search in lifestore_searches:
         if search[1] == ventas[1]:
           busque+=1
       ingrexm=precio*v
       octb= [v,estrellas,devolu,busque,stock,clave,nombre,ingrexm]
       octubre.append(octb) 
       v=0
       devolu=0
       busque=0
       estrellas=0
   elif '11' == ventas[3][3:5]:
       for producto in lifestore_products:
         if producto[0] == ventas[1]:
           nombre=producto[1]
           v+=1
           stock=producto[4]
           nombre=producto[1]
           clave=producto[0]
           precio=producto[2]     
           estrellas+=ventas[2]
           if ventas[4]==1:
             devolu+=1  
       for search in lifestore_searches:
         if search[1] == ventas[1]:
           busque+=1
       ingrexm=precio*v
       nov= [v,estrellas,devolu,busque,stock,clave,nombre,ingrexm]
       noviembre.append(nov) 
       v=0
       devolu=0
       busque=0
       estrellas=0
   elif '12' == ventas[3][3:5]:
       for producto in lifestore_products:
         if producto[0] == ventas[1]:
           v+=1
           stock=producto[4]
           nombre=producto[1]
           clave=producto[0]
           precio=producto[2]     
           estrellas+=ventas[2]
           if ventas[4]==1:
             devolu+=1  
       for search in lifestore_searches:
         if search[1] == ventas[1]:
           busque+=1
       ingrexm=precio*v
       dic= [v,estrellas,devolu,busque,stock,clave,nombre,ingrexm]
       diciembre.append(dic) 
       v=0
       devolu=0
       busque=0
       estrellas=0

#SECUENCIA PARA ACOMODO POR CATEGORÍA
#contadores
busque=0
v=0   
estrellas=0
devolu=0
#definir arreglos para información por meses
procesador=[]
tarjetas_de_video=[]
tarjetas_madre=[]
discos_duros=[]
memorias_usb=[]
pantallas=[]
bocinas=[]
audifonos=[]
 #iteracion sobre productos 
for producto in lifestore_products:
   #print(producto[1][0:20])
  #iteracion sobre ventas para contarlas
   if 'procesadores' == producto[3]:
       for ventas in lifestore_sales: 
         if producto[0] == ventas[1]:
           v+=1
           estrellas+=ventas[2]
           stock=producto[4]
           nombre=producto[1]
           clave=producto[0]
           precio=producto[2]
           if ventas[4]==1:
             devolu+=1  
       for search in lifestore_searches:
         if search[1] == ventas[1]:
           busque+=1
       ingrexproducto=precio*v
       proce= [v,estrellas,devolu,busque,stock,clave,nombre,ingrexproducto]
       procesador.append(proce) 
       v=0
       devolu=0
       busque=0
       estrellas=0
   elif 'tarjetas de video' == producto[3]:
       for ventas in lifestore_sales: 
         if producto[0] == ventas[1]:
           v+=1
           estrellas+=ventas[2]
           stock=producto[4]
           nombre=producto[1]
           clave=producto[0]
           precio=producto[2]
           if ventas[4]==1:
             devolu+=1  
       for search in lifestore_searches:
         if search[1] == ventas[1]:
           busque+=1
       ingrexproducto=precio*v
       vid= [v,estrellas,devolu,busque,stock,clave,nombre,ingrexproducto]
       tarjetas_de_video.append(vid) 
       v=0
       devolu=0
       busque=0
       estrellas=0
   elif 'tarjetas madre' == producto[3]:
       for ventas in lifestore_sales: 
         if producto[0] == ventas[1]:
           v+=1
           estrellas+=ventas[2]
           stock=producto[4]
           nombre=producto[1]
           clave=producto[0]
           precio=producto[2]
           if ventas[4]==1:
             devolu+=1  
       for search in lifestore_searches:
         if search[1] == ventas[1]:
           busque+=1
       ingrexproducto=precio*v
       mad= [v,estrellas,devolu,busque,stock,clave,nombre,ingrexproducto]
       tarjetas_madre.append(mad) 
       v=0
       devolu=0
       busque=0
       estrellas=0
   elif 'discos duros'== producto[3]:
       for ventas in lifestore_sales: 
         if producto[0] == ventas[1]:
           v+=1
           estrellas+=ventas[2]
           stock=producto[4]
           nombre=producto[1]
           clave=producto[0]
           precio=producto[2]
           if ventas[4]==1:
             devolu+=1  
       for search in lifestore_searches:
         if search[1] == ventas[1]:
           busque+=1
       ingrexproducto=precio*v
       disc= [v,estrellas,devolu,busque,stock,clave,nombre,ingrexproducto]
       discos_duros.append(disc) 
       v=0
       devolu=0
       busque=0
       estrellas=0
   elif 'memorias usb' == producto[3]:
       for ventas in lifestore_sales: 
         if producto[0] == ventas[1]:
           v+=1
           estrellas+=ventas[2]
           stock=producto[4]
           nombre=producto[1]
           clave=producto[0]
           precio=producto[2]
           if ventas[4]==1:
             devolu+=1  
       for search in lifestore_searches:
         if search[1] == ventas[1]:
           busque+=1
       ingrexproducto=precio*v
       usb= [v,estrellas,devolu,busque,stock,clave,nombre,ingrexproducto]
       memorias_usb.append(usb) 
       v=0
       devolu=0
       busque=0
       estrellas=0
   elif 'pantallas' == producto[3]:
       for ventas in lifestore_sales: 
         if producto[0] == ventas[1]:
           v+=1
           estrellas+=ventas[2]
           stock=producto[4]
           nombre=producto[1]
           clave=producto[0]
           precio=producto[2]
           if ventas[4]==1:
             devolu+=1  
       for search in lifestore_searches:
         if search[1] == ventas[1]:
           busque+=1
       ingrexproducto=precio*v
       pan= [v,estrellas,devolu,busque,stock,clave,nombre,ingrexproducto]
       pantallas.append(pan) 
       v=0
       devolu=0
       busque=0
       estrellas=0
   elif 'bocinas' == producto[3]:
       #print(producto[3])
       for ventas in lifestore_sales: 
         #print(producto[0],ventas[1])
         if producto[0] == ventas[1]:
           #print(producto[0],ventas[1],v)
           v+=1
           estrellas+=ventas[2]
           stock=producto[4]
           nombre=producto[1]
           clave=producto[0]
           precio=producto[2]
           #print("ventas acomuladas",v,"producto",nombre[0:15])
           if ventas[4]==1:
             devolu+=1  
       for search in lifestore_searches:
         if search[1] == ventas[1]:
           busque+=1
       ingrexproducto=precio*(v)
       boc= [v,estrellas,devolu,busque,stock,clave,nombre,ingrexproducto]
       bocinas.append(boc) 
       v=0
       devolu=0
       busque=0
       estrellas=0
   elif 'audifonos' == producto[3]:
       for ventas in lifestore_sales: 
         if producto[0] == ventas[1]:
           v+=1
           estrellas+=ventas[2]
           stock=producto[4]
           nombre=producto[1]
           clave=producto[0]
           precio=producto[2]
           if ventas[4]==1:
             devolu+=1  
       for search in lifestore_searches:
         if search[1] == ventas[1]:
           busque+=1
       ingrexproducto=precio*v
       aud= [v,estrellas,devolu,busque,stock,clave,nombre,ingrexproducto]
       audifonos.append(aud) 
       v=0
       devolu=0
       busque=0
       estrellas=0

ingrexcatego=[]   #para guarda info
ingrexmes=[]
suma=0
# SUMA DE INGRESOS POR CATEGORÍA
suma=0
v=0
for dat in procesador:  #PARA Procesadores
  suma+=dat[7]
  v+=dat[0]
ingre=[suma,'procesadores',v]
ingrexcatego.append(ingre)

suma=0
v=0
for dat in tarjetas_de_video:
  suma+=dat[7]
  v+=dat[0]
ingre=[suma,'tarjetas de video',v]
ingrexcatego.append(ingre)

suma=0
v=0
for dat in tarjetas_madre:
  suma+=dat[7]
  v+=dat[0]
ingre=[suma,'tarjetas madre',v]
ingrexcatego.append(ingre)

suma=0
v=0
for dat in discos_duros:
  suma+=dat[7]
  v+=dat[0]
ingre=[suma,'discos duros',v]
ingrexcatego.append(ingre)

suma=0
v=0
for dat in memorias_usb:
  suma+=dat[7]
  v+=dat[0]
ingre=[suma,'memorias usb',v]
ingrexcatego.append(ingre)

suma=0
v=0
for dat in pantallas:
  suma+=dat[7]
  v+=dat[0]
ingre=[suma,'pantallas',v]
ingrexcatego.append(ingre)

suma=0
v=0
for dat in bocinas:
  suma+=dat[7]
  v+=dat[0]
ingre=[suma,'bocinas',v]
ingrexcatego.append(ingre)

suma=0
v=0
for dat in audifonos:
  suma=suma+dat[7]
  v+=dat[0]

ingre=[suma,'audifonos',v]
ingrexcatego.append(ingre)

# SUMA DE INGRESOS POR MESES
suma=0
devo=0
busqu=0
v=0
t=0
mayor=0
for dat in enero:            #Enero
  suma+=dat[7]
  v+=dat[0]
  devo+=dat[2]
  busqu+=dat[3]
  if dat[0]>t:
    t=dat[0]
    mayor=dat[6]
ingre=[suma,'enero',v,devo,busqu,mayor]
ingrexmes.append(ingre)

suma=0
devo=0
busqu=0
v=0
t=0
mayor=0
for dat in febrero:
  suma+=dat[7]
  v+=dat[0]
  devo+=dat[2]
  busqu+=dat[3]
  if dat[0]>t:
    t=dat[0]
    mayor=dat[6]
ingre=[suma,'febrero',v,devo,busqu,mayor]
ingrexmes.append(ingre)

suma=0
devo=0
busqu=0
v=0
t=0
mayor=0
for dat in marzo:
  suma+=dat[7]
  v+=dat[0]
  devo+=dat[2]
  busqu+=dat[3]
  if dat[0]>t:
    t=dat[0]
    mayor=dat[6]
ingre=[suma,'marzo',v,devo,busqu,mayor]
ingrexmes.append(ingre)

suma=0
devo=0
busqu=0
v=0
t=0
mayor=0
for dat in abril:
  suma+=dat[7]
  v+=dat[0]
  devo+=dat[2]
  busqu+=dat[3]
  if dat[0]>t:
    t=dat[0]
    mayor=dat[6]
ingre=[suma,'abril',v,devo,busqu,mayor]
ingrexmes.append(ingre)

suma=0
devo=0
busqu=0
v=0
t=0
mayor=0
for dat in mayo:
  suma+=dat[7]
  v+=dat[0]
  devo+=dat[2]
  busqu+=dat[3]
  if dat[0]>t:
    t=dat[0]
    mayor=dat[6]
ingre=[suma,'mayo',v,devo,busqu,mayor]
ingrexmes.append(ingre)

suma=0
devo=0
busqu=0
v=0
t=0
mayor=0
for dat in junio:
  suma+=dat[7]
  v+=dat[0]
  devo+=dat[2]
  busqu+=dat[3]
  if dat[0]>t:
    t=dat[0]
    mayor=dat[6]
ingre=[suma,'junio',v,devo,busqu,mayor]
ingrexmes.append(ingre)

suma=0
devo=0
busqu=0
v=0
t=0
mayor=0
for dat in julio:
  suma+=dat[7]
  v+=dat[0]
  devo+=dat[2]
  busqu+=dat[3]
  if dat[0]>t:
    t=dat[0]
    mayor=dat[6]
ingre=[suma,'julio',v,devo,busqu,mayor]
ingrexmes.append(ingre)

suma=0
devo=0
busqu=0
v=0
t=0
mayor=0
for dat in agosto:
  suma+=dat[7]
  v+=dat[0]
  devo+=dat[2]
  busqu+=dat[3]
  if dat[0]>t:
    t=dat[0]
    mayor=dat[6]
ingre=[suma,'agosto',v,devo,busqu,mayor]
ingrexmes.append(ingre)

suma=0
devo=0
busqu=0
v=0
t=0
mayor=0
for dat in septiembre:
  suma+=dat[7]
  v+=dat[0]
  devo+=dat[2]
  busqu+=dat[3]
  if dat[0]>t:
    t=dat[0]
    mayor=dat[6]
ingre=[suma,'septiembre',v,devo,busqu,mayor]
ingrexmes.append(ingre)

suma=0
devo=0
busqu=0
v=0
t=0
mayor=0
for dat in octubre:
  suma+=dat[7]
  v+=dat[0]
  devo+=dat[2]
  busqu+=dat[3]
  if dat[0]>t:
    t=dat[0]
    mayor=dat[6]
ingre=[suma,'octubre',v,devo,busqu,mayor]
ingrexmes.append(ingre)

suma=0
devo=0
busqu=0
v=0
t=0
mayor=0
for dat in noviembre:
  suma+=dat[7]
  v+=dat[0]
  devo+=dat[2]
  busqu+=dat[3]
  if dat[0]>t:
    t=dat[0]
    mayor=dat[6]
ingre=[suma,'noviembre',v,devo,busqu,mayor]
ingrexmes.append(ingre)

suma=0
devo=0
busqu=0
v=0
t=0
mayor=0
for dat in diciembre:
  suma+=dat[7]
  v+=dat[0]
  devo+=dat[2]
  busqu+=dat[3]
  if dat[0]>t:
    t=dat[0]
    mayor=dat[6]
ingre=[suma,'diciembre',v,devo,busqu,mayor]
ingrexmes.append(ingre)

#print(ingrexmes)

#SECUENCIA PARA CONTAR VENTAS y BUSQUEDAS TOTAL
j=0       #contador
i=1  # contador 
searchxproducto = [] # subformato [[contador,id,nombre],[]]
devolucion = []
ventasxproducto = [] # subformato [[contador,id,nombre],[]]
calidad_producto=[] # subformato [[devoluciones,puntaje,id,nombre],[]]
devoluciones=0
score=0
for producto in lifestore_products:
   for ventas in lifestore_sales:
     if producto[0] == ventas[1]:
       estrellas+=ventas[2]
       stock=producto[4]
       nombre=producto[1]
       clave=producto[0]
       precio=producto[2]
       if ventas[4]==1:
           devoluciones+=1  
       j+=1
   #print(producto[0],"id",estrellas,"score",devoluciones,"devoluciones",j,"ventas")
   if j==0:
     score=0
     devolu=0
   elif j!=0:
     score=round(estrellas/j,2)
     devolu=round(devoluciones/j,2)
   #print(score,producto[0])
   calidad = [score,devoluciones,j,producto[0],producto[1] ]
   calidad_producto.append(calidad)
   datos_ventas = [j,producto[0],producto[1]] #subformato
   ventasxproducto.append(datos_ventas)  #guarda info
   j=0
   for search in lifestore_searches:
     if producto[0] == search[1]:
       i+=1
   datos_search = [i,producto[0],producto[1],stock] #subformato
   searchxproducto.append(datos_search)       #guarda info # de ventas
   dev=[devoluciones,devolu,producto[0],producto[1],j] 
   devolucion.append(dev)
   i=0
   estrellas=0
   score=0
   devoluciones=0


#CODIGO PARA USUARIO !
#cadena para guardar listas de usuarios
# formato [permisosadministrados nnombre contraseña]
usuarios = [[True,True,'Teposte','chicorita'],[True,True,'ana','b'],[False,True,'Gina','1987'],[True,True,'Javier','123'] ]   
num_usu=len(usuarios)-1

#Bienvenida he inicio de sección
bienvenida = "" "Bienvenido. \n    Ingrese por favor el nombre de su usuario \n    (respete minúsculas y mayúsculas) \n \n \n " " "
print (bienvenida)

#Ingresa nombre y contraseña de usuario, determina su existencia

usuario_in = input ('Nombre de usuario : ')
i=0   #contador 
for usuario in usuarios:
  if usuario[2] == usuario_in:
    contra_in = getpass.getpass('Ingrese su contraseña : \n ')
    #Determina si la contraseña es correcta
    if contra_in == usuario[3]:
      print('\n \n Hola', usuario_in)
      #Si no es correcta se hace un ciclo para 2 intentos mas 
    elif contra_in != usuario[3]:
       for j in range (0,2):
          print('La contraseña es incorrecta, tiene', 2-j ,
                 "intentos más",j)
          contra_in = getpass.getpass('Ingrese contraseña :\n  ')
          if contra_in == usuario[3]:
            print('\n \n Hola', usuario_in  )
            break
          elif j==1:
            print('\n \n ¡EXCESO DE INTENTOS PERMITIDO!\n  REINICIE EL PROGRAMA O CONTACTE AL ADMINISTADOR\n\n')
            print("Nombre el adminnistrador:",NOMBREADMI)
            print("contacto",  CORREO)
            print("telefono", TEL)
            exit()
    #continue
    break
  elif num_usu==i:
    print("El usuario",usuario_in, "no existe. contante con un administrador \n \n")
    print("Nombre el adminnistrador:",NOMBREADMI)
    print("contacto",  CORREO)
    print("telefono", TEL)
    exit()
  i+=1

#MENUS y SUBMENUS
menu1_admi = "" "seleciona tecleando un número y dando enter\n  \n         1. MENU:\n   1. Ver o generar reportes \n   2. Cambiar de usuario\n   3. Crear nuevo usuario invitado \n   4. Eliminar usuario  \n   5. Editar información de contacto\n   6. Salir \n" " "

menu1_cli = "" "seleciona tecleando un número y dando enter\n   1. MENU:\n   1. Ver reportes.\n   2. Contacto con el administrador \n   3. Salir \n  " " "

menu_reportes = "" "Seleciona tecleando un número y dando enter. \n \n     1.1 MENU DE REPORTES:\n   1. Anual  \n   2. Mensual \n   3. Salir \n" " "

menu_reportesanual = "" "\nSeleciona tecleando un número y dando enter. \n  \n     1.1.1 MENU DE REPORTE ANUAL:\n   1. Listado de los mejores productos.   \n   2. Listado de los peores productos. \n   3. Listado de valoraciones del cliente.\n   4. Reporte de ventas.\n   5. Salir.  \n" " "

menu_mejor = "" "\nSeleciona tecleando un número y dando enter. \n  \n     1.1.1.1 MENU DE MEJORES PRODUCTOS:\n   1. Regresar.   \n   2. Mejores ventas. \n   3. Mayores busquedas.\n   4. Reporte por categoría.\n   5. Salir.  \n" " "

menu_peor = "" "\nSeleciona tecleando un número y dando enter. \n  \n     1.1.1.2 MENU DE PEORES PRODUCTOS:\n   1. Regresar.   \n   2. Menores ventas. \n   3. Menores busquedas.\n   4. Reporte por categoría.\n   5. Salir.  \n"

menu_valora = "" "\nSeleciona tecleando un número y dando enter. \n  \n     1.1.1.3  MENU DE VALORACIÓN DEL CLIENTE:\n   1. Regresar.   \n   2. Mejor valorado. \n   3. Menos valorado.\n   4. Devoluciones.\n   5. Salir.  \n"

m=0 #contador
if usuario[0] and usuario[1]:
   print("Eres administrador.\n \n \n  ¿Qué deseas hacer? ")

   for m in range (0,1):
     print(menu1_admi)
     respuesta= int(input())
     if respuesta == 1:
         print("\n Seleccionar el reporte:\n ")
         print(menu_reportes)
         respu= int(input())  
         if respu==1:               #Anual1.1
           print(menu_reportesanual)
           resp= int(input())
           if resp==1:                   #Anual-Mejores productos
             print(menu_mejor)  
             res= int(input())    
             if res==1:                   #Anual-Mejores Reporte Gral
               print("\n\n Regresando al menu principal.\n\n")
             elif res==2:               #Anual-Mejores Ventas 
               print("\n\n LISTADO DE LOS PRODUCTOS MÁS VENDIDOS.\n\n")
               print("POSICION / VENTAS  / NOMBRE CORTO .\n\n")
               #Acomodo mayor a menor
               ventasxproducto.sort(reverse=True) 
               n=50   #cantidad de archivos
               z = 0  #contador
               while z < n:
                 print(z+1,'  /  ',ventasxproducto[z][0] ,'  /  ', ventasxproducto[z][2][0:37] ,'  . \n ')
                 z+=1
             elif res==3:   #Anual-Mejores Busquedas 
               print("\n\n LISTADO DE LOS PRODUCTOS MÁS BUSCADOS.\n\n")
               print("POSICION /N° BUSQUEDAS/ STOCK / NOMBRE CORTO .\n\n")
               searchxproducto.sort(reverse=True) #Acomodo mayor-menor
               n=20   #cantidad de archivos
               z = 0  #contador
               while z < n:
                 print(z+1,'  /  ',searchxproducto[z][0],'  /  ',searchxproducto[z][3] ,'  /  ', searchxproducto[z][2][0:34],'. \n '  )
                 z+=1
             elif res==4:     #anual por categorias
               print("\n\n REPORTE POR CATEGORÍA.\n\n")
               print("POSICION / INGRESOS / VENTAS  / CATEGORÍA .\n\n")
               #Acomodo mayor a menor
               ingrexcatego.sort(reverse=True) 
               n=12   #cantidad de archivos
               z = 0  #contador
               while z < n:
                 print(z+1,'  /  $',ingrexcatego[z][0] ,'  /  ', ingrexcatego[z][2] ,'  /  ',ingrexcatego[z][1][0:37] ,'  . \n ')
                 z+=1
             elif res==5:
               print('Hasta luego.')
               exit()
           elif resp==2:     #Anual-Peores productos
             print(menu_peor)  
             res= int(input()) 
             if res==1:                   #Anual-Peores Reporte Gral
               print("\n\n Regresando al menu principal . . .\n\n")

             elif res==2:               #Anual-PEoresVentas 
               print("\n\n LISTADO DE LOS PRODUCTOS MENOS VENDIDOS.\n\n")
               print("POSICION / VENTAS  / NOMBRE CORTO .\n\n")
               #Acomodo menor a mayores
               ventasxproducto.sort() 
               n=60   #cantidad de archivos
               z = 0  #contador
               while z < n:
                 print(z+1,'  /  ',ventasxproducto[z][0] ,'  /  ', ventasxproducto[z][2][0:37] ,'  . \n ')
                 z+=1
             elif res==3:   #Anual-Peores Busquedas 
               print("\n\n LISTADO DE LOS PRODUCTOS MENOS BUSCADOS.\n\n")
               print("POSICION /N° BUSQUEDAS/ STOCK / NOMBRE CORTO .\n\n")
               searchxproducto.sort() #Acomodo menor-mayor
               n=20   #cantidad de archivos
               z = 0  #contador
               while z < n:
                 #print(z+1,'  /  ',searchxproducto[z][0],'  /  ','  /  ', '. \n '  )
                 print(z+1,'  /  ',searchxproducto[z][0],'  /  ',searchxproducto[z][3] ,'  /  ', searchxproducto[z][2][0:34],'. \n '  )
                 z+=1
             elif res==4:     #anual por categorias
               print("\n\n REPORTE POR CATEGORÍA.\n\n")
               print("POSICION / INGRESOS / VENTAS  / CATEGORÍA .\n\n")
               #Acomodo menor a mayor
               ingrexcatego.sort() 
               n=8   #cantidad de archivos
               z = 0  #contador
               while z < n:
                 print(z+1,'  /  $',ingrexcatego[z][0] ,'  /  ', ingrexcatego[z][2] ,'  /  ',ingrexcatego[z][1][0:37] ,'  . \n ')
                 z+=1
             elif res==5:
               print('Hasta luego.')
               exit()
           elif resp==3:   #Anual-Valoraciones}
             print(menu_valora)  
             res= int(input())
             if res==1:
               print('REPORTE GENENERAL DE VALORACIÓN DEL CLIENTE.')
             elif res==2:
                print("VALORACIÓN DEL CLIENTE (MEJORES)")
                print("POSICION /PUNTAJE /VENTAS/DEVOLUCION  / PRODUCTO .\n\n")
                #Acomodo mayor a menor
                calidad_producto.sort(reverse=True) 
               
                n=20   #cantidad de archivos
                z = 0  #contador
                while z < n:
                  print(z+1,'   /   ',calidad_producto[z][0],"     /    ",calidad_producto[z][2] ,'      /    ', calidad_producto[z][1] ,'     /    ',calidad_producto[z][4][0:16] ,'  . \n ')
                  z+=1
             elif res==3:
                print("VALORACIÓN DEL CLIENTE (PEORES)")
                print("POSICION /PUNTAJE /VENTAS/DEVOLUCION  / PRODUCTO .\n\n")
                #Acomodo mayor a menor
                calidad_producto.sort() 
               
                n=60   #cantidad de archivos
                z = 0  #contador
                while z < n:
                  print(z+1,'   /   ',calidad_producto[z][0],"     /    ",calidad_producto[z][2] ,'      /    ', calidad_producto[z][1] ,'     /    ',calidad_producto[z][4][0:16] ,'  . \n ')
                  z+=1
             elif res==4:
                print("REPORTE DE DEVOLUCIONES \n")
                print("POSICIÓN /  DEVOLUCIONES / VENTAS   / DEVOLUCIONXVENTAS  / PRODUCTO .\n\n")
                #Acomodo mayor a menor
                devolucion.sort(reverse=True) 
               
                n=15   #cantidad de archivos
                z = 0  #contador
                while z < n:
                  print(z+1,'   /       ',devolucion[z][0],"        /    ",devolucion[z][4] ,'         /      ',devolucion[z][1],'     /    ',devolucion[z][3][0:16] ,'  . \n ')
                  z+=1
           elif resp==4:   #Anual-Reporte ventas
             total=0
             print("\n\n REPORTE DE VENTAS ANUAL.\n\n")
             print(" \n\n A continuación se muestra el resumen de las ventas del año.\n\n ")
             print("/  MES  /  VENTAS  / INGRESOS  /\n  ")
             for mes in ingrexmes:
               print(mes[1]," / ",mes[2]," / $",mes[0])
               total=total + mes[0]
             print(" \n\n TABLA ORDENADA DE MAYOR A MENOS INGRESO\n\n ") 
             ingrexmes.sort(reverse=True) #mayor a menor
             for mes in ingrexmes:
               print(mes[1]," / ",mes[2]," / $",mes[0])
             print(" \n\n TOTAL DE INGRESOS ANUALES: \n ", "$" , total ," \n \n ")
           elif resp==5:   #exit
             print('Hasta luego.')
             exit()
           else: 
             print("Error en la opción seleccionada")

         elif respu==2:  #Mensual 1.2
           print("\n\nRESUMEN DE MESES\n\n")
           for mes in ingrexmes:
             print("\n\nMES:",mes[1])
             print("Ingreso: $",mes[0])
             print("Ventas totales:",mes[2])
             print("Producto con mayor venta:",mes[5])
             print("Busquedas totales:",mes[4])
             print("Devoluciones totales:",mes[3])


         elif respu==3:   # Salir 1.3
           print('Hasta luego.')
           exit()
 
     elif respuesta ==2:
         print("PROXIMAMENTE. el código se volvería muy largo. jaja\n ")
     elif respuesta == 3:
          print("Escribe los datos")
          nom = input("Nombre de usuario : ")
          con = input("Contraseña : ")
          usuarios.append([False,True,nom,con])
     elif respuesta==4:
         print("Escribe el nombre de usuario que desees borrar")
         nom = input("Nombre de usuario : ")
         usuarios.remove(nom)
     elif respuesta==5:
         print("Nombre el adminnistrador:",NOMBREADMI)
         print("contacto",  CORREO)
         print("telefono", TEL)
         print("Desea editar.\n 1. Nombre\n 2. contacto\n 3. telefono\n")
         resp = int(input("opción n°: "))
         if resp==1:
           NOMBREADMI= input("Nombre completo:\n")
         elif resp==2:
           CORREO= input("Correo electrónico:\n")
         elif resp==3:
           TEL= input("telefóno:\n")
         else:
           print("Error en la opción seleccionada")
     elif respuesta==6:
       print('Hasta luego.')
       exit()
     else:
         print("Error en la opción seleccionada")
   m+=1
else:
  print('tu usuario tiene acceso limitado.\n')
  for m in range (0,50):
       print("\n\n\n¿Qué deseas hacer?")
       print(menu1_cli)
       respuesta= int(input())
       if respuesta == 1:
         print("\n Seleccionar el reporte: \n ")
         print(menu_reportes)
         respu= int(input('opción n°:'))
         print('SORRY! Estamos en construcción, vuelve luego')
         print('Lo siento, Javier ya no me dio tiempo de también copiar lo que hice en administradores, pero si lo pondre luego')
       elif respuesta ==2:
         print("Nombre el adminnistrador:",NOMBREADMI)
         print("contacto",  CORREO)
         print("telefono", TEL)
       elif respuesta==3:
         print('Hasta luego.')
         exit()
       else:
         print("Error en la respuesta")    
  m+=1             

