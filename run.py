def proc(u): m=u["message"];c=m["chat"]["id"];x=m["text"];tg("sendChatAction",chat_id=c,action="typing");a=ai([{"role":"system","content":"answer concisely in the user's language."},{"role":"user","content":x}]);[tg("sendMessage",chat_id=c,text=a[i:i+4000]) for i in range(0,len(a),4000)]
def stp(): d=tg("getUpdates",offset=O[0],timeout=25,allowed_updates="message")["result"];[proc(x) for x in d if x.get("message",{}).get("text")];O[0]=d[-1]["update_id"]+1 if d else O[0]
SO=__import__("socket").socket();SO.setsockopt(1,2,1);SO.bind(("0.0.0.0",int(os.environ.get("PORT","10000"))));SO.listen(9)
