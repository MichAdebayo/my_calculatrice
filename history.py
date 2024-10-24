
def history(x):
    with open("log_calculations.txt", "w") as f:
        for elem in x:
            f.write(elem)
    

# def show_results():
#     print(l)

