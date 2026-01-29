"""
Product Return Validator - Return Validator Module

This module contains the validate_return() function that validates return requests.

Function: validate_return(customer_name, product_name, purchase_date)
- Validates customer and product against purchase records
- Calculates days elapsed since purchase
- Determines eligibility based on 7-day return policy
- Displays appropriate success or error messages
"""


def validate_return(customer_name, product_name, purchase_date):
    """
    Validates product return request based on purchase records and return policy.
    
    Parameters:
    - customer_name (str): Name of the customer (case-sensitive)
    - product_name (str): Name of the product to return
    - purchase_date (str): Purchase date in mm/dd/yy format
    
    TODO: Create purchase records dictionary
    Structure:
    {
        'Alex': {'product': 'Wireless Mouse', 'price': '$25.99'},
        'Sarah': {'product': 'Laptop Stand', 'price': '$45.50'},
        'Michael': {'product': 'USB-C Cable', 'price': '$12.00'}
    }
    
    TODO: Validate customer name exists in purchase records (case-sensitive matching)
    Check: if customer_name not in purchase_records:
        Print: "You have not purchased that product recently with us."
        Print: "Thank you."
        Return from function
    
    TODO: Validate product name matches customer's purchased product
    Check: if purchase_records[customer_name]['product'] != product_name:
        Print: "You have not purchased that product recently with us."
        Print: "Thank you."
        Return from function
    
    TODO: Calculate days elapsed since purchase
    Steps:
    1. Import datetime module
    2. Get current system date: datetime.now().date()
    3. Parse purchase_date string using datetime.strptime(purchase_date, '%m/%d/%y')
    4. Extract date object from parsed datetime
    5. Calculate difference: (current_date - purchase_date).days
    
    TODO: Check return eligibility based on 7-day policy
    If days_elapsed <= 7:
        - Get product price: purchase_records[customer_name]['price']
        - Print success message:
          "Product:{product_name} will be collected from the delivered address and amount:{price} will be returned to your account."
        - Print: "Thank you."
    
    If days_elapsed > 7:
        - Print: "Sorry! the product cannot be returned"
        - Print: "Thank you."
    
    Validation Rules:
    - Customer name matching is case-sensitive
    - Both customer name AND product name must match purchase records
    - Date validation happens only after purchase record match confirmation
    """
    pass

