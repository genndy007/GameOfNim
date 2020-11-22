import pygame

GREEN = (0,255,0)
BLACK = (0,0,0)


class Thing:
    def __init__(self, x, y, width, height, pile_number, color=GREEN):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pile_number = pile_number


    def draw(self, scr, outline=BLACK):
        if outline:
            pygame.draw.rect(scr, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)

        pygame.draw.rect(scr, self.color, (self.x, self.y, self.width, self.height), 0)


    def isOver(self, pos):
        mouse_x = pos[0]
        mouse_y = pos[1]

        if mouse_x > self.x and mouse_x < self.x + self.width:
            if mouse_y > self.y and mouse_y < self.y + self.height:
                return True

        return False