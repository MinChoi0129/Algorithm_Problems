from datetime import datetime

# class Soldier:
#     def __init__(self, name, date):
#         self.name = name
#         self.date = date
    
#     def get_left_day(self):
#         return (self.date - datetime.now()).days + 546
    
#     def get_done_percent(self):
#         return (546 - self.get_left_day()) * 100 / 546

# me = Soldier("이민재", datetime(2021, 1, 11, 14, 0, 0))

# print(me.get_left_day())
# print(me.get_done_percent(), "%%")

print((datetime(2021, 2, 22, 17, 30, 0) - datetime(2021, 1, 11, 14, 0, 0)).days)