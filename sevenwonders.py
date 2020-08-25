x = input()
T = 0
C = 0
G = 0
small = 0

for i in range(len(x)):
    if x[i] == 'T':
        T = T + 1
    elif x[i] == 'C':
        C = C + 1
    elif x[i] == 'G':
        G = G + 1
    else:
        print("Error")
if T == C and T < G:
    small = T
elif T == G and T < C:
    small == T
elif G == C and C < T:
    small == G
elif T < C and T < G:
    small = T
elif C < T and C < G:
    small = C
elif G < C and G < T:
    small = G
elif G == C or C == T:
    small = G
else:
    print("Error with small")
small = small * 7

print(T*T + C*C + G*G + small)