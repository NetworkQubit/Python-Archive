




p = int(input("Principal: "))
r = int(input("Interest: "))
t = int(input("Time: "))

SI = (p * r * t) / 100
CI = p * (1 + r / 100) ** t - p

print("Simple Interest: ",SI)
print("Compound Interest: ",CI)
