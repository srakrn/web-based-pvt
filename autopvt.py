import socketio
import random
import time

s = socketio.Client()

s.connect("http://localhost:8888")

while True:
    t = random.triangular(3, 7)
    print("Emit")
    s.emit("control", {"to": "pvt", "action": "start", "duration": 500})
    time.sleep(t)
