store = { 
    '1':('Magi',20),
    '2':('Butter',150),
    '3':('Bread',50),
    '4':('Egg',10),
    '5':('Coffee','150'),
    '6':('Beer',200)
}

item_list = {}

def view_store(): 
    print('\nThis is the available store')
    for item_id,(item_name,item_pirce) in store.items():
        print(f'{item_id} - {item_name} - {item_pirce}')

def purchase_item():
    id = input('Enter item id: ')
    qnty = int(input('Enter the quantity: '))

    if id in store:
        name,price = store[id]
        item_list[id] = [name,price,qnty]

def view_purchased_items():
    print('\nPurchased list is :')
    print('id - name - price - qnty')
    for x in (item_list):
       print(x)

def update_purchased_item():
    id = input('Enter the id of the item in the cart to be modified :')
    qnty = int(input('Enter the new quantity to be modified :'))

    cnt = 0
    for x in item_list:
        if x[0] == id :
            item_list[cnt][3] = qnty
        cnt += 1

def delete_purchased_item():
    id = input('Enter the id of the item to be deleted: ')
    
    cnt=0
    for x in item_list:
        if x[0] == id:
            del item_list[cnt]
        cnt += 1

def gen_invoice():
    total = 0
    for x in range(len(item_list)):
        item_list[x].append(item_list[x][2] * item_list[x][3])
        total += (item_list[x][2] * item_list[x][3])

    print(item_list,' ',total)

    with open('invoice.txt','w') as file:
        file.write("***** Invoice Copy *******\n")

        cnt=0
        for x in range(len(item_list)):
            file.write(f'{item_list[cnt][0]} - {item_list[cnt][1]} - {item_list[cnt][2]} - {item_list[cnt][3]} - {item_list[cnt][4]} \n') 
            cnt += 1
        
        file.write("***************************\n")
        file.write(f"\nTotal: ${total}\n")
        file.write("***************************\n")
        print("Invoice saved to invoice.txt")   



while True:
    print('\nMenu')
    print('1.View the store')
    print('2.Purchase the item')
    print('3.Update the purchased item')
    print('4.Remove the  purchased item')
    print('5.View the purchased items')
    print('6.Generate the invoice')
    print('7.Exit')

    choice = input('Enetr the choice 1-6: ')
    if choice == '1':
        view_store()
    elif choice == '2':
        purchase_item()
    elif choice == '3':
        update_purchased_item()
    elif choice == '4':
        delete_purchased_item()
    elif choice == '5':
        view_purchased_items()
    elif choice == '6':
        gen_invoice()
    elif choice == '7':
        break
    else:
        print('Wrong entry!')
        
