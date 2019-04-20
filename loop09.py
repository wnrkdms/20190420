#1부터 1000까지의 수 중에 7의 배수를 생략한 합을 구하세요.
s = 0
i = 1

while i <= 100:
    if i % 7 == 0:
        i += 1
        continue
    s += i
    i += 1

print("1부터 1000까지의 수 중에 7의 배수를 생략한 합",s)

s = 0
for i in range(1, 101):
    if i % 7 == 0:
        continue
    s += i

print("1부터 1000까지의 수 중에 7의 배수를 생략한 합", s)
