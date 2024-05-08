import random


class SnakeGame:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.snake_position = [(10, 10), (10, 9), (10, 8)]
        self.snake_direction = 'ВПРАВО'
        self.food_position = self.spawn_food()
        self.score = 0

    def print_field(self):
        for y in range(self.height + 2):
            for x in range(self.width + 2):
                if x == 0 or y == 0 or x == self.width + 1 or y == self.height + 1:
                    print('+', end='')
                elif (x - 1, y - 1) == self.snake_position[0]:
                    print('@', end='')
                elif (x - 1, y - 1) in self.snake_position:
                    print('#', end='')
                elif (x - 1, y - 1) == self.food_position:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()

    def change_direction(self, new_direction):
        opposites = {'ВВЕРХ': 'ВНИЗ', 'ВНИЗ': 'ВВЕРХ', 'ВЛЕВО': 'ВПРАВО', 'ВПРАВО': 'ВЛЕВО'}
        if opposites[new_direction] != self.snake_direction:
            self.snake_direction = new_direction

    def move_snake(self):
        head_x, head_y = self.snake_position[0]
        move_offsets = {'ВВЕРХ': (0, -1), 'ВНИЗ': (0, 1), 'ВЛЕВО': (-1, 0), 'ВПРАВО': (1, 0)}
        new_head = (head_x + move_offsets[self.snake_direction][0], head_y + move_offsets[self.snake_direction][1])
        self.snake_position.insert(0, new_head)
        if new_head == self.food_position:
            self.score += 1
            self.food_position = self.spawn_food()
        else:
            self.snake_position.pop()

    def spawn_food(self):
        while True:
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            if (x, y) not in self.snake_position:
                return (x, y)

    def check_collisions(self):
        head = self.snake_position[0]
        return (head[0] < 0 or head[0] >= self.width or
                head[1] < 0 or head[1] >= self.height or
                head in self.snake_position[1:])

    def play_step(self):
        self.move_snake()
        if self.check_collisions():
            print('Игра окончена!')
            print(f'Итоговый счёт: {self.score}')
            return True
        self.print_field()
        print(f'Счёт: {self.score}')
        return False


def main():
    game = SnakeGame()
    while True:
        if game.play_step():
            break


if __name__ == "__main__":
    main()
