from pieces.enums.colors import Color


class Current_Color_Keeper():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.current_color: Color = Color.White 
        return cls._instance

    def toggle_color(self):
        if self.current_color == Color.White:
            self.current_color = Color.Black
        else:
            self.current_color = Color.White

    def get_current_color(self):
        return self.current_color