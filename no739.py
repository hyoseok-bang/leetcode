# https://leetcode.com/problems/daily-temperatures/

def dailyTemperatures(T):
    answer = [0] * len(T)
    stack = list()
    for i, tmp in enumerate(T):

        # stack에 값이 남아있고, 현재 온도가 스택의 마지막 값의 온도보다 높으면 while문 실행
        while stack and tmp > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
            print(f"(while loop executed) answer[{last}] = {i} - {last}")
        stack.append(i)
        print(stack)
    
    return answer
