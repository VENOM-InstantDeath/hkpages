import amino
from modules import color
# from modules import chelp
from modules import cmds
from os import listdir, system
from json import dumps, load
from getpass import getpass
from time import sleep
from shlex import split

client = amino.Client()  # Global class

# Inicia sesión
while True:
    if "data" not in listdir():
        print("\t\tInicia sesión\n\n")
        DATA = {'CREDS': {"email": input("Correo electrónico: "), "password": getpass("Contraseña: ")},
                'SYM': '/',
                'OWNER': ['83e9eb60-3b0e-4009-8b67-dbe432ddae14'],
                'ADMIN': ['83e9eb60-3b0e-4009-8b67-dbe432ddae14']
                }
        try:
            client.login(**DATA['CREDS'])
        except amino.exceptions.InvalidAccountOrPassword:
            print("\nCorreo o contraseña incorrectos")
            print("Presiona enter para continuar.")
            input()
            system("clear")
            continue
        F = open("data", "w+")
        F.write(dumps(DATA, indent=4))
        F.close()
        print("\033[2J")
    else:
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
            DATA['COMM'] = client.search_community(DATA['COMM']).comId[0]
            client.join_community(DATA['COMM'])
        except amino.exceptions.CommunityNotFound:
            print("Comunidad inexistente.")
            sleep(1)
            print("\033[2J")
            continue
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

def reconsocketloop():
    while (1):
        shandle = clienteAmino.socket
        print(threading.active_count())
        shandle.close()
        shandle.start()
        time.sleep(480)


@client.callbacks.event("on_group_member_join")
def on_group_member_join(data):
    subclient.send_message(data.message.chatId, f"Bienvenido/a al chat, {data.message.author.nickname}")


@client.callbacks.event("on_group_member_leave")
def on_group_member_leave(data):
    subclient.send_message(data.message.chatId, "Mal ahí, se nos fue un miembro xD")


@client.callbacks.event("on_text_message")
def on_text_message(data):
    if str(data.comId) == str(DATA['COMM']):
        if __name__ == '__main__':
            if data.message.content[0] == DATA['SYM']:
                cmd = split(data.message.content[1:])
                print("Command detected")
                print(cmd)
                if cmd[0] in cmds.CMDS:
                    print("Command recognized")
                    response = cmds.CMDS[cmd[0]](subclient, cmd[1:], data.message, DATA)
                    try:
                        subclient.send_message(data.message.chatId, response[0], messageType=response[1])
                    except:
                        pass
                elif cmd[0] == 'chsym':
                    if len(cmd) > 1:
                        DATA['SYM'] = cmd[1]
                        open('data', 'w').write(dumps(DATA, indent=4))
                    else:
                        subclient.send_message(data.message.chatId, "Falta un argumento: <Sym>")
            elif data.message.content == '¿Tux?':
                subclient.send_message(data.message.chatId, f"Estoy vivo.\n\nSym: {DATA['SYM']}")
