import time

def BinaryFib(k:int) -> int:
    global count
    count+=1
    if k <= 1:
        return k
    else:
        return BinaryFib(k-1) + BinaryFib(k-2)
    
def LinearFib(k:int) -> (int,int):
    global count
    count+=1
    if k == 1:
        return (k,0)
    else:
        (a,b) = LinearFib(k-1)
        return (a+b,a)

if __name__ == "__main__":
    count=0
    start = time.time()
    print(BinaryFib(20))
    end = time.time()
    print("BinaryFib(20) : {:.5f}".format(end-start))
    print("BinaryFib(20) count : {}".format(count))

    count=0
    start = time.time()
    print(LinearFib(20)[0])
    end = time.time()
    print("LinearFib(20) : {:.5f}".format(end-start))
    print("LinearFib(20) count : {}".format(count))
