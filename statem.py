import pygame.mouse


class State:
    def __init__(self, context):
        self.context = context

    def idle(self, screen):
        pass

    def click(self, screen):
        pass

    def next_state(self):
        pass


class StateSettingPos(State):
    def idle(self, screen):
        RED = 255, 0, 0
        r = 5
        x, y = pygame.mouse.get_pos()
        pygame.draw.circle(screen, RED, (x, y), r)

    def click(self, screen):
        self.context.next_state()

    def next_state(self):
        return StateSettingSpeed(self.context)


class StateSettingSpeed(State):
    def idle(self, screen):
        YELLOW = (255, 255, 0)
        r = 5
        x, y = pygame.mouse.get_pos()
        pygame.draw.circle(screen, YELLOW, (x, y), r)

    def click(self, screen):
        print(f"yolo on {screen}")



class Context:
    def __init__(self):
        self.state = StateSettingPos(self)

    def idle(self, screen):
        self.state.idle(screen)

    def click(self, screen):
        self.state.click(screen)

    def next_state(self):
        self.state = self.state.next_state()
