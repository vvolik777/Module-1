import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Pong Game'
BALL_SPEED = 3
BAR_SPEED = 5


class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('ball.png', 0.05)
        self.change_x = BALL_SPEED
        self.change_y = BALL_SPEED

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Отскок от стен
        if self.right >= SCREEN_WIDTH or self.left <= 0:
            self.change_x = -self.change_x
        if self.top >= SCREEN_HEIGHT:
            self.change_y = -self.change_y

        if self.bottom <= 0:
            self.reset_position()

    def reset_position(self):
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2
        self.change_y = BALL_SPEED


class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('bar.png', 0.2)

    def update(self):
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left <= 0:
            self.left = 0


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bar = Bar()
        self.ball = Ball()
        self.score = 0
        self.setup()

    def setup(self):
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 10
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2
        self.bar.change_x = 0

    def on_draw(self):
        self.clear((255, 255, 255))
        self.bar.draw()
        self.ball.draw()

        arcade.draw_text(f"Score: {self.score}", 10, SCREEN_HEIGHT - 30, arcade.color.BLACK, 20)
        # отображение счета

    def update(self, delta_time):

        if arcade.check_for_collision(self.bar, self.ball) and self.ball.change_y < 0:
            self.ball.change_y = -self.ball.change_y
            self.ball.change_x += self.bar.change_x * 0.1
            self.score += 1  # увеличение счета

        self.ball.update()
        self.bar.update()

    def on_key_press(self, key, modifiers):

        if key == arcade.key.RIGHT:
            self.bar.change_x = BAR_SPEED
        if key == arcade.key.LEFT:
            self.bar.change_x = -BAR_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.bar.change_x = 0


if __name__ == "__main__":
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
