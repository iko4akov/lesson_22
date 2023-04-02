# Вам не кажется, что CubeVolumeCalculator 
# чаще дергает методы класса Cube? Исправьте так, 
# чтобы избавиться от лишних обращений к классу Cube


class Cube:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def _get_x(self):
        return self.x

    def _get_y(self):
        return self.y

    def _get_z(self):
        return self.z

class CubeVolumeCalculator(Cube):

    def __init__(self, x, y, z):
        super().__init__(self, x, y, z)

    def calc_cube_volume(self):
        return self.y * self.x * self.z
