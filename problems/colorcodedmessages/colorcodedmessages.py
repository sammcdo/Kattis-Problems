colors = {
    "white": (255,255,255),
    "blue": (0,0,255),
    "fuchsia": (255,0,255),
    "orange": (255,165,0),
    "ultramarine": (18,10,143),
    "crimson": (220,20,60),
    "red": (255,0,0),
    "yellow": (255,255,0),
    "silver": (192,192,192),
    "indigo": (75,0,130),
    "hazel": (165,42,42),
    "green": (0,255,0),
    "aqua": (0,255,255),
    "maroon": (128,0,0),
    "emerald": (80,200,120),
    "pink": (255,192,203),
    " ": (0, 0, 0)
}

message = ""
for i in range(int(input())):
    a, b, c = map(int, input().split())
    col = ""
    maximum = 1E9
    for color, values in colors.items():
        v1, v2, v3 = values
        d = abs(a-v1) + abs(b-v2) + abs(c-v3)
        if d < maximum:
            col = color
            maximum = min(maximum, d)
    message += col[0]
print(message)