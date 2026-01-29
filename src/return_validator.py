from datetime import datetime

def validate_return(customer_name, product_name, purchase_date):
    # Predefined purchase records (CASE-SENSITIVE)
    records = {
        ("Alex", "Wireless Mouse"): "$25.99",
        ("Sarah", "Laptop Stand"): "$45.50",
        ("Michael", "USB-C Cable"): "$12.00"
    }

    key = (customer_name, product_name)

    # ❌ Customer-product not found
    if key not in records:
        print("You have not purchased that product recently with us.")
        print("Thank you.")
        return

    # Parse purchase date
    try:
        purchase_dt = datetime.strptime(purchase_date, "%m/%d/%y").date()
    except ValueError:
        print("You have not purchased that product recently with us.")
        print("Thank you.")
        return

    # Current system date (mocked in tests)
    current_date = datetime.now().date()

    days_diff = (current_date - purchase_dt).days

    # ✅ Within 7 days
    if days_diff <= 7:
        price = records[key]
        print(
            f"Product:{product_name} will be collected from the delivered address "
            f"and amount:{price} will be returned to your account."
        )
    else:
        print("Sorry! the product cannot be returned")

    print("Thank you.")
