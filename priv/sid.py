import re
import base64

pink="\033[38;2;255;77;255m"
black = "\033[30m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
cyan = "\033[1;36m"
white = "\033[1;37m"
nm="\033[0m"

def decode_base64(data: str):
    d = data
    data = re.sub(rb'[^a-zA-Z0-9+/]', b'', data.encode())[:162]

    print("\n\n\t\tFunction\n\n")
    print(f"""{yellow}def{nm} {blue}decode_base64{nm}(data: {blue}str{nm}):
    data = re.sub(rb{pink}'[^a-zA-Z0-9+/]'{nm}, b{pink}''\033[0m, data.encode())[:{pink}162{nm}]
    {yellow}return{nm} base64.b64decode(data + b{pink}'='{nm} * (-{blue}len{nm}(data) % 4)).decode({pink}"cp437"{nm})[{pink}1{nm}:]""")

    print(f"\n\n{red}Original data:{nm} {d}")
    print(f"\n\n{red}data:{nm} {data}")
    print(f"\n\n{red}data + b'=':{nm} {data + b'='}")
    print(f"\n\n{red}-len(data):{nm} {-len(data)}")
    print(f"\n\n{red}-len(data) % 4:{nm} {-len(data) % 4}")
    print(f"\n\n{red}data + b'=' * (-len(data) % 4):{nm} {data + b'=' * (-len(data) % 4)}")
    print(f"\n\n{red}base64.b64decode(data + b'=' * (-len(data) % 4)):{nm} {base64.b64decode(data + b'=' * (-len(data) % 4))}")
    print(f"\n\n{red}base64.b64decode(data + b'=' * (-len(data) % 4)).decode('cp437'):{nm} {base64.b64decode(data + b'=' * (-len(data) % 4)).decode('cp437')}")
    print(f"\n\n{red}base64.b64decode(data + b'=' * (-len(data) % 4)).decode('cp437')[1:]:{nm} {base64.b64decode(data + b'=' * (-len(data) % 4)).decode('cp437')[1:]}")
    print(f"\n\n{red}Arreglado:{nm} {base64.b64decode(data + b'=' * (-len(data) % 4)).decode('cp437') + '}'}")


    return base64.b64decode(data + b'=' * (-len(data) % 4)).decode("cp437")[1:]

if __name__=='__main__':
    sid = input("SID: ")
    decode_base64(sid)
