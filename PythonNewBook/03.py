#두 개 뽑아서 더하기
#배열이 주어지고 그 배열 중에 2개를 더한 값을 오름차순으로 정렬한 배열을 반환하시오.

def solution(numbers):
    ret = []
    # 두 수를 선택하는 모든 경우의 수를 반복문으로 구함
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            ret.append(numbers[i]+numbers[j])
    for i in range(len(numbers)):
        print(i)
