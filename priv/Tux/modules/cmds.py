import random
from requests import get
from urllib import parse
from json import load
td = load(open('modules/td.json', 'r'))


def chnick(subclient, *params) -> tuple:
    """
    Cambiar el nickname
    :param subclient: amino.SubClient()
    :param params: nickname, message object
    :rtype: tuple
    """
    try:
        subclient.edit_profile(nickname=params[0][0])
        subclient.edit_profile(nickname=params[0][0])
        return "Hecho!", 0
    except:
        return "Error al configurar el nickname", 0


def chbio(subclient: object, *params) -> tuple:
    """
    Cambiar la biografía del perfil
    :param subclient: amino.SubClient()
    :param params: biografía, message object
    :rtype: tuple
    """
    subclient.edit_profile(content=params[0][0])
    return "Hecho!", 0


def chprofpic(subclient: object, *params) -> tuple:
    """
    Cambiar la foto del perfil
    :param subclient: amino.SubClient()
    :param params: None, data.message
    :rtype: tuple
    """
    if params[1].extensions and 'mediaValue' in params[1].extensions['replyMessage']:
        pic = params[1].extensions['replyMessage']['mediaValue']
    else:
        return "Error, el mensaje solicitado no es una imagen", 0
    try:
        subclient.edit_profile(icon=pic)
        subclient.edit_profile(icon=pic)
        return "Hecho!", 0
    except:
        return "Error al configurar la imagen", 0


def echo(*params) -> tuple:
    """
    Devuelve lo que se le pasa como argumento
    :param params: None, str, messageType=0
    :rtype: tuple
    """
    if len(params[1]) < 1:
        return "Falta un argumento: <string>", 0
    if len(params[1]) > 1 and params[1][1].isdigit():
        return params[1][0], int(params[1][1])
    return params[1][0], 0


def join(subclient: object, *params) -> tuple:
    """
    Une el bot a un chat
    :param subclient: amino.SubClient()
    :param params: link hacia el chat
    :rtype: tuple
    """
    try:
        subclient.join_chat(subclient.get_from_code(params[0][0]).objectId)
        return "Hecho!", 0
    except:
        return "Hubo un error en el proceso", 0


def leave(subclient: object, *params) -> tuple:
    """
    Deja el chat desde el que se ejecute el comando
    :param subclient: amino.SubClient()
    :param params: None, data.message
    :rtype: tuple
    """
    subclient.leave_chat(params[1].chatId)
    return "Hecho!", 0


def rm(subclient: object, *params) -> tuple:
    """
    Elimina la cantidad de mensajes que se especifiquen
    :param subclient: amino.SubClient
    :param params: numero de mensajes a eliminar, si se quiere eliminar como Staff
    :type params: int, bool
    :rtype: tuple
    """
    if params[0] and params[0][0].isdigit:
        if int(params[0][0]) > 50:
            return "No voy a borrar tantos mensajes, alta flojera", 0
        msg = subclient.get_chat_messages(params[1].chatId, int(params[0][0])).messageId
        if len(params[0]) > 1 and eval(params[0][1]):
            for i in msg:
                subclient.delete_message(chatId=params[1].chatId, messageId=i, asStaff=True, reason='-')
        else:
            for i in msg:
                subclient.delete_message(messageId=i, chatId=params[1].chatId)
        return f"Se han eliminado {len(msg)} mensajes", 0
    else:
        return "Se ha producido un error en la operación", 0


def choice(*params) -> tuple:
    """
    Escoge entre una lista de cosas
    :param params: None, lista separada por comas
    :rtype: tuple
    """
    li = [i.strip() for i in params[1][0].split(',')]
    li = list(filter(None, li))
    return random.choices(li)[0], 0


def rand(*params) -> tuple:
    """
    Devuelve un número aleatorio entre dos números dados
    :param params: None, dos números separados por comas
    :rtype: tuple
    """
    try:
        li = [int(i.strip()) for i in params[1][0].split(',')]
    except ValueError:
        return "Uno de los valores especificados no es un número", 0
    li = list(filter(None, li))
    if len(li) == 2:
        return str(random.randint(li[0], li[1])), 0
    else:
        return "La lista presenta más o menos de 2 números", 0


def truth(*params) -> tuple:
    return random.choices(td['Truth'])[0]['summary'], 0


def dare(*params) -> tuple:
    return random.choices(td['Dare'])[0]['summary'], 0


def newton(*params) -> tuple:
    return get(f'https://newton.now.sh/api/v2/simplify/{parse.quote(params[1][0])}').json()['result'], 0


CMDS = {
    'nickname': chnick,
    'bio': chbio,
    'set_ppic': chprofpic,
    'echo': echo,
    'join': join,
    'leave': leave,
    'rm': rm,
    'choice': choice,
    'random': rand,
    'truth': truth,
    'dare': dare,
    'math': newton
}
