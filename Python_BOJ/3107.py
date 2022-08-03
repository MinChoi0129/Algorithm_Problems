short_ipv6, full_ipv6 = input(), []

if short_ipv6.count('::'):
    count = short_ipv6.count(':')
    if count == 8:
        short_ipv6 = list(short_ipv6.replace('::', ':0000:'))
        if short_ipv6[0] == ':': short_ipv6.pop(0)
        if short_ipv6[-1] == ':': short_ipv6.pop()
    else:
        idx = short_ipv6.index('::')
        short_ipv6 = list(short_ipv6)
        for _ in range(7 - count): short_ipv6.insert(idx, ':')

short_ipv6 = list(short_ipv6)
while True:
    try:
        idx = short_ipv6.index(':')
        full_ipv6.append('0' * (4 - idx) + ''.join(short_ipv6[:idx]))
        for _ in range(idx + 1): short_ipv6.pop(0)
    except:
        full_ipv6.append('0' * (4 - len(short_ipv6)) + ''.join(short_ipv6))
        break

print(':'.join(full_ipv6))