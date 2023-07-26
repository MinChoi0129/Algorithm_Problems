# 제일 처음 짠 코드
number_of_holes_of_power_strip, number_of_electric_devices = map(int, input().split())
electric_devices = [*map(int, input().split())]

plugged_devices = set()
pop_count = 0
for i in range(len(electric_devices)):
    device = electric_devices[i]

    if device not in plugged_devices and len(plugged_devices) < number_of_holes_of_power_strip:
        plugged_devices.add(device)
    else: # 안 꽂혀있는데도 빈자리도 없음
        when_to_use = dict()
        for plugged_device in plugged_devices:
            try:
                when_to_use[plugged_device] = electric_devices[i+1:].index(plugged_device)
            except:
                when_to_use[plugged_device] = int(1e9)
                break
        
        if when_to_use:
            지금꽂혀있는것중가장나중에쓸시간 = max(when_to_use.values())
            device_to_pop = [plugged_device for plugged_device in when_to_use if when_to_use[plugged_device] == 지금꽂혀있는것중가장나중에쓸시간][0]
            plugged_devices.remove(device_to_pop)
        else:
            plugged_devices.remove(plugged_devices[0])
        
        pop_count += 1
        plugged_devices.add(device)

print(pop_count)


# 한 번 줄여봄
number_of_holes_of_power_strip, number_of_electric_devices = map(int, input().split())
electric_devices = [*map(int, input().split())]
plugged_devices, pop_count = set(), 0

for i in range(len(electric_devices)):
    device = electric_devices[i]

    if device not in plugged_devices and len(plugged_devices) < number_of_holes_of_power_strip:
        plugged_devices.add(device)
    else: # 안 꽂혀있는데도 빈자리도 없음
        when_to_use = dict()
        for plugged_device in plugged_devices:
            try: when_to_use[plugged_device] = electric_devices[i+1:].index(plugged_device)
            except: when_to_use[plugged_device] = int(1e9); break
        
        device_to_pop = plugged_devices[0]
        if when_to_use:
            지금꽂혀있는것중가장나중에쓸시간 = max(when_to_use.values())
            device_to_pop = [plugged_device for plugged_device in when_to_use if when_to_use[plugged_device] == 지금꽂혀있는것중가장나중에쓸시간][0]
        
        plugged_devices.remove(device_to_pop); pop_count += 1
        plugged_devices.add(device)
        
print(pop_count)