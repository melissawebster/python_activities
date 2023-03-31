import pytest

def discount(unitary_price,quantity):
    # unitary_price = float(input('Unitary price of the product: '))
    # quantity = int(input('How many units are you taking? '))
    discount = 1

    if quantity >= 10 and quantity <= 99:
        discount = 0.95
    elif quantity >= 100 and quantity <= 999:
        discount = 0.90
    elif quantity >= 1000:
        discount = 0.85

    price_without_discount = unitary_price * quantity
    price_with_discount = unitary_price * discount * quantity
    
    print(f'Total price (no discount applied): {price_without_discount:.2f} R$')
    print(f'Total price (with discount): {price_with_discount:.2f} R$')

    return price_without_discount, price_with_discount


def test_discount():
    assert discount(50, 100) == (5000.00, 4500.00)