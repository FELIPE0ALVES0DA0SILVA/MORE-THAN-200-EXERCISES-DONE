with open("nossa_senhora.PNG", "rb") as rf:
    for nums in range(11):
        file = f"nossa_senhora_{nums}.PNG"
        with open(f"{file}", "wb") as wf:
            for line in rf:
                wf.write(line)
