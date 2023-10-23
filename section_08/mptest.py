
import multiprocessing, os

def print_mp():
    print('I am process',os.getpid())

if __name__=='__main__': # needed to prevent errors from multiple loads
    print('Process',os.getpid(), 'spawning a new process')
    p=multiprocessing.Process(target=print_mp)
    p.start()
