sig=input("Enter The signal color (red/green/yellow)")
match sig:
    case "red":
        print("Please Stop : ")
    case " green":
        print("You Can Go : ")
    
    case "yellow":
        print("Please Wait : ")
    case _:
        print("you Are Enter A Wrong Info :")