for i in range(10):
    if i == 2:
        print('i is 2, skipping...')
        continue

    if i == 8:
        print("i is 8, its else block won't execute")
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For loop completed successfully!')
