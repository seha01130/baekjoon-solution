n = int(input())

dp = [0, 1, 2]  # n이 2이하일때 횟수를 미리 초기화
if n > 2:  # 만약 n이 3보다 크다면
    dp = dp + ([0] * (n - 2))  # 반복문을 돌기 위해 그 이후의 n-2개를 dp배열에 추가해준다.
    for i in range(3, n + 1):  # 3 부터 n 까지 점화식을 돈다.
        dp[i] = dp[i - 1] + dp[i - 2]  # 3번째 항부터 1,2번째 항의 합과 같다. (i번째 항은 i-2번째항과 i-1번째 항의 값과 같다.)

print(dp[n] % 10007)  # 출력