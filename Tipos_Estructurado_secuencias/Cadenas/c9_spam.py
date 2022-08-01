from smtplib import SMTP

servidor = SMTP('alu-mail.uji.es')
remitente = 'al00000@alumail.uji.es'

texto = 'Estimado =S =A:\n\n'
texto += 'Por la presente le informamos de que nos debe usted la' 
texto += 'cantidad de =E euros. Si no abona dicha cantidad antes'
texto += 'de 3 días, su nombre pasará a nuestra lista de morosos'

seguir = 's'
while seguir == 's':
    destinatario = input('Dirección del Dstinatario: ')
    tratamiento = input('Tratamiento: ')
    apellido = input('Apellido: ')
    euros = input('Deuda (en euros): ')

    mensaje = 'From: {}\nTo: {}\n\n'.format(remitente, destinatario)

    personalizado = ''
    i = 0
    while i < len(texto):
        if texto[i] != '=':
            personalizado += texto[i]
        else:
            if texto[i+1] == 'A':
                personalizado += apellido
            elif texto[i+1] == 'E':
                personalizado += euros
            elif texto[i+1] == 'S':
                personalizado += tratamiento
                i = i + 1 
            else:
                personalizado += '='
        i = i + 1
    mensaje += personalizado

    servidor.sendmail(remitente, destinatario, mensaje)
    seguir = input('Si desea enviar otro correo, pulse "s": ')
