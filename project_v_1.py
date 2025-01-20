dict_2={}

resp="yes"
while resp.lower()=="yes":
    name = input("What's your name?\n")
    bid = int(input("What's your bidding price?\n"))
    dict_2[name]=bid
    resp=input("Type yes to continue,type anything else to exit the system\n")

if dict_2:
    max_bid = 0
    max_name=""
    for k in dict_2:
        if dict_2[k] > max_bid:
            max_bid = dict_2[k]
            max_name = k
    print(f"The winner is {max_name} and their bidding price is {max_bid} !")






