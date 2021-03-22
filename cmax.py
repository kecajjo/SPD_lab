



#permutation - konkretna kolejnosc zadan do realizacji,
def calculate(permutation, table):
    m = [0] * len(permutation)  #robienie miejsca listę
    for i in permutation:
        for j in range(0, len(table[0])): #inaczej ilosc maszyn
            if j == 0:
                m[j] += table[i-1][j] #i-1 bo w wektorze permutacji mamy liczby od 1 i bysmy wyleciali poza tablice
            else:
                m[j] = max(m[j], m[j-1]) + table[i-1][j]
    return max(m)