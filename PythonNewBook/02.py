#배열 제어하기
#정수배열 받고 배열의 중복값 제거하고 내림차순으로 정렬해서 반환

def solution(arr):
    unique_lst =list(set(arr))
    unique_lst.sort(reverse=True)
    return unique_lst