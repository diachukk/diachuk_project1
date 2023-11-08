import math

def calculate_func(x, s):
    g = math.sin(x) + 1 / math.sin(s)
    r = 2 * math.pow(g, 3)
    return g, r

with open("input.txt", "r") as input_file:
    lines = input_file.read().split(' ')
    x, s = map(float, lines)

g, r = calculate_func(x, s)

with open("output.txt", "w") as output_file:
    output_file.write(f"x = {x}\n")
    output_file.write(f"s = {s}\n")
    output_file.write(f"g = {g}\n")
    output_file.write(f"r = {r}\n")

print("x =", x)
print("s =", s)
print("g =", g)
print("r =", r)