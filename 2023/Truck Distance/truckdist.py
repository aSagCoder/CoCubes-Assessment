def Distance(Ax, Ay, Bx, By):
    distance_A = Ax**2 + Ay**2
    distance_B = Bx**2 + By**2

    if distance_A == distance_B:
        return distance_A
    elif distance_A < distance_B:
        return distance_A
    else:
        return distance_B
