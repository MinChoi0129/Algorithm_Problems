for _ in range(int(input())):
    n, key1, key2, encrypted = int(input()), input().split(), input().split(), input().split()
    decrypted = ['' for _ in range(n)]
    for idx in range(n):
        decrypted[idx] = encrypted[key2.index(key1[idx])]
    print(' '.join(decrypted))