from smtplib import SMTP

servidor = SMTP('alu-mail.uji.es') # Cambia la cadena por el nombre del servidor.
remitente = 'al00000@alumail.uji.es'
destinatario = 'al99999@alumail.uji.es'
mensaje = 'From: {}\nTo: {}\n\n'.format(remitente, destinatario)
mensaje += 'Hola. \n'
mensaje += 'Hasta Luego. \n'

servidor.sendmail(remitente, destinatario, mensaje)
