def calculate_discount(price, discount_percent):

    if discount_percent > 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = int(input("Enter the discount percentage: "))
    
    
    final_price = calculate_discount(price , discount_percent)
    
    
   
    print(f"\nOriginal price: {price:.2f}")
    print(f"Discount percentage: {discount_percent}%")
    
    if discount_percent >= 20:
        print(f"Discount applied: {price * (discount_percent / 100):.2f}")
        print(f"Final price after discount: {final_price:.2f}")
    else:
        print("No discount applied (discount must be 20% or higher)")
        print(f"Final price: ${final_price:.2f}")
        
except ValueError:
    print("Error: Please enter valid numbers for price and discount percentage.")
