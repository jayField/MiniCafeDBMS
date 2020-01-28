import numpy as np
import pandas as pd
import time

####### 카페 주인 class #########
class CafeOwner:

    # 메뉴 값 초기화
    def __init__(self):
        self.menu = pd.read_excel('./menu.xlsx')

    # 인사하는 method
    def greet(self):
        print("어서오세요*^^*")

    # 메뉴를 화면에 보여주는 method
    def displayMenu(self):
        #print(self.menu[["name"]]) 인덱스 포함 print
        print("*******메뉴판********")
        print("*******************")
        print(self.menu.to_string(index=False)) # 인덱스 제외 print
        print("*******************")
        # df.to_string(index=False)

    # 주문 받는 method
    def order(self):
        print("주문하시겠습니까?")
        print("위에 있는 메뉴를 골라주세요")

    # 멤버쉽 유무 질의 method
    def inquireMembership(self):
        print("멤버쉽이 있으십니까? (YES or NO)")

    # 주문한 음료를 점검하는 method
    def checkOrder(self):
        while(1):
            self.order()
            cus = Customer()
            cus_menu = cus.chooseMenu()
            cnt = 0
            count = 0

            for i in self.menu["name"]:
                cnt+=1
                if(i == cus_menu):
                    print("주문하신 메뉴가 있습니다")
                    print("주문되셨습니다.")
                    count+=1
                    break

            if(count == 1):
                return cus_menu

            if(self.menu.shape[0] == cnt):
                print("해당 메뉴는 없습니다.")
                print("다시 주문해주세요.")
                continue

    # 마지막 멘트 method
    def order_fin(self):
        print("주문이 완료되었습니다.")
        print("잠시만 기다려주세요")
        time.sleep(5)
        print()
        print("주문하신 음료 나왔습니다. 맛있게 드세요*^^*")

    # 계산 안내 method
    def help_cal(self):
        print("계산 도와드리겠습니다.")

    # 멤버쉽 조회 method
    def askMembership(self):
        print("조회 해드리겠습니다. 이름을 입력해주세요")

# 카페 데이터 베이스를 관리하는 클래스
class CafeDB:

    def __init__(self,name):
        self.name = name
        self.level = ""
        self.visit_num = 0

    # 멤버쉽 등록이 되어 있지 않아서 등록을 도와주는 method
    # register_membership
    def add_membership(self):
        self.level = "SILVER"
        self.visit_num = 1

        membership_excel = pd.read_excel("./cafeDB.xlsx")
        raw_data = [[self.name, self.level, self.visit_num]]

        df_raw_data = pd.DataFrame(raw_data,columns=['name', 'level', 'visit_num'])
        df_new = pd.concat([membership_excel, df_raw_data], sort=False, ignore_index=True)
        df_new = df_new.loc[:, ~df_new.columns.str.contains('^Unnamed')]
        df_new.to_excel('./cafeDB.xlsx')

    # 멤버쉽 등록된 사람을 조회하는 method
    def chkd_membership(self):
        membership_excel = pd.read_excel("./cafeDB.xlsx")
        cnt = -1
        count = 0
        for i in membership_excel["name"]:
            cnt+=1
            if(name == i):
                count = cnt

        #train.at[count, "visit_num"] += 1
        membership_excel.at[count,"visit_num"] +=1
        membership_excel = membership_excel.loc[:, ~membership_excel.columns.str.contains('^Unnamed')]
        membership_excel.to_excel('./cafeDB.xlsx')

    # 멤버쉽도 없고 등록도 안하는 경우
    def add_noneCust(self):
        self.name = "None"
        self.level = "None"
        self.visit_num = 1

        membership_excel = pd.read_excel("./cafeDB.xlsx")
        raw_data = [[self.name, self.level, self.visit_num]]

        df_raw_data = pd.DataFrame(raw_data,columns=['name', 'level', 'visit_num'])
        df_new = pd.concat([membership_excel, df_raw_data], sort=False,ignore_index=True)
        df_new = df_new.loc[:, ~df_new.columns.str.contains('^Unnamed')]
        df_new.to_excel('./cafeDB.xlsx')

# 멤버쉽 등록하는 클래스
class Membership(CafeDB):

    def __init__(self,name):
        self.name = name
        self.level = ""
        self.visit_num = 0

    # 멤버쉽에 가입했나 확인하는 메소드
    #  return 값으로 구분해서 알고리즘 진행
    def checkMembership(self):

        membership_data = pd.read_excel('./membership.xlsx')
        cnt = 0

        for i in membership_data["name"]:
            #name_list.append(i)
            #print("i값 ", i)
            cnt+=1
            if(self.name == i):
                print("저희 고객님이 맞습니다")
                return 1

            if(cnt == membership_data.shape[0]):
                print("죄송합니다 저희 고객님이 아닙니다.")
                return 0


    # 멤버쉽 등록을 도와주는 메소드 (이름, 등급, 방문횟수 등록)
    def add_membership(self):
        self.level = "SILVER"
        self.visit_num = 1

        membership_excel = pd.read_excel("./membership.xlsx")
        raw_data = [[self.name, self.level, self.visit_num]]

        df_raw_data = pd.DataFrame(raw_data,columns=['name', 'level', 'visit_num'])
        df_new = pd.concat([membership_excel, df_raw_data], sort=False,ignore_index=True)
        df_new = df_new.loc[:, ~df_new.columns.str.contains('^Unnamed')]
        df_new.to_excel('./membership.xlsx')

        # 엑셀 실행문
        #new_membership_excel = pd.read_excel('./membership.xlsx')
        #new_membership_excel = new_membership_excel[new_membership_excel.filter(regex='^(?!Unnamed)').columns]
        #print(new_membership_excel) # for debugging

    # 이미 멤버쉽 가입이 된 사람들의 방문횟수를 추가하는 method
    def chkd_membership(self,name): # para : "[이름,레벨,방문횟수]"
        membership_excel = pd.read_excel("./membership.xlsx")
        cnt = -1
        count = 0
        for i in membership_excel["name"]:
            cnt+=1
            if(name == i):
                count = cnt

        #train.at[count, "visit_num"] += 1
        membership_excel.at[count,"visit_num"] +=1
        membership_excel = membership_excel.loc[:, ~membership_excel.columns.str.contains('^Unnamed')]
        membership_excel.to_excel('./membership.xlsx')

        #new_membership_excel = pd.read_excel('./membership.xlsx')
        #new_membership_excel = new_membership_excel[new_membership_excel.filter(regex='^(?!Unnamed)').columns]
        #print(new_membership_excel) # for debugging

# 손님 답변 클래스
class Customer:
    def __init__(self):
        pass

    def cust_YesOrNo(self):
        ans = input("손님: ")
        return ans

    def chooseMenu(self):
        ans = input("손님: ")
        return ans

    def tellName(self):
        ans = input("손님: ")
        return ans

    def sendMoney(self):
        ans = int(input("손님: "))
        return ans



if __name__ == '__main__':

    owner = CafeOwner() # 카페 주인 객체
    cus = Customer() # 손님 객체

    menu = ""
    ans = ""

    # 손님이 들어옴 인사하기
    owner.greet()

    #메뉴 화면에 띄우기
    #손님이 입장했습니다
    owner.displayMenu()

    #ord_menu : 손님이 주문한 메뉴
    #메뉴를 골라주세요
    #ord_menu = owner.order()
    #menu = cus.chooseMenu()

    #정회님 ver
    #손님이 메뉴 주문함

    cust_menu = owner.checkOrder()

    """
    while 1 :
    #메뉴를 골라주세요
        ord_menu = owner.order()
        menu = cus.chooseMenu()
        cnt = 0
        count = 0
        for i in owner.menu["name"]:

            cnt = 0

            cnt +=1
            if(i == menu):
                print("주문되셨습니다")
                count+=1
                break
        if(count == 1):
            break

        if(cnt == owner.menu.shape[0]):
            print("없는 메뉴입니다.")
            continue
    """

    #손님 멤버쉽 유무 확인
    owner.inquireMembership()
    ans = cus.cust_YesOrNo()

    # 멤버쉽 등록 되어 있는 경우, 멤버쉽 확인
    if(ans == "YES"):
        # 멤버쉽 체크

        owner.askMembership()
        name = cus.tellName()

        # 멤버쉽으로 멤버쉽 체크
        member = Membership(name)
        chked_member = member.checkMembership()

        # 멤버쉽이 등록되었다고 말했고 멤버쉽이 등록되어 있는 경우
        if chked_member == 1 :
            #YES 등록됨 visit_num +=1
            member.chkd_membership(name)
            db = CafeDB(name)
            db.chkd_membership()

        # 멤버쉽이 등록되었다고 말했는데 등록이 되어있지 않은 경우
        else :
            print("그러면 멤버쉽 등록을 하시겠습니까? YES or NO")
            ans = cus.cust_YesOrNo()

            # membership 클래스 호출
            # 등록 가능
            if (ans == "YES"):
                print("등록을 진행해드리겠습니다. 성함을 입력해주세요")
                name = cus.tellName()
                member = Membership(name)

                # 20.1.9 excel test
                member.add_membership()

                db = CafeDB(name)
                db.add_membership()

            # 등록안하고 메뉴 제외 나머지 값 none으로 저장
            else:
                # 생성자 오버로딩 찾기
                db = CafeDB("None")
                db.add_noneCust()

        #NO 등록되어있지 않습니다

        ################## DB사용#######################


    # 멤버쉽 등록 안되어 있는 경우
    else :
        print("그러면 멤버쉽 등록을 하시겠습니까? YES or NO")
        ans = cus.cust_YesOrNo()

        # membership 클래스 호출
        # 등록 가능
        if(ans =="YES"):
            print("등록을 진행해드리겠습니다. 성함을 입력해주세요")
            name = cus.tellName()
            member = Membership(name)

            # 20.1.9 excel test
            member.add_membership()

            db = CafeDB(name)
            db.add_membership()
            #print(Membership.member) 확인하는 법

            ################## DB사용#######################

        # 등록안하고 메뉴 제외 나머지 값 none으로 저장
        else :
            # 생성자 오버로딩 찾기
            db = CafeDB("None")
            db.add_noneCust()
            ################## DB사용#######################


    #계산 부탁드리겠습니다.
    owner.help_cal()


    x = 0

    while(1):
        cnt_money = 0
        for i in owner.menu["name"]:

            if i == cust_menu :
                break
            cnt_money += 1


        #membership_excel.at[count, "visit_num"]
        money = cus.sendMoney()
        if(owner.menu.at[cnt_money, "price"] == money):
            print("금액이 일치합니다.")
            break

        else :
            print("금액이 틀렸습니다. 다시 내주세요")
    # 주문이 완료되었습니다
    # 잠시만 기달려주세요
    owner.order_fin()



######메소드명 바꾸기, 상속, 생성자 오버로딩, #재료추가, 컬럼추가(커피내용), 멤버쉽있다고 뻥치는 사람 참교육 당하는중##############
###### 총액 구하기 ########
