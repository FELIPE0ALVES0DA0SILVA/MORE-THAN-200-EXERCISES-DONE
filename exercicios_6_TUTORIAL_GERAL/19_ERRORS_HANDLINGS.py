try:
    f = open("17_sign_ups.csv")
    if f:
        """
        This handle underneath is to give start in something, if something in the current stage give wrong
        """
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print("Sorry, this file don't exist")
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")
