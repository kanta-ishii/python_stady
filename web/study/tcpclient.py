'''
手順
1, このpythonファイルを実行してTCP通信を行う
2, Chromeで http://localhost:8080 を投げる
'''

import socket

class TCPServer:
    '''TCP通信を行う'''
    def serve(self):
        print("=== サーバーを起動します ===")
        try:
            server_socket = socket.socket()
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            server_socket.bind(("localhost", 8080))
            server_socket.listen(1)

            print("=== クライアントからの接続を待つ ===")
            (client_socket, address) = server_socket.accept()
            print(f"=== クライアントとの接続が完了しました remote_address: {address} ===")

            request = client_socket.recv(4096) #データを取得する

            with open("web/study/server_recv.txt", "wb") as f:
                f.write(request)

            client_socket.close()

        finally:
            print("=== サーバーを停止します。 ===")


if __name__ == '__main__':
    server = TCPServer()
    server.serve()