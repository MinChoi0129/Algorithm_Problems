import os
followerFILE = open("follower.txt", mode = "r",  encoding="utf-8")
followingFILE = open("following.txt", mode = "r",  encoding="utf-8")
follower, following, j = [], [], 0
os.system("cls")
for i in followerFILE:
    if "님의 프로필 사진" in i:
        follower.append(i[:-10])

for i in followingFILE:
    if "님의 프로필 사진" in i:
        following.append(i[:-10])

len_of_longest_letter = 0
for i in follower:
    if len(i) > len_of_longest_letter:
        len_of_longest_letter = len(i)
for i in following:
    if len(i) > len_of_longest_letter:
        len_of_longest_letter = len(i)


print("팔로워 수: ", len(follower))
print("팔로잉 수: ", len(following))

print("\n내가 팔로우 하지만 상대는 안하는 경우  : ")
for i in following:
    if i not in follower:
        print("%25s" %(i), end = " | ")
        j += 1
        if j == 4:
            print()
            j =  0

j = 0
print("\n나는 팔로우 안하지만 상대가 하는 경우  : ")
for  i in follower:
    if i not in following:
        print("%25s" %(i), end = " | ")
        j += 1
        if j == 4:
            print()
            j =  0
