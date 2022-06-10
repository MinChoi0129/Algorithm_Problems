import os

class InstagramChecker:

    def __init__(self):
        self.name = self.getUserName()
        self.followers = [user[:-10] for user in open("InstagramChecker/follower.txt", mode = "r",  encoding="utf-8") if "님의 프로필 사진" in user]
        self.followings = [user[:-10] for user in open("InstagramChecker/following.txt", mode = "r",  encoding="utf-8") if "님의 프로필 사진" in user]
    
    def cclear(): os.system("cls")
    
    def getUserName(self):
        isAllDataReady = False
        while not isAllDataReady:
            try:
                InstagramChecker.cclear()
                answer = input("모든 파일을 올바르게 준비하였습니까? (Y / N) > ").upper()
                if answer == "Y": isAllDataReady = True;
                elif answer == "N": InstagramChecker.cclear(); print("모든 파일을 준비한 후 다시 시작해주세요."); break
            except: continue
            
        if not isAllDataReady: return ""

        isNameOk, userName = False, ""
        while not isNameOk:
            InstagramChecker.cclear()
            userName = input("이름을 입력해주세요 > ")
            while userName:
                try:
                    InstagramChecker.cclear()
                    isUserNameSatisfied = input("[" + userName + "]" + "님이 맞습니까? (Y / N) > ").upper()
                    if isUserNameSatisfied == "Y": isNameOk = True; break
                    elif isUserNameSatisfied == "N": InstagramChecker.cclear(); break
                except: continue
        
            InstagramChecker.cclear()
        return userName

    def followEachOtherPrinter(self, one, other):
        printCounter = 0
        for person in one:
            if person not in other:
                print("%30s" % person.strip(), end = " | ")
                printCounter += 1
                if printCounter == 5: printCounter = 0; print()
        print(); print()

    def showInstagramUserInfo(self):
        numberOfFollowers, numberOfFollowings = len(self.followers), len(self.followings)
        
        print("[%s]님의 Instagram 정보입니다." % self.name, end = "\n\n")
        
        print("팔로워 : %d명, 팔로잉: %d명" % (numberOfFollowers, numberOfFollowings), end = "\n\n")
        
        print("팔로워는 팔로잉의 %.2f%% 입니다." % (100 * numberOfFollowers / numberOfFollowings), end = "\n\n")

        print("[%s]님께서 팔로우 하지만 상대방은 팔로우하지 않는 케이스입니다." % self.name)
        self.followEachOtherPrinter(self.followings, self.followers)

        print("[%s]님을 팔로우 하지만 [%s]님께선 팔로우하지 않는 케이스입니다." % (self.name, self.name))
        self.followEachOtherPrinter(self.followers, self.followings)

user = InstagramChecker()
if user.name: user.showInstagramUserInfo()