def main():
    balance = 800
    paycheck = 2000

    print(f"balance plus paycheck equals: {balance + paycheck}") #2800
    print(f"balance minus paycheck equals: {balance - paycheck}") #-1200
    print(f"balance times paycheck equals: {balance * paycheck}") #1600000
    print(f"balance divided by paycheck equals: {balance / paycheck}") #0.4
    print(f"balance integer divided by paycheck equals: {balance // paycheck}") #0
    print(f"balance modulus paycheck equals: {balance % paycheck}") #0
    print() 
    print(f"balance is equal to paycheck: {balance == paycheck}") #False
    print(f"balance is not equal to paycheck: {balance != paycheck}") #True
    print(f"balance is greater than paycheck: {balance > paycheck}") #False
    print(f"balance is less than paycheck: {balance < paycheck}") #True
    print(f"balance is greater than or equal to paycheck: {balance >= paycheck}") #False
    print(f"balance is less than or equal to paycheck: {balance <= paycheck}") #True
    print()
    balance += paycheck
    print(f"balance plus equals paycheck equals: {balance}") #2800
    balance -= paycheck
    print(f"balance minus equals paycheck equals: {balance}") #1200
    balance *= paycheck
    print(f"balance multiply equals paycheck equals: {balance}") #1600800
    balance /= paycheck
    print(f"balance divides equals paycheck equals: {balance}") #800.4
    balance //= paycheck
    print(f"balance integer divides equals paycheck equals: {balance}") #800
    balance %= paycheck 
    print(f"balance modulus divides equals paycheck equals: {balance}") #1200

    

    

 


if __name__ == "__main__":
    main()