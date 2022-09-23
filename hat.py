from sense_hat import SenseHat


class hat:
    def __init__(self):
        self.__hat__ = SenseHat()

    def clear_resource(self):
        self.__hat__.clear()

    def get_env(self):
        return {
            "pressure": self.__hat__.get_pressure(),
            "temperature": self.__hat__.get_temperature(),
            "humidity": self.__hat__.get_humidity()
        }

    def get_movement(self):
        orientation = self.__hat__.get_orientation()
        acceleration = self.__hat__.get_accelerometer_raw()
        return {
            "pitch": orientation["pitch"],
            "roll": orientation["roll"],
            "yaw": orientation["yaw"],
            "x": acceleration["x"],
            "y": acceleration["y"],
            "z": acceleration["z"],
            "x_rounded": round(acceleration["x"], 0),
            "y_rounded": round(acceleration["y"], 0),
            "z_rounded": round(acceleration["z"], 0)
        }

    def display_text(self, message: str):
        self.__hat__.show_message(message)

    def display_character(self, character: str):
        self.__hat__.show_letter(character)

    def display_image(self,
                      image: [[]]
                      ):

        matrix = [[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
                  [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
                  [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
                  [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
                  [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
                  [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
                  [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
                  [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]]

        for row_index, row in enumerate(image):
            for value_index, value in enumerate(row):
                if value != (0, 0, 0):
                    matrix[row_index][value_index] = value

        self.__hat__.set_pixels(matrix)

    def flip_h(self):
        self.__hat__.flip_h()

    def flip_v(self):
        self.__hat__.flip_v()

    def rotate(self, angle):
        self.__hat__.set_rotation(angle)

    def get_joypad(self):
        for event in self.__hat__.stick.get_events():
            print(event.direction, event.action)
