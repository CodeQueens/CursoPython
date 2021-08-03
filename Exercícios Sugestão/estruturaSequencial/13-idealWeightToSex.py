height = input() # in meters
weightM = (72.7 * float(height)) - 58
weightF = (62.1 * float(height)) - 44.7

print("Ideal weight if you're a man: {:.2f}" .format(weightM))
print("Ideal weight if you're a woman: {:.2f}" .format(weightF))