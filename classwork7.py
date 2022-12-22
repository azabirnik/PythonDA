
class Color:
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, r: int, g: int, b: int) -> None:
        self.rgb = (r, g, b)

    def __str__(self) -> str:
        # Cornflower blue
        return (f'{self.START};{self.rgb[0]};{self.rgb[1]};{self.rgb[2]}{self.MOD}●{self.END}{self.MOD}')

    def __eq__(self, other: "Color") -> bool:
        return self.rgb == other.rgb

    def __add__(self, other: "Color") -> "Color":
        if not isinstance(other, self):
            raise ValueError('ValueError')
        return Color(*(min(255, self.rgb[i], other.rgb[i]) for i in range(3)))

    def __hash__(self):
        return hash(self.rgb)

    def __mul__(self, c: float) -> "Color":
        if not 0.0 <= c <= 1.0:
            raise ValueError('Contrast must be between 0.0 and 1.0.')
        cl = 256 * (c - 1)
        F = 259 * (cl + 255) / 255 / (259 - cl)
        return Color(*(int(F * (self.rgb[i] - 128)) + 128 for i in range(3)))

    __rmul__ = __mul__

print(Color(255, 0, 0) * 0.5)

orange1 = Color(255, 165, 0)
red = Color(255, 0, 0)
green = Color(0, 255, 0)
orange2 = Color(255, 165, 0)

color_list = [orange1, red, green, orange2]
set(color_list)
