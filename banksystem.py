# Parent Class
class Transaction:
    def __init__(self):
        self.bank_name = "Student Union Bank"

    # This method will be overridden by the child classes
    def execute(self, amount):
        print(f"Processing a generic transaction of ${amount}")


# Child Class 1
class Deposit(Transaction):
    # Method Overriding: Changes what execute() does for deposits
    # Method Overloading: Uses default arguments (bonus=0) to accept 1 or 2 inputs
    def execute(self, amount, bonus=0):
        total = amount + bonus
        if bonus > 0:
            print(f"[DEPOSIT] Employer deposited basic salary: ${amount} + Holiday Bonus: ${bonus}. Total: ${total}")
        else:
            print(f"[DEPOSIT] Employer deposited salary: ${amount}")


# Child Class 2
class Withdrawal(Transaction):
    # Method Overriding
    # Method Overloading: Uses a default fee argument to handle different withdrawal types
    def execute(self, amount, fee=0):
        total_deducted = amount + fee
        if fee > 0:
            print(f"[WITHDRAWAL] Employer withdrew: ${amount} (ATM Fee: ${fee}). Total deducted: ${total_deducted}")
        else:
            print(f"[WITHDRAWAL] Employer withdrew: ${amount} (No fee charged)")


# Child Class 3
class Transfer(Transaction):
    # Method Overriding
    # Method Overloading: Uses a default recipient to simulate two ways to transfer
    def execute(self, amount, recipient="Company Main Account"):
        print(f"[TRANSFER] Employer transferred ${amount} to {recipient}")


# MAIN PROGRAM
if __name__ == "__main__":
    print("--- WELCOME TO THE EMPLOYER BANKING SYSTEM ---")
    
    # Instantiate child objects
    emp_deposit = Deposit()
    emp_withdrawal = Withdrawal()
    emp_transfer = Transfer()

    # 1. Demonstrate Overriding & Overloading for DEPOSIT
    # Call with 1 argument (Basic deposit)
    emp_deposit.execute(5000) 
    # Call with 2 arguments (Overloaded behavior with a bonus)
    emp_deposit.execute(5000, 500) 

    print("-" * 50)

    # 2. Demonstrate Overriding & Overloading for WITHDRAWAL
    # Call with 1 argument (Standard withdrawal)
    emp_withdrawal.execute(1000)
    # Call with 2 arguments (Overloaded behavior with an ATM fee)
    emp_withdrawal.execute(1000, 5)

    print("-" * 50)

    # 3. Demonstrate Overriding & Overloading for TRANSFER
    # Call with 1 argument (Default transfer recipient)
    emp_transfer.execute(15000)
    # Call with 2 arguments (Overloaded behavior specifying a custom recipient)
    emp_transfer.execute(2500, "John Bosco (Employee #41)")
