# def main():
#     print('Hello World')
#
#
# if __name__ == "__main__":
#     main()

t=int(input())
for test_case in range(1,t+1):
    #n은 물건 개수
    n=int(input())
    arr = list(map(int,input().split()))
    result=0
    arr.sort()
    while(True):
        if len(arr)==0:
            break
        if max(arr)-min(arr)==0:
            for i in arr:
                result+=i
            break
        num = len(arr)-1
        result+=arr[num]
        if arr[num] == arr[num-1]:
            if arr.count(arr[num]) == num:
                    result+=arr[num]*num
            arr.pop(num - 2)
        else:
            arr.pop(num-1)
        num2 = len(arr)-1
        arr.pop(num2)
    # print(f'#{tc} {result}')
    print("#%d" % test_case,end=' ')
    print("%d" %result)
    # print("#%d %d" % test_case, result)
    #     arr.sort()
    #
    #     maxV = max(arr)
    #     index=arr.index(maxV)
    #     # maxV=arr[2].pop()
    #     print(maxV)
    # print(arr)

    ######
    # t = int(input())
    # for tc in range(1, t + 1):
    #     # n은 물건 개수
    #     n = int(input())
    #     arr = list(map(int, input().split()))
    #     result = 0
    #     arr.sort()
    #     # for i in range(arr):
    #     while (True):
    #         if len(arr) == 0:
    #             print("len=0이라서 break")
    #             break
    #         if max(arr) - min(arr) == 0:
    #             for i in arr:
    #                 result += i
    #             print("max와 min 차이가 0이라서 break")
    #             break
    #         num = len(arr)
    #         print("arr[num-1]의 값은 :" + str(arr[num - 1]))
    #         result += arr[num - 1]
    #         print("result의 값은 :" + str(result))
    #         arr.pop(num - 1)
    #         arr.pop(num - 2)
    #         print(arr)
    #         # print(maxV)
    #         # print(arr)
    #     print(f'#{tc} {result}')

    ###
    # t = int(input())
    # for tc in range(1, t + 1):
    #     # n은 물건 개수
    #     n = int(input())
    #     arr = list(map(int, input().split()))
    #     result = 0
    #     arr.sort()
    #     # for i in range(arr):
    #     while (True):
    #         if len(arr) == 0:
    #             print("len=0이라서 break")
    #             break
    #         if max(arr) - min(arr) == 0:
    #             for i in arr:
    #                 result += i
    #             print("max와 min 차이가 0이라서 break")
    #             break
    #         num = len(arr) - 1
    #         print(num)
    #         print("arr[num-1]의 값은 :" + str(arr[num]))
    #         result += arr[num]
    #         print("result의 값은 :" + str(result))
    #         # if num == 1:
    #         #     result += arr[num] + arr[num - 1]
    #         if arr[num] == arr[num - 1]:
    #             arr.pop(num - 2)
    #         else:
    #             arr.pop(num - 1)
    #         num2 = len(arr) - 1
    #         arr.pop(num2)
    #         print("여기 " + str(arr))
    #         # arr.pop(num - 1)
    #         # else:
    #         print(arr)
    #         # print(maxV)
    #         # print(arr)
    #     print(f'#{tc} {result}')