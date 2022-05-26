def ask_for_int():
    try:
        result=int(input("please provide number: "))
    except:
        print("whoops! That is not a number")
    finally:
        print("End of try/except/finally")
