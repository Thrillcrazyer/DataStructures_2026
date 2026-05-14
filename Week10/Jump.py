import time
import random
random.seed(20260514)

N=6

def readtable(s:str)->list:
    t = []
    for line in s.splitlines():
        t.append(list(map(int, line.split())))
    return t

def jump(y:int,x:int)->bool:
    if y == N and x == N:
        return True
    else:
        if y < 0 or y > N or x < 0 or x > N:
            return False
        else:
            jumpSize = t[y][x]
            return jump(y+jumpSize,x) or jump(y,x+jumpSize)

def jump2(y:int,x:int)->bool:
    if y == N and x == N:
        return True
    else:
        if y < 0 or y > N or x < 0 or x > N:
            return False
        if cache[y][x] != -1:
            return cache[y][x]
        else:
            jumpSize = t[y][x]
            t[y][x] = 'X'
            cache[y][x] = jump2(y+jumpSize,x) or jump2(y,x+jumpSize)
            return cache[y][x]


if __name__ == "__main__":
    N=6
    
    
    print("TEST CASE 1 : ")
    t1="""2 5 1 6 1 4 1
6 1 1 2 2 9 3
7 2 3 2 1 3 1
1 1 3 1 7 1 2
4 1 2 3 4 1 2
3 3 1 2 3 4 1
1 5 2 9 4 7 0"""
    t=readtable(t1)
    cache=[[-1 for _ in range(N+1)] for _ in range(N+1)]
    print(t1)
    print("-"*15)
    
    start_time = time.time()
    j1=jump(0,0)
    end_time = time.time()
    print(f"Execution time for jump: {end_time - start_time} seconds")
    
    start_time = time.time()
    j2=jump2(0,0)
    end_time = time.time()
    print(f"Execution time for jump2: {end_time - start_time} seconds")
    
    print(f"Expected Answer : True , Actual Answer Jump: {j1} , Actual Answer Jump2: {j2}")
    
    print("TEST CASE 2 : ")
    t2="""2 5 1 6 1 4 1
6 1 1 2 2 9 3
7 2 3 2 1 3 1
1 1 3 1 7 1 2
4 1 2 3 4 1 3
3 3 1 2 3 4 1
1 5 2 9 4 7 0 """
    t=readtable(t2)
    print(t2)
    print("-"*15)
    cache=[[-1 for _ in range(N+1)] for _ in range(N+1)]
    start_time = time.time()
    j1=jump(0,0)
    end_time = time.time()
    print(f"Execution time for jump: {end_time - start_time} seconds")
    
    start_time = time.time()
    j2=jump2(0,0)
    end_time = time.time()
    print(f"Execution time for jump2: {end_time - start_time} seconds")
    
    print(f"Expected Answer : True , Actual Answer Jump: {j1} , Actual Answer Jump2: {j2}")
    
    print("TEST CASE 3 : ")
    t3="""1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 0"""

    t=readtable(t3)
    print(t3)
    print("-"*15)
    cache=[[-1 for _ in range(N+1)] for _ in range(N+1)]
    
    start_time = time.time()
    j1=jump(0,0)
    end_time = time.time()
    print(f"Execution time for jump: {end_time - start_time} seconds")
    
    start_time = time.time()
    j2=jump2(0,0)
    end_time = time.time()
    print(f"Execution time for jump2: {end_time - start_time} seconds")
    
    print(f"Expected Answer : True , Actual Answer Jump: {j1} , Actual Answer Jump2: {j2}")
    
    N=60
    
    print("TEST CASE 4 : ")
    t4 = "\n".join([" ".join([str(random.randint(1, 9)) for _ in range(N+1)]) for _ in range(N+1)])
    
    print(t4)
    print("-"*int(N*2))
    t=readtable(t4)
    cache=[[-1 for _ in range(N+1)] for _ in range(N+1)]
    
    start_time = time.time()
    j1=jump(0,0)
    end_time = time.time()
    print(f"Execution time for jump: {end_time - start_time} seconds")
    
    start_time = time.time()
    j2=jump2(0,0)
    end_time = time.time()
    print(f"Execution time for jump2: {end_time - start_time} seconds")
    
    print(f"Expected Answer : True , Actual Answer Jump: {j1} , Actual Answer Jump2: {j2}")
    
    N=65
    
    print("TEST CASE 5 : ")
    t5 = "\n".join([" ".join([str(random.randint(1, 9)) for _ in range(N+1)]) for _ in range(N+1)])
    
    print(t5)
    print("-"*int(N*2))
    t=readtable(t5)
    cache=[[-1 for _ in range(N+1)] for _ in range(N+1)]
    
    start_time = time.time()
    j1=jump(0,0)
    end_time = time.time()
    print(f"Execution time for jump: {end_time - start_time} seconds")
    
    start_time = time.time()
    j2=jump2(0,0)
    end_time = time.time()
    print(f"Execution time for jump2: {end_time - start_time} seconds")
    
    print(f"Expected Answer : True , Actual Answer Jump: {j1} , Actual Answer Jump2: {j2}")
    
    
    