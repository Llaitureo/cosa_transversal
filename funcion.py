import random, os, time, csv

#1. Asignar sueldos aleatorios
#2. Clasificar sueldos
#3. Ver estadísticas.
#4. Reporte de sueldos
#5. Salir del programa

#trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez"
#               ,"Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
trabajadores2=[]
afp=0
salud=0
jp=0
mg=0
cl=0
an=0
pr=0
lh=0
ms=0
ig=0
fd=0
ef=0


def opc_1():
    
    print('\tAsignando sueldos Aleatorios')
    jp=random.randint(300000,2500000)
    mg=random.randint(300000,2500000)
    cl=random.randint(300000,2500000)
    an=random.randint(300000,2500000)
    pr=random.randint(300000,2500000)
    lh=random.randint(300000,2500000)
    ms=random.randint(300000,2500000)
    ig=random.randint(300000,2500000)
    fd=random.randint(300000,2500000)
    ef=random.randint(300000,2500000)

    trabajadores =[{'nombre':'Juan Pérez',
                    'sueldo':jp,
                    'salud':salud,
                    'afp':afp},
                    {'nombre':'María García',
                    'sueldo':mg,
                    'salud':salud,
                    'afp':afp},
                    {'nombre':'Carlos López',
                    'sueldo':cl,
                    'salud':salud,
                    'afp':afp},
                    {'nombre':'"Ana Martínez',
                    'sueldo':an,
                    'salud':salud,
                    'afp':afp},
                    {'nombre':'Pedro Rodríguez',
                    'sueldo':pr,
                    'salud':salud,
                    'afp':afp},
                    {'nombre':'Laura Hernández',
                    'sueldo':lh,
                    'salud':salud,
                    'afp':afp},
                    {'nombre':'Miguel Sánchez',
                    'sueldo':ms,
                    'salud':salud,
                    'afp':afp},
                    {'nombre':'Isabel Gómez',
                    'sueldo':ig,
                    'salud':salud,
                    'afp':afp},
                    {'nombre':'Francisco Díaz',
                    'sueldo':fd,
                    'salud':salud,
                    'afp':afp},
                    {'nombre':'Elena Fernández',
                    'sueldo':ef}]
            
    trabajadores2.append(trabajadores)
    
    print('listo!')
    time.sleep(3)
    return trabajadores


def opc_2():
    if len(trabajadores2)==0:
        print('error.. vaya a la opción 1')
    else:
        print('\tClasificar sueldos')
        t800 = 0
        t800_2000 = 0
        t2500 = 0

        for x in trabajadores2:
            for elementos in x:
                        
                        if elementos["sueldo"] <800000:
                            t800= t800+1
                            print(f'nombre: {elementos["nombre"]}')
                            print(f'sueldo: {elementos["sueldo"]}')
                        elif elementos["sueldo"] >=800000 or elementos["sueldo"] <=2000000:
                            t800_2000= t800_2000+1
                            print(f'nombre: {elementos["nombre"]}')
                            print(f'sueldo: {elementos["sueldo"]}')
                        elif elementos["sueldo"]>2000000:
                            t2500=t2500+1
                            print(f'nombre: {elementos["nombre"]}')
                            print(f'sueldo: {elementos["sueldo"]}')

                           

        total = jp+mg+cl+an+pr+lh+ms+ig+fd+ef
            
    print('\nTrabajadores con sueldo menor a 800.000 : ',t800)
    print('Trabajadores con sueldo entre 800.000 y 2.000.000 : ',t800_2000)
    print('Trabajadores con sueldo mayor a 2.000.000 : ',t2500)

    print('\n\t total de sueldos: ',total)

def opc_3():
    if len(trabajadores2)==0:
        print('error.. vaya a la opción 1')
    else:
        total2=0
        sueldo_mayor =0
        sueldo_menor=0
        for x in trabajadores2:
            for elementos in x:
                if elementos["sueldo"]>elementos["sueldo"]:
                    sueldo_mayor= elementos["sueldo"]
                if elementos["sueldo"]==300000:
                    sueldo_menor = elementos["sueldo"]
                total2 = total2 + elementos["sueldo"]
        total3 = total2/10
        print('sueldo mayor: ', sueldo_mayor)
        print('sueldo menor: ', sueldo_menor)
        print('promedio sueldos: ', total3)
        MG= (total2)**(1/10)
        print('MG :', MG)

def opc_4():
    if len(trabajadores2)==0:
        print('error.. vaya a la opción 1')
    else:
        
        
        for x in trabajadores2:
            for elementos in x:

                

                with open ('archivo.csv', "w")as csvfile:
                    escritor = csv.writer(csvfile)
                    escritor.writerow([elementos["nombre"]])
                    escritor.writerow([elementos["sueldo"]])

    print('listo!')
                


def menu():
    while True:
        os.system('cls')
        print('\tMENÚ')
        print("\nopc.1 = Asignar sueldo aleatorio.")
        print('opc.2 = Clasificar sueldos.')
        print('opc.3 = Ver estadísticas.')
        print('opc.4 = Reporte de sueldos.')
        print('opc.5 = Salir.')
        while True:
            try:
                opc = int(input('ingrese opción: '))
                if opc == int:
                    break
            except:
                print('dígitos.')

        if opc in (1,2,3,4,5):
            os.system('cls')
            if opc ==1:
                opc_1()
            elif opc ==2:
                opc_2()
                time.sleep(7)
            elif opc ==3:
                opc_3()
                time.sleep(4)
            elif opc ==4:
                opc_4()
                time.sleep(2)
            else:
                print('finalizando programa...')
                time.sleep(3)
                print('Desarrollado por Fernanda LLaitureo.')
                print('RUT: 21.941.445-5')
                return
        else:
            print('ingrese el núnmero de la opción en forma digito.')
            