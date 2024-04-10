print ("Hola este programa te ayuda a conocer si tienes que pagar declaracion de renta, y en el caso de que lo tengas que hacer cuanto es lo que deberas pagar.")
input ("Primero ingrese su nombre completo: ")
user = input ("Cree un usuario para ingresar al sistema: ")
valid_user = [user]
password = input ("Cree una contraseña: ")
valid_pass = [password]
print ("Puede continuar")
user1 = input ("Ingrese su usuario: ")
pass1 = input ("Ingrese su contraseña: ")
if user1 in valid_user and pass1 in valid_pass:
    print ("Bienvenido al sistema a continuacion se le realizara una encuesta")
    asal = input ("Es ud asalariado si(1) no(2): ")
    fuera = input ("Es usted persona natural o juridica extranjera residente fuera del pais si(1) no(2): ")
    if asal == "1" and (fuera == "1" or "2"):
        print ("Usted no debe presentar declaracion de renta")
    else:
        topbrut = input ("Ahora se le preguntaran algunos de sus topes. Su patrimonio bruto supero en 2023 los 190.854.000 millones de pesos si(1) no(2): ")
        topingre = input ("Sus ingresos anuales fueron mayores a 59.377.000 millones de pesos si(1) no(2): ")
        toptarjeta = input ("Sus gastos con su tarjeta de credito fueron mayores a 59.377.000 millones de pesos si(1) no(2):  ")
        topconsum = input ("SU gasto anual en consumo fue mayor a 59.377.000 millones de pesos si(1) no(2): ")
        topbanco = input ("Sus consignaciones, depositos, etc. Fueron mayores a 59.377.000 millones de pesos si(1) no(2):  ")
        if topbrut or topingre or toptarjeta or topconsum or topbanco == "1":
            print ("Usted debe declarar renta segun los topes establecidos por la DIAN para el año 2023")
            pers = input ("Es ud persona natural(1) o juridica(2)")
            if pers == "1":
                print ("Usted al ser una persona natural para declarar renta debera realizar el cuestionario 210 de la DIAN el cual encontrara en el siguiente link (https://acortar.link/mqHxCI)")
            else:
                print ("Usted al ser una persona juridica para declarar renta debera realizar el cuestionario 110 de la DIAN el cual encontrara en el siguiente link (https://acortar.link/4sQPVO)")
        else:
            print ("Ud no debe declarar renta") 
else:
    print ("Usuario o contraseña invalidos vuelva a ingresar")




