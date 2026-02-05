#match case statements 

x=int(input("Enter Grade of Student from 1-5"))

match x:
    case 1:
        print("Result is Outstanding")
    case 2:
        print("Result is Great ")
    case 3:
        print("Result is Good")
    case 4:
        print("Need more Focus")
    case 5:
        print("Better luck for next time")
    case _:
        print("Invalid Grade")