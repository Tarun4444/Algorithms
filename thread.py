import threading
import os

def print_cube(num):
    print("cube:{}".format(num*num*num))

def print_square(num):
    print("square:{}".format(num*num))

def task1():
    print("Task1:{}".format(threading.current_thread().n))
    print("ID_1:{}".format(os.getpid()))

if __name__ == "__main__":

    t1=threading.Thread(target=print_square,args=(10,))
    t2=threading.Thread(target=print_cube,args=(10,))
    t3=threading.Thread(target=task1,n='Hola')
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()

    print("done")
