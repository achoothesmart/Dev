def growth(inv, per, years):
    inter = inv * per / 100
    ret = inv + inter

    if years == 1:
        return ret
    else:
        return growth(ret, per, years-1)
    
print(growth(inv=1471598, per=5, years=10))