def priceCheck( products,productPrices, productSold, soldPrice):
    count = 0
    for index,ps in enumerate(productSold):
        indexOfProductsPrices = products.index(ps) 
        if  indexOfProductsPrices >=0:
            if(soldPrice[index] != productPrices[indexOfProductsPrices]):
                count+=1
    return count
    
