import time

sec = int(input("unesite sekunde: "))
for i in range(sec, 0, -1):
    print(i)
    time.sleep(0.7)

print("Isteklo je vreme!")
