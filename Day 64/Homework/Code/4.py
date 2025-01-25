def pillars(num_pill, dist, width):
    if num_pill == 1:
        return 0
    elif num_pill == 2:
        return dist * 100
    else:
        return (num_pill - 2)* width + (dist * 100)*(num_pill - 1)