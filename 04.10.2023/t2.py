s1 = input("Для переводу з цельсія на фарангейти введіь цифру 1 , для переводу з фарангейту на цельсія цифру 2 ")
s1 = int(s1)
if s1 == 1:
   c1 = input("Введіть скільки цельсій перевести на фарангейти:")
   c1 = int(c1)
   print(c1 * 9 / 5 + 32)
elif s1 == 2:
    c2 = input("Введіть скільки фарангейтів перевести на цельсія:") 
    c2 = int(c2)
    print((c2 - 32) * 5 / 9)
    
    
    