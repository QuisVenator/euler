for i in range(1, 10**6):
    i_str = sorted(str(i))
    for j in range(2, 7):
        if i_str != sorted(str(j * i)):
            break
    else:
        print(i)
        break