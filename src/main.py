"""
Product Return Validator - Main Module

This module handles user input collection and delegates validation logic to return_validator.validate_return()

Module Structure:
- main.py: Collects user input and calls return_validator.validate_return()
- return_validator.py: Contains validate_return() function with validation logic

Purchase Records (defined in return_validator.py):
- Alex    : Wireless Mouse, $25.99
- Sarah   : Laptop Stand, $45.50
- Michael : USB-C Cable, $12.00

Return Policy: Products can be returned within 7 days of purchase
Date Format: mm/dd/yy
"""


def validate_product_return():
    """
    Function that collects user input and calls return_validator.validate_return()
    
    TODO: Print introduction message
    Format: "Please enter the details to return the product."
    
    TODO: Get customer name from user input
    Prompt: "Enter your name:"
    Store in variable: customer_name
    
    TODO: Get product name from user input
    Prompt: "Enter the product name:"
    Store in variable: product_name
    
    TODO: Get purchase date from user input
    Print: "When did you purchase the product?"
    Prompt: "Please enter the date in mm/dd/yy format:"
    Store in variable: purchase_date
    
    TODO: Import return_validator and call validate_return() function
    Import: from return_validator import validate_return
    Call: validate_return(customer_name, product_name, purchase_date)
    
    Note: All validation logic, purchase record checks, date calculations, and output messages
          are handled by return_validator.validate_return() function
    """
    pass


def main():
    """
    Entry point for the application when run as a script.
    """
    validate_product_return()


if __name__ == "__main__":
    main()
