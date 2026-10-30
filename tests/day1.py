# name = "小王"
# age = 20
# address = "黄土高坡"
# print(f"我的名字叫{name},芳龄{age},家住{address}上")

# salary = 9999
# if salary>=100000:
#     print("有钱赚")
# elif salary >=50000:
#     print("中富")
# elif salary >=10000:
#     print("小富")
# else :
#     print("穷鬼")

# work = [16,22,24,26,30]
# for works in work:
#      if works == 16:
#          print ("very good work")
#      elif works == 22:
#          print("good work")
#      elif works == 24:
#          print("SO-so work")
#      else:
#          print("bad work")

# goodwork = [works for works in work if works <24]
# print(goodwork)

def holiday(quantity):
    if quantity>=100:
        print("very good work")
    elif quantity>=50:
        print("good work")
    else:
        print("bad work")
holiday(10)

def check_user(user):
    check_name =["id","name","age"]
    for check_names in check_name:
        if  user.get(check_names) is None:
            return f"缺少字段{check_names}"
    return "未缺少"
user1 ={ "id":1,"name":"小王","age":18}
user2 = {"id":2,"name":"小李"}
print(check_user(user1))
print(check_user(user2))