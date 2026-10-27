def ac(): c,a=SO.accept();c.sendall(b"HTTP/1.1 200 OK\r\nContent-Length: 2\r\n\r\nok");c.close()
threading.Thread(target=lambda: [ac() for _ in iter(int,1)],daemon=True).start()
def ka(): [time.sleep(40) or U.urlopen(SELF,timeout=10).read() for _ in iter(int,1)]
SELF and threading.Thread(target=ka,daemon=True).start()
while 1: stp()
