col = []
positive_diagonal = []
for i in range(4):
    for j in range(4):
        if i in col:
            break
        else:
            col.append(i)
            
            if (i + j) in positive_diagonal:
                break
            else:
                positive_diagonal.append(i + j)
                print("yes")
                print(i)
                print(j)
                print(col)
print(col)
print(positive_diagonal)