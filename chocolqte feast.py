def chocolateFeast(n, c, m):
    choco = n // c
    embalage = choco
    while embalage>=m:
        nbChoco = embalage // m
        choco+=nbChoco
        embalage = nbChoco + embalage%m
    return choco