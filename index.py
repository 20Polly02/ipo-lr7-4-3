import json #Импортируем библиотеку json
with open("car.json", 'r', encoding='utf-8') as file:
    car_file = json.load(file)
count = 0
f=True
def menu():# Выводим текстовое меню для выбора действия.
    print("""
       1: Вывести все записи 
       2: Вывести запись по полю 
       3: Добавить запись 
       4: Удалить запись по полю 
       5: Выйти из программы
    """)

def all_car():#выводим список всех машин
       global count
        for car in car_file:  
            print(f"""
            Номер записи: {car['id']}, 
            Название модели: {car['name']},                       
            Название производителя: {car['manufacturer']}, 
            Заправляется ли бензином:{car['is_petrol']},    
            Объем бака: {car['tank_volume']} 
            """)
        count+=1
  
def car():#выводим машину по введенному номеру пользователем
        global count 
        id = int(input("Введите номер машины: "))  
        find = False  
        for car in car_file: 
            if id == car['id']:  
                print(f"""
            Номер записи: {car['id']}, 
            Название модели: {car['name']},                       
            Название производителя: {car['manufacturer']}, 
            Заправляется ли бензином:{car['is_petrol']},    
            Объем бака: {car['tank_volume']} 
            """)
                find = True   
                break 
          
        if not find:  
            print("Запись не найдена.")
        count+=1   
        
def add_car(): #добавление новой машины
        global count
        id = len(car_file) + 1      
        name = input("Введите название модели машины: ")  
        manufacturer = input("Введите назване производителя: ")  
        is_petrol = input("Введите, заправляется ли машина бензином (да/нет): ")  
        tank_volume = int(input("Введите обьем бака(целое число): "))
        new_car = {
                'id': id,
                'name': name,
                'manufacturer':manufacturer ,
                'is_petrol': True if is_petrol.lower() == 'да' else False, 
                'tank_volume': tank_volume
            }
        car_file.append(new_car) 
        with open("car.json", 'w', encoding='utf-8') as out_file: 
            json.dump(car_file, out_file)  
        print("Запись успешно добавлена.")
        count+=1
       
def delete_car():#удаляем машину
        global count
        id = int(input("Введите номер машины: "))  
        find = False   
        for car in car_file:  
            if id == car['id']: 
                car_file.remove(car)  
                find = True 
                break 
        if not find:  
            print("Запись не найдена.")
        else:  
            with open("car.json", 'w', encoding='utf-8') as out_file:
                json.dump(car_file, out_file)  
            print("Запись успешно удалена.")
        count+=1
            
def exit():#выход из программы
        global f
        print(f"""Программа завершена.""") 
        f=False 
    
def main(): # Функция main вызывающая все остальные функции

    with open("car.json", 'r', encoding='utf-8') as file: 
        car_file = json.load(file) 
    while f:
        menu()
        
        num = int(input("Введите номер действия: "))
        if num >= 1 and num <= 5:
           
            if num == 1:
                all_car()
               
            elif num == 2:
                car()
                
            elif num == 3:
                add_car()
                
            elif num == 4:
                delete_car()
                
            elif num == 5:
                exit()
                print("Количество операций:",count)
                break
            else:
                print("Такого номера нет.")

            with open("car.json", 'w', encoding='utf-8') as out_file: 
                json.dump(car_file, out_file, ensure_ascii = False, indent = 2)

if __name__ == "__main__":
    main()



