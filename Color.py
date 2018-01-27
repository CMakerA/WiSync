class Color:
    def __init__(self, red: int, green: int, blue: int, alpha: int = -1):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def has_alpha(self) -> bool:
        return self.alpha >= 0

    def get(self) -> (int, int, int, int):
        if self.has_alpha():
            return self.red, self.green, self.blue, self.alpha
        else:
            return self.red, self.green, self.blue

    @staticmethod
    def hex_to_rgb(value: str) -> (int, int, int):
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))