import operator

n = int(input())
word_list = []
word_len_dic = {} # word 길이별 dict

for i in range(n) :
    word = input()
    if len(word) in word_len_dic : # 있으면 존재하는 리스트에 append
        word_len_dic[len(word)].append(word)

    else : # 없으면 담을 리스트 생성
        word_len_dic[len(word)] = [word]

sorted_dic = sorted(word_len_dic.items()) # 키를 기준으로 정렬
print(sorted_dic)

for key, value in sorted_dic : # list원소를 set하여 중복원소 제거
    for w in sorted(set(value)) :
        print(w)