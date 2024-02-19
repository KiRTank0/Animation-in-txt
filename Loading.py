import runpy
import time

i = 0
list_of_symbols = ["|","/","-","\\"]

reply = input("Type (start) to initiate:""\n")

while reply == "start":
    X = list_of_symbols[i]

    spin = open("spin.txt", "w")
    spin.write(X)
    spin.close()

    time.sleep(0.2)
    i += 1
    if i == 4:
        i = 0

else:
    "Wrong input"
    runpy.run_path("Loading.py")
