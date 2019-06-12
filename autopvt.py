import socketio
import random
import time
import datetime

s = socketio.Client()
s.connect("http://localhost:8888")
received = True
before_time = datetime.datetime.now()

f = open("pvtlog.txt", "a")


@s.on("screen")
def after(data):
    global received
    if data["action"] == "tapped":
        print("Button received")
        after_time = datetime.datetime.now()
        f.write("{}\n".format(after_time - before_time))
        received = True


time.sleep(10)
while True:
    period = random.triangular(3, 7)
    before_time = datetime.datetime.now()
    s.emit("control", {"to": "pvt", "action": "start", "duration": 500})
    print("Transmitted")
    received = False
    while not received:
        pass
    time.sleep(period)
