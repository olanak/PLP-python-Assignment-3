def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying discount.
    If discount_percent is less than 20%, return original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price

# prompt user for price and discount percent
try:
    price = float(input("Enter the original price:  "))
    discount_percent = float(input("Enter the discount percent:  "))

    final_price = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f"Final price after {discount_percent}% discount: {final_price:.2f}")
    else:
        print(f"No discount applied. Final price: {final_price:.2f}")

except ValueError:
    print("Invalid input! Please enter numeric values.")