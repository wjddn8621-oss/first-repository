import random

class Account:
    bank_name = "SC은행"
    account_count = 0
    interest_rate = 0.01 

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.account_number = self.generate_account_number()
        self.deposit_count = 0
        self.deposit_history = []
        self.withdraw_history = []
        Account.account_count += 1

    def generate_account_number(self):
        num1 = str(random.randint(0, 999))
        num2 = str(random.randint(0, 99))
        num3 = str(random.randint(0, 999999))
        return f"{num1}-{num2}-{num3}"

    def deposit(self, amount):
        if amount <= 0:
            print("입금 금액은 0원보다 커야 합니다.")
            return
        self.balance += amount
        self.deposit_count += 1
        self.deposit_history.append(amount)
        print(f"{amount:,}원이 입금되었습니다. 현재 잔액: {self.balance:,}원")

        if self.deposit_count % 5 == 0:
            interest = int(self.balance * Account.interest_rate)
            self.balance += interest
            print(f"입금 5회 달성 이자 {interest:,}원이 지급되었습니다. 현재 잔액: {self.balance:,}원")

    def withdraw(self, amount):
        if amount <= 0:
            print("출금 금액은 0원보다 커야 합니다.")
            return
        if amount > self.balance:
            print(f"잔액 부족. 잔액: {self.balance:,}원")
            return
        self.balance -= amount
        self.withdraw_history.append(amount)
        print(f"{amount:,}원이 출금되었습니다. 현재 잔액: {self.balance:,}원")

    def show_deposit_history(self):
        print(f"\n[{self.owner}] 입금 내역:")
        if not self.deposit_history:
            print("입금 내역이 없습니다.")
        else:
            for i, amt in enumerate(self.deposit_history, 1):
                print(f"{i}. {amt:,}원")

    def show_withdraw_history(self):
        print(f"\n[{self.owner}] 출금 내역:")
        if not self.withdraw_history:
            print("출금 내역이 없습니다.")
        else:
            for i, amt in enumerate(self.withdraw_history, 1):
                print(f"{i}. {amt:,}원")

    def display_info(self):
        print(f"\n은행이름: {Account.bank_name}")
        print(f"예금주: {self.owner}")
        print(f"계좌번호: {self.account_number}")
        print(f"잔액: {self.balance:,}원")
        print(f"입금 횟수: {self.deposit_count}회")

    def get_account_num():
        print(f'현재 총 계좌 {Account.account_count}개')

acc1 = Account("홍길동", 1000000)
acc2 = Account("김철수", 20000)

account_list = [acc1, acc2]

def show_vip_accounts(accounts):
    print("\n잔고 1,000,000원 이상 고객 목록 ")
    vip_list = [acc for acc in accounts if acc.balance >= 1_000_000]
    if not vip_list:
        print("해당 조건을 만족하는 고객이 없습니다.")
    else:
        for acc in vip_list:
            acc.display_info()

    
print(f"총 {len(account_list)}개의 계좌가 생성되었습니다.\n")

for acc in account_list:
    acc.display_info()


acc = Account("홍길동", 1000000)

acc.deposit(5000)
acc.deposit(2000)
acc.withdraw(3000)
acc.deposit(1000)
acc.withdraw(2000)
acc.deposit(5000) 
acc.deposit(5000) 

acc.display_info()


acc.show_deposit_history()
acc.show_withdraw_history()
