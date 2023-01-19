from q1 import priceCheck
import pytest

def testPriceCheck():
    products=['rice', 'sugar', 'wheat', 'cheese']
    productPrices=[16.89, 56.92, 20.89, 345.99]
    productSold=['rice', 'cheese']
    soldPrice=[18.99, 400.89]
    assert priceCheck(products, productPrices, productSold, soldPrice) == 2
def testPriceCheck2():
    products=['rice', 'sugar', 'wheat', 'cheese']
    productPrices=[16.89, 56.92, 20.89, 345.99]
    productSold=['rice', 'cheese','wheat','sugar']
    soldPrice=[18.99, 400.89,20.90,56.92]
    assert priceCheck(products, productPrices, productSold, soldPrice) == 3

