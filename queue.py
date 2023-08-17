from collections import deque

queue = deque([])

while True:
    print(
        "Choose a number from following \n 1.Show queue \n 2.enque \n 3.deque \n 4.QUIT \n"
    )

    choice = int(input("Choice: "))

    if choice == 1:
        print(queue)
        continue
    elif choice == 2:
        x = int(input("Enter sa value"))
        queue.append(x)
        continue
    elif choice == 3:
        queue.popleft()
        continue
    elif choice == 4:
        quit()
    else:
        print("Incorrect input")

