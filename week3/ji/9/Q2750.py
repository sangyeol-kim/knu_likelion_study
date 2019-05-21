# 삽입정렬 거품정렬
# insert sort
'''
1. 삽입정렬의 개념과 구현
처음부터 마지막까지 각 원소의 알맞은 위치를 탐색하여 insert
배열의 2번째 원소부터 마지막 원소까지 차례대로 key값으로 설정하여
그 key값이 알맞은 자리를 찾아갈 수 있도록
key 이전의 원소들 즉, 이미 정렬된 배열부분과
비교해가며 알맞은 위치를 찾아 삽입한다.

삽입시 삽입위치 앞쪽의 원소들은 모두 인덱스를 +1 씩 증가시킨다
2. 시간복잡도
외부루프 : key를 설정 : len() - 1번 : n-1
내부루프 : key-1 만큼(최악)
>> O(n^2)
'''
def insert_sort(num_list) :
    # 첫번째 원소는 이미 정렬완료
    # 두번째 원소부터 정렬
    for i in range(1, len(num_list)) : # key
        key = num_list[i]
        # 현재 정렬된 배열은 i-1까지 이므로 i-1번째부터 역순으로 조사한다.
        # 이때 j의 범위는 i-1 ~ 0 까지 이다.
        for j in range(i-1, -1, -1) :
            if key < num_list[j] : # key를 insert해주기위해 오른쪽으로 밀기
                num_list[j+1] = num_list[j]
            else : # insert key
                num_list[j+1] = key
                break
    return

# bubble sort
'''
1. 버블정렬의 개념과 구현
서로 인접한 두 원소를 검사하여 정렬
0 1 > 1 2 > 2 3 > 3 4 ...
1회전 수행시 탐색한 배열에서 가장 큰 원소가 맨 뒤로감
즉, n회전 수행시 정렬완료

2. 버블정렬의 시간복잡도
외부루프 : n회전 수행 : n번
내부루프 : n 인덱스까지의 회전이라면 n-1번 수행 : n-1
n-1, n-2, n-3...2, 1번 = n(n-1)/2 == O(n^2)   
'''


def bubble_sort() :
    

num_length = (int(input())) # 입력받을 수의 개수
num_list = []
for _ in range(num_length) :
    num_list.append(int(input())) # 입력받은 수들의 list

print("original :", num_list)
insert_sort(num_list)
print("insert_sort :", num_list)

