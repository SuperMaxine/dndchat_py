import socketserver


class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        #接收用户名、更新用户列表
        playername_ret_bytes = conn.recv(1024)
        playerlist = ['host']
        playerlist.append(str(playername_ret_bytes,encoding="utf-8"))
        print("玩家"+str(playername_ret_bytes,encoding="utf-8")+"已加入\n在线玩家："+",".join(playerlist))
        conn.sendall(bytes(",".join(playerlist), encoding="utf-8"))
        #欢迎信息↓
        conn.sendall(bytes("您已连接至" + servername + "\n房间列表：\n" + roomlist_str, encoding="utf-8"))
        roomnumber_ret_bytes = conn.recv(1024)
        roomnumber = int(str(roomnumber_ret_bytes, encoding="utf-8"))
        conn.sendall(bytes("您已连接至" + roomlist[roomnumber], encoding="utf-8"))

        while True:
            ret_bytes = conn.recv(1024)
            ret_str = str(ret_bytes, encoding="utf-8")
            if ret_str == "q":
                break
            else:
                conn.sendall(bytes(ret_str + "你好我好大家好", encoding="utf-8"))


if __name__ == "__main__":
    servername = input("请输入服务器名称：")
    roomlist = ["defult"]
    roomlist[0] = input("请创建初始房间：")
    roomlist_str = str(roomlist[::])
    print(roomlist)
    print("服务器正在运行")
    server = socketserver.ThreadingTCPServer(("127.0.0.1", 8080), Myserver)
    server.serve_forever()