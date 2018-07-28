import socket


def select_room():
    roomname = input("请选择房间 \n：(输入房间序号以选择）")
    obj.sendall(bytes(roomname, encoding="utf-8"))
    room_welcome_ret_bytes = obj.recv(1024)
    room_welcome_ret_str = str(room_welcome_ret_bytes,encoding="utf-8")
    print(room_welcome_ret_str)


player_name = input("请输入玩家昵称：")        #设定玩家昵称

obj = socket.socket()               #与服务器建立连接
obj.connect(("127.0.0.1", 8080))

obj.sendall(bytes(player_name, encoding="utf-8"))       #上传玩家名称
print("已设定玩家昵称为"+player_name)
onlineplayer_ret_bytes = obj.recv(1024)     #获得在线玩家列表
onlineplayer_ret_str = str(onlineplayer_ret_bytes, encoding="utf-8")
print("在线玩家："+onlineplayer_ret_str)

server_welcome_ret_bytes = obj.recv(1024)
server_welcome_ret_str = str(server_welcome_ret_bytes, encoding="utf-8")
print(server_welcome_ret_str)

select_room()

while True:
    inp = input("请输入内容（输入q以退出） >>>")
    if inp == "q":
        obj.sendall(bytes(inp, encoding="utf-8"))
        break
    else:
        obj.sendall(bytes(inp, encoding="utf-8"))
        chat_ret_bytes = obj.recv(1024)
        chat_ret_str = str(chat_ret_bytes, encoding="utf-8")
        print(chat_ret_str)