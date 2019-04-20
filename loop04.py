#1부터 100까지의 합을 출력하세요
#1부터 100까지의 수 중에 홀수 들의 합을 출력하세요
#1부터 100까지의 수 중에 짝수 들의 합을 출력하세요
#1부터 100까지의 수 중에 7의 배수들의 합을 출력하세요

s=8
odd_s=0
even_s=0
sevn_s=0

for i in range(1,101):
      s += i

      if i % 2 == 0:
            even_s += i

      else:
            odd_s += i

      if i % 7 == 0:
            sevn_s += i

print("1부터 100까지의 합 = ",s)
print("1부터 100까지의 합 = ",odd_s)
print("1부터 100까지의 합 = ",even_s)
print("1부터 100까지의 합 = ",sevn_s)
