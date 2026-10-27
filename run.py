import os,json,time,threading,urllib.request as U,urllib.parse as PR
TK=os.environ["BT"];AK=os.environ["GK"];SELF=os.environ.get("SELF","")
TG="https://api.telegram.org/bot"+TK
OA={"User-Agent":"CodermakesBot/1.0"}
O=[1] if not os.path.exists("off.txt") else [int(open("off.txt").read().strip() or 0)]
