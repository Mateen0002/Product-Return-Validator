from return_validator import validate_return

def validate_product_return():
    print("Please enter the details to return the product.")

    name = input("Enter your name:")
    product = input("Enter the product name:")

    print("When did you purchase the product?")
    date = input("Please enter the date in mm/dd/yy format:")

    validate_return(name, product, date)


if __name__ == "__main__":
    validate_product_return()
