from multiprocessing import Pool, Manager

def fill_array(index,arr):
    arr[index]=index**2

if __name__=='__main__':
    with Manager() as manager:
        arr=manager.list(range(10))
        
        with Pool(processes=2) as pool:
            dat = [(i,arr) for i in range(10)]
            res=pool.starmap_async(fill_array, dat)
            res.get(timeout=1)
            print(arr)
