import threading, time
t=threading.Lock()
def san(Name):
    for x in range(2):
        t.acquire()
        print(f"{Name}, S.No. {x}")
        t.release()
        time.sleep(5)
trd_1 = threading.Thread(target=san, args=("Anu K",))
trd_2 = threading.Thread(target=san, args=("Bhavi S",))
trd_3 = threading.Thread(target=san, args=("Chaithra M",))
trd_4 = threading.Thread(target=san, args=("Dhivi D",))

trd_1.start(); trd_2.start(); trd_3.start(); trd_4.start()
trd_1.join(); trd_2.join(); trd_3.join(); trd_4.join()
