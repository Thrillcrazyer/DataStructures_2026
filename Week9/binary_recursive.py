import time
import math

def SOLVE(N):
    global totalcall
    totalcall += 1
    if N==1:
        return 1
    elif N<1:
        return 0
    else:
        return SOLVE(N//2)+SOLVE(N-N//2)

A=[0]*10000001

def SOVLE2(N):
    global totalcall
    totalcall += 1
    if A[N]!=0:
        return A[N]
    if N==1:
        A[N]=1
    elif N<1:
        A[N]=0
    else:
        A[N]=SOVLE2(N//2)+SOVLE2(N-N//2)
    return A[N]



if __name__ == "__main__":
    
    K=10000000
    totalcall=0
    
    print("1. SOLVE Test")
    start_time = time.time()
    print(SOLVE(K))
    totaltime1=time.time() - start_time
    print(f"SOLVE took {totaltime1:.8f} seconds")
    print(f"SOLVE total calls: {totalcall}")
    
    totalcall=0
    print("\n2. SOVLE2 Test")
    start_time = time.time()
    print(SOVLE2(K))
    totaltime2=time.time() - start_time
    print(f"SOVLE2 took {totaltime2:.8f} seconds")
    print(f"SOVLE2 total calls: {totalcall}")
    