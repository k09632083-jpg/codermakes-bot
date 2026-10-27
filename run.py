import os,json,time,threading,urllib.request as U,urllib.parse as PR
TK=os.environ["BT"];AK=os.environ["GK"];SELF=os.environ.get("SELF","")
TG="https://api.telegram.org/bot"+TK
O=[0]
def call(url,data,hd,tm=60): return json.loads(U.urlopen(U.Request(url,data=data,headers=hd),timeout=tm).read())
def tg(m,**p): return call(TG+"/"+m,json.dumps(p).encode(),{"Content-Type":"application/json"})
def ai(t): return call("https://api.groq.com/openai/v1/chat/completions",json.dumps({"model":"qwen/qwen3.8-27b","messages":t}).encode(),{"Authorization":"Bearer "+AK,"Content-Type":"application/json"},120)["choices"][0]["message"]["content"]
def proc(u): m=u["message"];c=m["chat"]["id"];x=m["text"];tg("sendChatAction",chat_id=c,action="typing");a=ai([{"role":"system","content":"answer concisely in the user's language."},{"role":"user","content":x}]);[tg("sendMessage",chat_id=c,text=a[i:i+4000]) for i in range(0,len(a),4000)]
def stp(): d=tg("getUpdates",offset=O[0],timeout=25,allowed_updates="message")["result"];[proc(x) for x in d if x.get("message",{}).get("text")];O[0]=d[-1]["update_id"]+1 if d else O[0]
SO=__import__("socket").socket();SO.setsockopt(1,2,1);SO.bind(("0.0.0.0",int(os.environ.get("PORT","10000"))));SO.listen(9)
def ac(): c,a=SO.accept();c.sendall(b"HTTP/1.1 200 OK\r\nContent-Length: 2\r\n\r\nok");c.close()
threading.Thread(target=lambda: [ac() for _ in iter(int,1)],daemon=True).start()
def ka(): [time.sleep(40) or U.urlopen(SELF,timeout=10).read() for _ in iter(int,1)]
SELF and threading.Thread(target=ka,daemon=True).start()
while 1: stp()
