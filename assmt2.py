print("WELCOME TO THE E-COMMERCE PLATFORM")

# Pre-defined user credentials and access levels
admin_user = "admin123"
admin_pass = "adminpass"

customer_user = "john_bosco"
customer_pass = "custard"

cashier_user = "cashier1"
cashier_pass = "cashierpass"

# Ask user for login details
username_input = input("Enter Username: ")
password_input = input("Enter Password: ")

access_granted = False
user_role = ""

# Checking credentials using nested conditions
if username_input == admin_user:
    if password_input == admin_pass:
        print("\nLogin Successful! Welcome, Administrator.")
        print("Access Level: Full System Control (Manage Inventory, View Reports, Process Sales)")
        access_granted = True
        user_role = "Admin"
    else:
        print("Invalid: Incorrect password for Admin.")
elif username_input == customer_user:
    if password_input == customer_pass:
        print("\nLogin Successful! Welcome to your Shopping Dashboard.")
        print("Access Level: Customer (Browse Products, View Cart, Checkout)")
        access_granted = True
        user_role = "Customer"
    else:
        print("Invalid: Incorrect password for Customer.")
elif username_input == cashier_user:
    if password_input == cashier_pass:
        print("\nLogin Successful! Welcome, Cashier.")
        print("Access Level: Staff (Process Sales, Scan Items)")
        access_granted = True
        user_role = "Cashier"
    else:
        print("Invalid: Incorrect password for Cashier.")
else:
    print("Invalid: Username not found in the system.")

# E-commerce checkout calculation
if access_granted == True:
    print("\nSTARTING CHECKOUT PROCESS")
    
    subtotal = float(input("Enter the product subtotal amount ($): "))
    discount_rate = 0.0
    tax_rate = 0.0
    
    # Automatic discount levels based on Subtotal volume
    if subtotal >= 500:
        print("System Alert: High-value order! Applying 15% VIP automatic discount.")
        discount_rate = 0.15
    elif subtotal >= 100:
        print("System Alert: Applying standard 5% automatic discount.")
        discount_rate = 0.05
    else:
        print("System Alert: Subtotal under $100. No automatic discount applied.")
        discount_rate = 0.0
        
    # Coupon Code validation 
    has_coupon = input("Do you have a coupon code? (yes/no): ").lower()
    
    if has_coupon == "yes":
        coupon_code = input("Enter coupon code: ")
        
        if coupon_code == "SAVE20":
            print("Coupon 'SAVE20' valid! Adding an extra 20% discount.")
            discount_rate = discount_rate + 0.20
        elif coupon_code == "FREESHIP":
            print("Coupon 'FREESHIP' valid! Free shipping applied (No extra price discount).")
        else:
            print("Invalid coupon code! No extra discount added.")
            
    # Tax rates based on Location 
    location = input("Enter shipping location state/region (KLA, EBB, or OTHER): ").upper()
    
    if location == "KLA":
        tax_rate = 0.08  # 8% Tax for Kampala
        print("Location identified: KLA. Tax rate is 8%.")
    elif location == "EBB":
        tax_rate = 0.06  # 6% Tax for Entebbe
        print("Location identified: EBB. Tax rate is 6%.")
    else:
        tax_rate = 0.05  # 5% Default Tax for other places
        print("Location identified: Other region. Default tax rate is 5%.")

    # Final Calculations
    discount_amount = subtotal * discount_rate
    price_after_discount = subtotal - discount_amount
    tax_amount = price_after_discount * tax_rate
    final_price = price_after_discount + tax_amount

    # Print out the invoice summary
    print("\n")
    print("FINAL RECEIPT")
    print("")
    print("Processed By:", user_role)
    print("Original Subtotal: $", round(subtotal, 2))
    print("Total Discount Applied: - $", round(discount_amount, 2))
    print("Price After Discount: $", round(price_after_discount, 2))
    print("Tax Amount Charged: + $", round(tax_amount, 2))
    print("")
    print("FINAL TOTAL PRICE: $", round(final_price, 2))
    print("")

else:
    print("\nAccess Denied. You cannot process a calculation without logging in.")
