class Unit:
    def move_or_fly(self, field, x_axis: int, y_axis: int, course: str, fly: bool, go: bool, speed: float = 1):
        if fly and go:
            raise ValueError('Рожденный ползать летать не должен!')

        if fly:
            speed *= 1.2
            if course == 'UP':
                y_axis += speed
            elif course == 'DOWN':
                y_axis -= speed
            elif course == 'LEFT':
                x_axis -= speed
            elif course == 'RIGHT':
                x_axis += speed

        if go:
            speed *= 0.5
            if course == 'UP':
                y_axis += speed
            elif course == 'DOWN':
                y_axis -= speed
            elif course == 'LEFT':
                x_axis -= speed
            elif course == 'RIGHT':
                x_axis += speed

            field.set_unit(x=x_axis, y=y_axis, unit=self)
