import random


def initialize_snake(width, height):
    board = [[0 for _ in range(width)] for _ in range(height)]
    board[int(height/2)][1] = 1
    board[int(height/2)][2] = 1
    return board

def initialize_head(width, height):
    board = [[0 for _ in range(width)] for _ in range(height)]
    board[int(height / 2)][3] = 1
    return board

def initialize_food(width, height):
    board = [[0 for _ in range(width)] for _ in range(height)]
    board[int(height / 2)][width-2] = 1
    return board

class SnakeGame:

    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.game_over = False

        self.snake = [
            (int(height/2), 3),
            (int(height/2), 2),
            (int(height/2), 1),
        ]

        self.direction = "right"

        self.snake_body = initialize_snake(width, height)
        self.head = initialize_head(width, height)
        self.food = initialize_food(width, height)

        self.score = 0


    def print_board(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.snake_body[row][col] == 1:
                    print('*', end=' ')
                elif self.head[row][col] == 1:
                    print('@', end=' ')
                elif self.food[row][col] == 1:
                    print('X', end=' ')
                else:
                    print('.', end=' ')
            print()


    def update_state(self, food=False):
        #self.snake_body = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                self.snake_body[i][j] = 0
                self.head[i][j] = 0
                if food:
                    self.food[i][j] = 0

        for i in range(1,len(self.snake)):
            self.snake_body[self.snake[i][0]][self.snake[i][1]] = 1

        self.head[self.snake[0][0]][self.snake[0][1]] = 1

        if food:
            zero_positions = [(i, j) for i in range(self.height)
                              for j in range(self.width) if (self.snake_body[i][j] == 0 and self.head[i][j] == 0)]

            if zero_positions:
                row, col = random.choice(zero_positions)
                self.food[row][col] = 1


    def update_game(self, action):
        # turn left:  [1,0,0]
        # straight:   [0,1,0]
        # turn right: [0,0,1]

        head_position = self.snake[0]

        # when the action is left:
        if action == [1,0,0]:

            if self.direction == "right":

                # wall:
                if head_position[0] == 0:
                    self.game_over = True
                    return

                # body:
                elif self.snake_body[head_position[0] - 1][head_position[1]] == 1:
                    self.game_over = True
                    return


                # food:
                elif self.food[head_position[0]-1][head_position[1]] == 1:
                    self.food[head_position[0]-1][head_position[1]] = 0
                    self.snake.insert(0, (head_position[0]-1, head_position[1]))
                    self.score += 1
                    self.update_state(food=True)

                # just move:
                else:
                    for i in range(len(self.snake)-1 , 0, -1):
                        self.snake[i] = self.snake[i-1]
                    self.snake[0] = (head_position[0]-1, head_position[1])
                    self.update_state()

                self.direction = "up"

            elif self.direction == "down":

                # wall:
                if head_position[1] == self.width-1:
                    self.game_over = True
                    return

                # body:
                elif self.snake_body[head_position[0]][head_position[1] + 1] == 1:
                    self.game_over = True
                    return

                # food:
                elif self.food[head_position[0]][head_position[1] + 1] == 1:
                    self.food[head_position[0]][head_position[1] + 1] = 0
                    self.snake.insert(0, (head_position[0], head_position[1] + 1))
                    self.score += 1
                    self.update_state(food=True)

                # just move:
                else:
                    for i in range(len(self.snake)-1 , 0, -1):
                        self.snake[i] = self.snake[i - 1]
                    self.snake[0] = (head_position[0], head_position[1] + 1)
                    self.update_state()

                self.direction = "right"

            elif self.direction == "left":

                # wall:
                if head_position[0] == self.height - 1:
                    self.game_over = True
                    return

                # body:
                elif self.snake_body[head_position[0] + 1][head_position[1]] == 1:
                    self.game_over = True
                    return

                # food:
                elif self.food[head_position[0] + 1][head_position[1]] == 1:
                    self.food[head_position[0] + 1][head_position[1]] = 0
                    self.snake.insert(0, (head_position[0] + 1, head_position[1]))
                    self.score += 1
                    self.update_state(food=True)

                # just move:
                else:
                    for i in range(len(self.snake)-1 , 0, -1):
                        self.snake[i] = self.snake[i - 1]
                    self.snake[0] = (head_position[0] + 1, head_position[1])
                    self.update_state()

                self.direction = "down"

            elif self.direction == "up":

                # wall:
                if head_position[1] == 0:
                    self.game_over = True
                    return

                # body:
                elif self.snake_body[head_position[0]][head_position[1] - 1] == 1:
                    self.game_over = True
                    return

                # food:
                elif self.food[head_position[0]][head_position[1] - 1] == 1:
                    self.food[head_position[0]][head_position[1] - 1] = 0
                    self.snake.insert(0, (head_position[0], head_position[1] - 1))
                    self.score += 1
                    self.update_state(food=True)

                # just move:
                else:
                    for i in range(len(self.snake)-1 , 0, -1):
                        self.snake[i] = self.snake[i - 1]
                    self.snake[0] = (head_position[0], head_position[1] - 1)
                    self.update_state()

                self.direction = "left"


        # when the action is straight:
        elif action == [0,1,0]:

            if self.direction == "right":

                # wall:
                if head_position[1] == self.width - 1:
                    self.game_over = True
                    return

                # body:
                elif self.snake_body[head_position[0]][head_position[1] + 1] == 1:
                    self.game_over = True
                    return

                # food:
                elif self.food[head_position[0]][head_position[1] + 1] == 1:
                    self.food[head_position[0]][head_position[1] + 1] = 0
                    self.snake.insert(0, (head_position[0], head_position[1] + 1))
                    self.score += 1
                    self.update_state(food=True)

                # just move:
                else:
                    for i in range(len(self.snake)-1 , 0, -1):
                        self.snake[i] = self.snake[i - 1]
                    self.snake[0] = (head_position[0], head_position[1] + 1)
                    self.update_state()

            elif self.direction == "down":

                # wall:
                if head_position[0] == self.height - 1:
                    self.game_over = True
                    return

                # body:
                elif self.snake_body[head_position[0] + 1][head_position[1]] == 1:
                    self.game_over = True
                    return

                # food:
                elif self.food[head_position[0] + 1][head_position[1]] == 1:
                    self.food[head_position[0] + 1][head_position[1]] = 0
                    self.snake.insert(0, (head_position[0] + 1, head_position[1]))
                    self.score += 1
                    self.update_state(food=True)

                # just move:
                else:
                    for i in range(len(self.snake)-1 , 0, -1):
                        self.snake[i] = self.snake[i - 1]
                    self.snake[0] = (head_position[0] + 1, head_position[1])
                    self.update_state()

            elif self.direction == "left":

                # wall:
                if head_position[1] == 0:
                    self.game_over = True
                    return

                # body:
                elif self.snake_body[head_position[0]][head_position[1] - 1] == 1:
                    self.game_over = True
                    return

                # food:
                elif self.food[head_position[0]][head_position[1] - 1] == 1:
                    self.food[head_position[0]][head_position[1] - 1] = 0
                    self.snake.insert(0, (head_position[0], head_position[1] - 1))
                    self.score += 1
                    self.update_state(food=True)

                # just move:
                else:
                    for i in range(len(self.snake)-1 , 0, -1):
                        self.snake[i] = self.snake[i - 1]
                    self.snake[0] = (head_position[0], head_position[1] - 1)
                    self.update_state()

            elif self.direction == "up":

                # wall:
                if head_position[0] == 0:
                    self.game_over = True
                    return

                # body:
                elif self.snake_body[head_position[0] - 1][head_position[1]] == 1:
                    self.game_over = True
                    return

                # food:
                elif self.food[head_position[0] - 1][head_position[1]] == 1:
                    self.food[head_position[0] - 1][head_position[1]] = 0
                    self.snake.insert(0, (head_position[0] - 1, head_position[1]))
                    self.score += 1
                    self.update_state(food=True)

                # just move:
                else:
                    for i in range(len(self.snake)-1 , 0, -1):
                        self.snake[i] = self.snake[i - 1]
                    self.snake[0] = (head_position[0] - 1, head_position[1])
                    self.update_state()


        # when the action is right:
        elif action == [0,0,1]:

            if self.direction == "right":

                # wall:
                if head_position[0] == self.height - 1:
                    self.game_over = True
                    return

                # body:
                elif self.snake_body[head_position[0] + 1][head_position[1]] == 1:
                    self.game_over = True
                    return

                # food:
                elif self.food[head_position[0] + 1][head_position[1]] == 1:
                    self.food[head_position[0] + 1][head_position[1]] = 0
                    self.snake.insert(0, (head_position[0] + 1, head_position[1]))
                    self.score += 1
                    self.update_state(food=True)

                # just move:
                else:
                    for i in range(len(self.snake)-1 , 0, -1):
                        self.snake[i] = self.snake[i - 1]
                    self.snake[0] = (head_position[0] + 1, head_position[1])
                    self.update_state()

                self.direction = "down"

            elif self.direction == "down":

                # wall:
                if head_position[1] == 0:
                    self.game_over = True
                    return

                # body:
                elif self.snake_body[head_position[0]][head_position[1] - 1] == 1:
                    self.game_over = True
                    return

                # food:
                elif self.food[head_position[0]][head_position[1] - 1] == 1:
                    self.food[head_position[0]][head_position[1] - 1] = 0
                    self.snake.insert(0, (head_position[0], head_position[1] - 1))
                    self.score += 1
                    self.update_state(food=True)

                # just move:
                else:
                    for i in range(len(self.snake)-1 , 0, -1):
                        self.snake[i] = self.snake[i - 1]
                    self.snake[0] = (head_position[0], head_position[1] - 1)
                    self.update_state()

                self.direction = "left"

            elif self.direction == "left":

                # wall:
                if head_position[0] == 0:
                    self.game_over = True
                    return

                # body:
                elif self.snake_body[head_position[0] - 1][head_position[1]] == 1:
                    self.game_over = True
                    return

                # food:
                elif self.food[head_position[0] - 1][head_position[1]] == 1:
                    self.food[head_position[0] - 1][head_position[1]] = 0
                    self.snake.insert(0, (head_position[0] - 1, head_position[1]))
                    self.score += 1
                    self.update_state(food=True)

                # just move:
                else:
                    for i in range(len(self.snake)-1 , 0, -1):
                        self.snake[i] = self.snake[i - 1]
                    self.snake[0] = (head_position[0] - 1, head_position[1])
                    self.update_state()

                self.direction = "up"

            elif self.direction == "up":

                # wall:
                if head_position[1] == self.width - 1:
                    self.game_over = True
                    return

                # body:
                elif self.snake_body[head_position[0]][head_position[1] + 1] == 1:
                    self.game_over = True
                    return

                # food:
                elif self.food[head_position[0]][head_position[1] + 1] == 1:
                    self.food[head_position[0]][head_position[1] + 1] = 0
                    self.snake.insert(0, (head_position[0], head_position[1] + 1))
                    self.score += 1
                    self.update_state(food=True)

                # just move:
                else:
                    for i in range(len(self.snake)-1 , 0, -1):
                        self.snake[i] = self.snake[i - 1]
                    self.snake[0] = (head_position[0], head_position[1] + 1)
                    self.update_state()

                self.direction = "right"


game = SnakeGame(10, 10)
game.print_board()

while(1):
    a = int(input())
    if a == 1:
        action = [1,0,0]
    elif a == 2:
        action = [0,1,0]
    elif a == 3:
        action = [0,0,1]
    else:
        break

    game.update_game(action)
    print('-------\t' + str(game.score) + '\t-------')
    game.print_board()
