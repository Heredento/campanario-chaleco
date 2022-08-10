import os, time as t, threading
def imWaiting(a, b):
    print("I'm starting to wait...", a)
    t.sleep(5)
    print("I've finished waiting", b)
    

waiting = threading.Thread(target=imWaiting, name="The waiter", args=("owo", "uwu"))
                                                    ## args=the args, 
print("Things are getting started..")
waiting.start()
threadlist=[]
for thread in threading.enumerate():
    threadlist.append(thread.name)
print(threadlist)

# thread_lenght=len(threadlist)


for i in range(1, 20):
    print(f"A second has passed and i is equal to: {i}")        
    t.sleep(1)

for thread in threading.enumerate():
    threadlist.append(thread.name)
print(threadlist)
print("Things have finished haha")
