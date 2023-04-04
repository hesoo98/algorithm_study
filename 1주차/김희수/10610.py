# https://www.acmicpc.net/problem/10610
# 30, 실버 4
# https://ko.wikipedia.org/wiki/%EB%B0%B0%EC%88%98_%ED%8C%90%EC%A0%95%EB%B2%95  (배수판정법)
a = list(map(int, input()))
if 0 not in a:  # 30의 배수면 0이 포함 되어야 함.
    print(-1)
else:
    a = sorted(a, reverse=True)  # 가장 큰수라 내림차수 정렬
    if sum(a) % 3 == 0:  # 배수판정법에 의하여 각자리수의 합이 3의배수여야 30의 배수가 됨.
        num = ""
        for i in a:
            num += str(i)
        print(num)
    else:
        # 배수가 아닐경우 출력 해줘야함.
        print(-1)
