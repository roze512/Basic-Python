id_num = 1

while id_num <= 20:
    if id_num % 2 == 0:
        print(f"ID {id_num}: Process Batch A")
    else:
        print(f"ID {id_num}: Process Batch B")
    id_num += 1
