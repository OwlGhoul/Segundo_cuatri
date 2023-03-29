import pywhatkit 

num_tel = (input('Ingrese un número de teléfono: '))
msj = str(input('Ingrese el mensaje que desea enviar: '))
hora = int(input('Ingrese la hora a la que se va a enviar el mensaje: '))
min = int(input('Ingrese el minuto en el que se va a enviar el mensaje: '))
pywhatkit.sendwhatmsg(num_tel, msj, hora, min, 10, True, 2)

#Permite enviar imágenes
#pywhatkit.sendwhats_image("KiNrXFE0y0g5J2xsKgHaMc", "FDownloads\hqdefault.jpg", "Testeo")
