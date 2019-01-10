class product:
    def __init__(self,price,idd,quant):
        self.price=price
        self.idd=idd
        self.quantity=quant
class inventory:
    item={}
    quant={}
    def __init__(self):
        self.item={}
        self.quant={}
    def add_product(self,product):
    	if product.idd in self.item.keys():#if already product exsists and more quantity of same added
    		self.quant[product.idd]=self.quant[product.idd]+product.quantity
    	else:
        	self.item[product.idd]=product.price
        	self.quant[product.idd]=product.quantity
    def calculate(self):#caluclatimng the total cost of all the products
        sum=0;
        for i in self.item:
            sum=sum+self.item[i]*self.quant[i]
            #print(sum)
        return sum
n=int(input("enter the number of products"))
a1=inventory()
for i in range(n):
	price=int(input("enter the price"))
	pid=int(input("enter the id"))
	quant=int(input("enter the quantity_on_hand"))
	a1.add_product(product(price,pid,quant))
print(a1.calculate())