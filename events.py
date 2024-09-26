import pygame
pygame.init()
screen = pygame.display.set_mode((700, 700))
class circle():
    def __init__(self, x, y, color, radius):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    def grow_bigger(self):
        self.radius += 5
        self.draw()
c1 = circle(100,100, "yellow", 25) 
screen.fill("light blue")
pygame.display.update()             
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            c1.draw()    
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            c1.grow_bigger()  
            pygame.display.update()    
        if event.type == pygame.MOUSEMOTION:   
            pos = pygame.mouse.get_pos()
            c2 = circle(pos[0], pos[1], "dark blue", 1)
            c2.draw()
            pygame.display.update()
            
            
    