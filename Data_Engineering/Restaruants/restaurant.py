class Table:
    def __init__(self):

        self.order_dict = []

    def order(self, item, price, quantity):
        self.item = item
        self.price = price
        self.quantity = quantity

        order = {"name": self.item, "quantity": self.quantity, "price": self.price}
        self.order_dict.append(order)


    def remove(self, item, quantity):


        for item in self.order_dict:
            if item["name"] == item:
                #if item["quantity"] <= quantity:
                    #del(self.order[])
                item["quantity"] -= quantity






    #def get_subtotal():


    #def get_total():


    #def split_bill():

mytable = Table()
mytable.order('fish', 1, 5)

mytable.remove('fish', 1)

print(mytable.order_dict)
