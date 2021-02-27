import amino

# Todos los imports que vienen desde "modules" están en la carpeta modules de Tux, son los recursos que usará el bot.

from modules import color  # Modulo para colorear el texto en la terminal.
from modules import cmds  # Modulo que contiene los comandos de Tux.
from os import listdir, system
from json import dumps, load  # El módulo json aquí se usa para cargar y guardar datos.
from getpass import getpass  # El módulo getpass se usa para preguntar una contraseña, es más seguro que input().
from time import sleep
from shlex import split  # Shlex se usa aquí para hacer un split que diferencie a un comando de sus parámetros.

client = amino.Client()

# Inicia sesión
while True:
    if "data" not in listdir():  # Si el archivo data no se encuentra en el directorio:
        print("\t\tInicia sesión\n\n")
        DATA = {'CREDS': {"email": input("Correo electrónico: "), "password": getpass("Contraseña: ")},
                'SYM': '/',
                'OWNER': ['83e9eb60-3b0e-4009-8b67-dbe432ddae14'],
                'ADMIN': ['83e9eb60-3b0e-4009-8b67-dbe432ddae14']
                }  # Aquí se guardan los datos sobre el usuario, su email, contraseña y el sym (símbolo) que se usará para llamar a Tux.
        try:
            client.login(**DATA['CREDS'])  # Inicia sesión usando las credenciales guardadas en el diccionario DATA
        except amino.exceptions.InvalidAccountOrPassword:  # Si las credenciales son incorrectas:
            print("\nCorreo o contraseña incorrectos")
            print("Presiona enter para continuar.")
            input()
            system("clear")
            continue

        # Si las credenciales son correctas, se crea y guarda el archivo data con los datos del usuario y el bot.
        F = open("data", "w+")
        F.write(dumps(DATA, indent=4))
        F.close()
        print("\033[2J")  # Escape ANSI que elimina el contenido de la pantalla.

    else:  # Si el archivo data existe en el directorio, carga los datos que contiene.

        F = open("data", "r")
        DATA = load(F)
        F.close()
        client.login(**DATA['CREDS'])
        print("\033[2J")

    break

print(client.profile.nickname)
print("\nlogged in...")

# Ingresa a comunidad
while True:
    if "COMM" not in DATA:
        print(f"{color.red}\t\t¿En qué comunidad deseas iniciar el bot?{color.nm}\n\n")
        DATA['COMM'] = input("aminoId: ")
        try:
            DATA['COMM'] = client.search_community(DATA['COMM']).comId[0]  # Obtiene el ID de la comunidad
            client.join_community(DATA['COMM'])  # Se une a la comunidad
        except amino.exceptions.CommunityNotFound:  # Si la comunidad no existe:
            print("Comunidad inexistente.")
            sleep(1)
            print("\033[2J")
            continue

        # Sobreescribe el archivo data incluyendo los datos de la comunidad.
        F = open("data", "w+")
        F.write(dumps(DATA, indent=4))
        F.close()
        break
    else:
        client.join_community(DATA['COMM'])
        break

subclient = amino.SubClient(DATA['COMM'], profile=client.profile)  # Operation with community
print("\nJoined Community...")
print("\nBot started Succesfully!")


@client.callbacks.event("on_group_member_join")
def on_group_member_join(data):
    subclient.send_message(data.message.chatId, f"Bienvenido/a al chat, {data.message.author.nickname}")


@client.callbacks.event("on_group_member_leave")
def on_group_member_leave(data):
    subclient.send_message(data.message.chatId, "Mal ahí, se nos fue un miembro xD")


@client.callbacks.event("on_text_message")
def on_text_message(data):
    if str(data.comId) == str(DATA['COMM']):  # Si el mensaje proviene de la comunidad en la que se inició el bot:
        if __name__ == '__main__':  # Si el bot está siendo ejecutado como main y no como módulo:
            if data.message.content[0] == DATA['SYM']:  # Si el mensaje empieza con el símbolo de invocación de Tux:
                cmd = split(data.message.content[1:])  # shlex.split() para obtener una lista con todos los argumentos del comando.
                print("Command detected")
                print(cmd)
                if cmd[0] in cmds.CMDS:  # Si el comando ingresado se encuentra dentro del diccionario de comandos:
                    print("Command recognized")
                    response = cmds.CMDS[cmd[0]](subclient, cmd[1:], data.message, DATA)  # Ejecuta el comando solicitado
                    try:
                        subclient.send_message(data.message.chatId, response[0], messageType=response[1])  # Envía el output
                    except:
                        pass
                elif cmd[0] == 'chsym':  # Comando para cambiar el símbolo de invocación de Tux.
                    if len(cmd) > 1:
                        DATA['SYM'] = cmd[1]
                        open('data', 'w').write(dumps(DATA, indent=4))
                    else:
                        subclient.send_message(data.message.chatId, "Falta un argumento: <Sym>")
            elif data.message.content == '¿Tux?':  # Comando para chequear si Tux está vivo y cuál es su símbolo de invocación.
                subclient.send_message(data.message.chatId, f"Estoy vivo.\n\nSym: {DATA['SYM']}")
