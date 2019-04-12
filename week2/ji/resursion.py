# n개의 숫자를 받아서 모두 더한 값 출력해주는 재귀식함수

def allSum(numList) :
    if len(numList) <= 0 :
        return 0
    else :
        return numList.pop() + allSum(numList)

numList = list(map(int,(input('input : ').split())))
print("output :", allSum(numList))





