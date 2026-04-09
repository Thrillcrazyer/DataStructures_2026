from linkedlistStack import LStack


def parenmatch(X:str,n:int)->bool:
    s=LStack()
    for i in range(n):
        if X[i] in '({[':
            s.push(X[i])
        elif X[i] in ')}]':
            if s.isEmpty():
                return False
            else:
                top=s.pop()
                if (X[i]==')' and top!='(') or (X[i]=='}' and top!='{') or (X[i]==']' and top!='['):
                    return False
    return s.isEmpty()

if __name__=='__main__':
    X ='{[킬링캠프(시발점),뉴런, 드릴제로]드릴}'
    print(f"{'Case 1':<10}: {X:<20}")
    n = len(X)
    if parenmatch(X,n) == True:
        print("Case 1번 통과")
    else:
        print("Case 1번 실패")

    print("-" * 30)
    
    X ='{{{{{{{}'
    print(f"{'Case 2':<10}: {X:<20}")
    n = len(X)
    if parenmatch(X,n) == False:
        print("Case 2번 통과")
    else:
        print("Case 2번 실패")
    print("-" * 30)
    
    X ='{[({}){}][나는 롯데팬이여서 행복합니다][]()()}'
    print(f"{'Case 3':<10}: {X:<20}")
    n = len(X)
    if parenmatch(X,n) == True:
        print("Case 3번 통과")
    else:
        print("Case 3번 실패")
    print("-" * 30)
    
    X ='}'
    print(f"{'Case 4':<10}: {X:<20}")
    n = len(X)
    if parenmatch(X,n) == False:
        print("Case 4번 통과")
    else:
        print("Case 4번 실패")
    print("-" * 30)
    
    X ='[かわいいだけじゃだめですか？'
    print(f"{'Case 5':<10}: {X:<20}")
    n = len(X)
    if parenmatch(X,n) == False:
        print("Case 5번 통과")
    else:
        print("Case 5번 실패")
    print("-" * 30)
    
    