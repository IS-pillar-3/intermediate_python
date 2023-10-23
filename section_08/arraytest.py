import multiprocessing

def fill_array(arr):
    arr[:]=[5,6,7]
    
if __name__=='__main__':
    dat=multiprocessing.Array('i',[1,2,3])
    p=multiprocessing.Process(target=fill_array,args=(dat,))
    p.start()
    p.join()
    print(dat[:])
