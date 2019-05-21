num = int(input())
a, i = 1, 1 # 방의 끝번호, 방개수
while(num > a) :
    i += 1
    a += i
j = a - num # 방의 끝번호 - 자신 => 끝번호에서 얼만큼 떨어져있는지 ==  j
if i % 2 == 0 : # 방번호가 짝수이면 a가 (i, 1)
    print("{}/{}".format(i-j, 1+j))

else : # 홀수이면 a가 (1, i)
    print("{}/{}".format(1+j, i-j))