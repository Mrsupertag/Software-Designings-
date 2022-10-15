number = [2 , 3 , 9 , 7, 12 , 91 , 102 , 150, 210 , 9 ]
winner_list = ["Saadiq" , "Doctor" , "Aria" , "Addison" , "Tawfique" , "Mrs Smith" , "Saman" , "Abrar" , "Mrs Akter" , "Mr Chowdhury"]

chance = number.count(9)
print("The winner number may be "+str(chance))


winner = winner_list.max()
print("The Winner is " +(winner))
winner_number = number.max()
print("Their number is "+(winner_number))