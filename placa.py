n = int(input())
for i in range(n):
    plate = input()
    if len(plate) == 8:
        sign = plate[3]
        front = plate[0:3]
        if sign == "-" and front.isalpha() and front == front.upper():
            tail = plate[4:8]
            try:
                l = int(tail)
                last_digit = int(tail[3])
                if 1 <= last_digit <= 2:
                    print("MONDAY")
                elif 3 <= last_digit <= 4:
                    print("TUESDAY")
                elif 5 <= last_digit <= 6:
                    print("WEDNESDAY")
                elif 7 <= last_digit <= 8:
                    print("THURSDAY")
                else:
                    print("FRIDAY")
            except:
                print("FAILURE")
        else:
            print("FAILURE")
    else:
        print("FAILURE")
