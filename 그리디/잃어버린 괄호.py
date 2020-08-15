# 문제
# 세준이는 양수와 +, -, 그리고 괄호를 가지고 길이가 최대 50인 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.
#
# 그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
#
# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다.
# 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다.
#
# 출력
# 첫째 줄에 정답을 출력한다.
#
# 예제 입력 1
# 55-50+40
# 예제 출력 1
# -35

# 먼저 - 를 기준으로 배열을 나눈다. 이러한 형식으로 나뉜 원소들마다 모두 더해주고 배열을 만든다음
# 배열 사이사이를 - 를 넣는다.
# 모두 더해버린다.
math_expression = input()
# -를 기준으로 나눈다.
math_expression = math_expression.split('-')
math_number = []

for i in math_expression:
    tmp = i.split('+')
    tmp = map(int, tmp)
    math_number.append(sum(tmp))

answer = math_number[0] * 2 - sum(math_number)
print(answer)










