class ThaiEvCar:
    #class attribute
    my_ThaiEvCar = []

    def __init__(self,carid,model,brand,accelerationrate,hp,range,price):
        self.carid = carid
        self.model = model
        self.brand = brand
        self.accelertionrate = accelerationrate
        self.hp = hp
        self.range = range
        self.price = price



    def ThaiEvCar_detail(self):
        print(f'carid:{self.carid} '
        f'model:{self.model} '
        f'brand:{self.brand} '
        f'accelertionrate:{self.accelertionrate} '
        f'hp:{self.hp}'
        f'range:{self.range}'
        f'price:{self.price}')

    def delete_ThaiEvCar(self,index):
            self.my_ThaiEvCar.pop(index)

    def edit_ThaiEvCar_price(self,index, new_price):
            self.my_ThaiEvCar[index].price = new_price



