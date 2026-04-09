H,W,N,M = map(int,input().split())
import math 
#math.ceil() -> 숫자의 올림
a = math.ceil(W/(M+1))
b = math.ceil(H/(N+1))
print(a*b)       
