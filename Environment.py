class Environment:
    def __init__(self, grid, bots):
        self.original_grid = np.array(grid)
        self.grid = self.original_grid.copy()
        self.bots = bots
        self.height, self.width = self.grid.shape
        self.steps = 0

    def is_valid_move(self, position):
        x, y = position
        return 0 <= x < self.height and 0 <= y < self.width and self.original_grid[x, y] != 'X'

    def get_state(self):
        return tuple(bot.position for bot in self.bots)

    def step(self, actions):
        rewards = np.zeros(len(self.bots))
        new_positions = []

        for i, (bot, action) in enumerate(zip(self.bots, actions)):
            new_pos = (bot.position[0] + ACTIONS[action][0], bot.position[1] + ACTIONS[action][1])
            if self.is_valid_move(new_pos) and new_pos not in new_positions:
                new_positions.append(new_pos)
                bot.move(ACTIONS[action])
                rewards[i] = 100 if bot.reached_goal() else -1
            else:
                new_positions.append(bot.position)
                bot.movements.append('Wait')  # Add 'Wait' if the bot couldn't move
                rewards[i] = -5

        rewards[np.array([new_positions.count(pos) > 1 for pos in new_positions])] -= 10

        self.steps += 1
        self.update_grid()
        done = all(bot.reached_goal() for bot in self.bots)
        return self.get_state(), rewards, done

    def update_grid(self):
        self.grid = self.original_grid.copy()
        for bot in self.bots:
            x, y = bot.position
            self.grid[x, y] = '⛳️' if bot.reached_goal() else bot.name
