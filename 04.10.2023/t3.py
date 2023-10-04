import random 
secret_number = random.randint(1,99)
while True:
    s1 = input("Я загадав цифру від 1 до 99, твоя задача вгадає моє число:")
    s1 = int(s1)
    if s1 == secret_number:
        print("Молодець ти виграв!")
        break
    elif s1 > secret_number:
        print("Моє число менше, пробуй ще раз!")
    elif s1 < secret_number:
        print("Моє число більше, пробуй ще раз!")
    print(type(s1))