def isAllSame(letters):
    for letter in letters[1:]:
        if letters[0] != letter:
            return False
    return True

n = int(input())
joined_ips =  []
for _ in range(n):
    joined_ips.append(''.join([*map(lambda x: bin(int(x))[2:].zfill(8), input().split('.'))]))
    
all_same_last_index = -1
for index in range(32):
    if isAllSame([joined_ip[index] for joined_ip in joined_ips]): all_same_last_index = index
    else: break

network_address = joined_ips[0][:all_same_last_index + 1] + '0' * (32 - (all_same_last_index + 1))
netmask_address = '1' * (all_same_last_index + 1) + '0' * (32 - (all_same_last_index + 1))

print(str(int(network_address[:8], 2)) + '.' + str(int(network_address[8:16], 2)) + '.' + str(int(network_address[16:24], 2)) + '.' + str(int(network_address[24:], 2)))
print(str(int(netmask_address[:8], 2)) + '.' + str(int(netmask_address[8:16], 2)) + '.' + str(int(netmask_address[16:24], 2)) + '.' + str(int(netmask_address[24:], 2)))