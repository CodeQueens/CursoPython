weight = int(input())
if(weight > 50):
    excess = weight - 50
    forfeit = excess * 4
    print("João had an excess of {}, so, the forfeit is: R$ {:.2f}" .format(excess, forfeit))
else:
    print("No excess")