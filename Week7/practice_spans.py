

def arraySpan(X: list, n: int) -> list:
    A = LStack()
    S = [0] * n

    for i in range(n):
        while not A.isEmpty() and X[A.top_element()] <= X[i]:
            A.pop()
        if A.isEmpty():
            S[i] = i + 1
        else:
            S[i] = i - A.top_element()
            
        A.push(i)
    return S


if __name__ == '__main__':
    print("데이터 구조 및 알고리즘 실습 - 2026/04/16 - Practice: Spans\n")
    
    ## Test Case 1
    
    X = [6,3,4,5,2]
    print(f"{'Case 1':<10}: {str(X):<20}")
    expected_output = [1, 1, 2, 3, 1]
    print(f"{'Input Array':<15}: {X}")
    n = len(X)
    spans = arraySpan(X, n)
    print(f"{'Expected Output':<15}: {expected_output}")
    
    if spans == expected_output:
        print("Case 1번 통과")
        print(f"{'Your Output':<15}: {spans}")
    else:
        print("Case 1번 실패")
        print(f"{'Your Output':<15}: {spans}")
    print("-" * 30)
    
    ## Test Case 2
    X = [1, 2, 3, 4, 5]
    print(f"{'Case 2':<10}: {str(X):<20}")
    expected_output = [1, 2, 3, 4, 5]
    print(f"{'Input Array':<15}: {X}")
    n = len(X)
    spans = arraySpan(X, n)
    print(f"{'Expected Output':<15}: {expected_output}")
    if spans == expected_output:
        print("Case 2번 통과")
        print(f"{'Your Output':<15}: {spans}")
    else:
        print("Case 2번 실패")
        print(f"{'Your Output':<15}: {spans}")
    print("-" * 30)
    
    ## Test Case 3
    X = [5, 4, 3, 2, 1]
    print(f"{'Case 3':<10}: {str(X):<20}")
    expected_output = [1, 1, 1, 1, 1]
    print(f"{'Input Array':<15}: {X}")
    n = len(X)
    spans = arraySpan(X, n)
    print(f"{'Expected Output':<15}: {expected_output}")
    if spans == expected_output:
        print("Case 3번 통과")
        print(f"{'Your Output':<15}: {spans}")
    else:
        print("Case 3번 실패")
        print(f"{'Your Output':<15}: {spans}")
    print("-" * 30)
    
    ## Test Case 4
    X = [3, 3, 3, 3, 3]
    print(f"{'Case 4':<10}: {str(X):<20}")
    expected_output = [1, 2, 3, 4, 5]
    print(f"{'Input Array':<15}: {X}")
    n = len(X)
    spans = arraySpan(X, n)
    print(f"{'Expected Output':<15}: {expected_output}")
    if spans == expected_output:
        print("Case 4번 통과")
        print(f"{'Your Output':<15}: {spans}")
    else:
        print("Case 4번 실패")
        print(f"{'Your Output':<15}: {spans}")
    print("-" * 30)
    
