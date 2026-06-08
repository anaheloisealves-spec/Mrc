temperaturas = (36.5, 37.2, 38.0, 36.8, 39.1)

for t in temperaturas:
    if t < 37.5:
        print("Normal")
    elif t <= 38.5:
        print("Febre moderada")
    else:
        print("Febre alta")