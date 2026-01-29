from datetime import datetime

PURCHASE_RECORDS = {
    ("Alex", "Wireless Mouse"): "$25.99",
    ("Sarah", "Laptop Stand"): "$45.50",
    ("Michael", "USB-C Cable"): "$12.00"
}

def validate_return(customer_name, product_name, purchase_date):
    key = (customer_name, product_name)

    #  Customer + Product not found
    if key not in PURCHASE_RECORDS:
        print("You have not purchased that product recently with us.")
        print("Thank you.")
        return

    # Parse date ONLY after validation
    purchase_dt = datetime.strptime(purchase_date, "%m/%d/%y")
    today = datetime.now().date()

    days_diff = (today - purchase_dt.date()).days

    # Exceeds 7 days
    if days_diff > 7:
        print("Sorry! the product cannot be returned")
        print("Thank you.")
        return

    #  Valid return
    price = PURCHASE_RECORDS[key]
    print(
        f"Product:{product_name} will be collected from the delivered address "
        f"and amount:{price} will be returned to your account."
    )
    print("Thank you.")
