from EvCar import ThaiEvCar

def display_option():
    print("welcome to ThaiEvCar Data Store System (VDSS)")
    print("1.Add_ev_car")
    print("2.Delete_ev_car")
    print("3.update_ev_carPrice")
    print("4.ev_car_detail")
    select = int(input("select(1-4)? : "))
    if select == 1:
        input_ThaiEvCar_data()
    elif select==2:
        delete_ThaiEvCar()
    elif select ==3:
        edit_ThaiEvCar_price()
    elif select ==5:
        display_ThaiEvCar()
    else:
        print("Please, select number 1-6.")

def input_ThaiEvCar_data():
    carid  = input("Enter ThaiEvCar carid ")
    model = input("Enter ThaiEvCar model ")
    brand  = input("Enter ThaiEvCar brand ")
    acelerationrate  = input("Enter ThaiEvCar acelerationrate ")
    HP = input("Enter ThaiEvCar HP ")
    range  = int(input("Enter ThaiEvCar range:"))
    price = float(input("Enter ThaiEvCar price: "))

    ThaiEvCar.my_thaiEvCar.append(ThaiEvCar(carid,model,brand,acelerationrate,HP,range,price))
    print("\n---------------------------------")
    print("Already add ThaiEvCar to stor.")
    print("\n---------------------------------")

def display_ThaiEvCar():
    if len(ThaiEvCar.my_thaiEvCar) ==0:
        print("You had no ThaiEvCar data.")
    else:
        print(f'You had{len(ThaiEvCar.my_thaiEvCar)} following:')
        n = 1
        for x in ThaiEvCar.my_thaiEvCar:
            print(f'[{n}]:',end=" ")
            x.ThaiEvCar_detail()
            n = n+1
        print("\n")

def delete_ThaiEvCar():
    display_ThaiEvCar()
    if len(ThaiEvCar.my_thaiEvCar) !=0:
        print("You had no data to delete.")
        s = int(input("Select to delete?: "))

        ThaiEvCar.delete_ThaiEvCar(ThaiEvCar,s - 1)
        print("\n---------------------------------")
        print("Your data has been deleted.")
        print("---------------------------------\n")

def edit_ThaiEvCar_price():
    display_ThaiEvCar()
    if len(ThaiEvCar.my_thaiEvCar) !=0:
        s = int(input("Select to edit?: "))
        print(f'/nprevious price: {ThaiEvCar.my_thaiEvCar,[s-1].price}')
        new_price  = float(input("new price: "))
        ThaiEvCar.edit_ThaiEvCar_price(ThaiEvCar,s-1,new_price)
        print("\n---------------------------------")
        print("Your data has been deleted.")
        print("---------------------------------\n")

s = 0
while s == 0:
    display_option()

