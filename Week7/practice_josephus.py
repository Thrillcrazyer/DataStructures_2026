from linkedListQueue import LQueue

def josephus(people, k):
    queue = LQueue()
    
    for person in people:
        queue.enqueue(person)
    
    result = []
    
    while not queue.isEmpty():
        for _ in range(k - 1):
            queue.enqueue(queue.dequeue())
        result.append(queue.dequeue())
    return result

if __name__ == '__main__':
    print("데이터 구조 및 알고리즘 실습 - 2026/04/16 - Practice: Josephus\n")
    
    ## Test Case 1
    people = [
        '에스쿱스', '정한', '조슈아', '준', '호시', '원우', '우지',
        '디에잇', '민규', '도겸', '승관', '버논', '디노'
    ]
    k = 2
    print(f"{'Case 1':<10}: 세븐틴 People: {people}, k: {k}")
    expected_output = ['정한', '준', '원우', '디에잇', '도겸', '버논', '에스쿱스', '호시', '민규', '디노', '우지', '조슈아', '승관']
    print(f"{'Expected Output':<15}: {expected_output}")
    
    result = josephus(people, k)
    if result == expected_output:
        print("Case 1번 통과")
        print(f"{'Your Output':<15}: {result}")
    else:
        print("Case 1번 실패")
        print(f"{'Your Output':<15}: {result}")
    print("-" * 30)
    
    ## Test Case 2
    people = [
        '안유진', '가을', '레이', '장원영', '이서', '리즈'
    ]
    k = 5
    print(f"{'Case 2':<10}: 아이브 People: {people}, k: {k}")
    expected_output = ['이서', '장원영', '리즈', '가을', '레이', '안유진']
    print(f"{'Expected Output':<15}: {expected_output}")
    
    result = josephus(people, k)
    if result == expected_output:
        print("Case 2번 통과")
        print(f"{'Your Output':<15}: {result}")
    else:
        print("Case 2번 실패")
        print(f"{'Your Output':<15}: {result}")
    print("-" * 30)
    
    ## Test Case 3
    people = [
        '태양', 'TOP', 'GD', '승리', '대성'
    ]
    k = 2
    print(f"{'Case 3':<10}: 빅뱅 People: {people}, k: {k}")
    expected_output = ['TOP', '승리', '태양', '대성', 'GD']
    print(f"{'Expected Output':<15}: {expected_output}")
    
    result = josephus(people, k)
    if result == expected_output:
        print("Case 3번 통과")
        print(f"{'Your Output':<15}: {result}")
    else:
        print("Case 3번 실패")
        print(f"{'Your Output':<15}: {result}")
    print("-" * 30)
    
    ## Test Case 4
    people = [
        '박택현'
    ]
    k = 5
    print(f"{'Case 4':<10}: 데구알 People: {people}, k: {k}")
    expected_output = ['박택현']
    print(f"{'Expected Output':<15}: {expected_output}")
    
    result = josephus(people, k)
    if result == expected_output:
        print("Case 4번 통과")
        print(f"{'Your Output':<15}: {result}")
    else:
        print("Case 4번 실패")
        print(f"{'Your Output':<15}: {result}")
    print("-" * 30)
    
    ## Test Case 5
    people = [
        '지유','이솔','수이','하음','키야'
    ]
    k = 8
    print(f"{'Case 5':<10}: 키키 People: {people}, k: {k}")
    expected_output = ['수이', '이솔', '키야', '하음', '지유']
    print(f"{'Expected Output':<15}: {expected_output}")
    
    result = josephus(people, k)
    if result == expected_output:
        print("Case 5번 통과")
        print(f"{'Your Output':<15}: {result}")
    else:
        print("Case 5번 실패")
        print(f"{'Your Output':<15}: {result}")
    print("-" * 30)