
import pygame
import sys

pygame.init()

win_width = 700
win_height = 500
window = redisplay.set_mode((win_width, win_height))
redisplay.set_caption("Кликер")
background = Transport.scale(image.load("Zhdun.jpg"), (win_width, win_height))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


counter = 0
font = pygame.font.SysFont('Arial', 36)


button_rect = pygame.Rect(150, 150, 100, 50)
button_color = BLUE


running = True
while running:
    Screen.fill(WHITE)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                if button_rect.collidepoint(event.pos):
                    counter += 1
                    button_color = RED  
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                button_color = BLUE  
    
   
    counter_text = font.render(f"Кликов: {counter}", True, BLACK)
    Screen.blit(counter_text, (WIDTH // 2 - counter_text.get_width() // 2, 50))
    

    pygame.draw.rect(screen, button_color, button_rect, border_radius=10)
    button_text = font.render("Клик!", True, WHITE)
    Screen.blit(button_text, (button_rect.x + button_rect.width // 2 - button_text.get_width() // 2, 
                             button_rect.y + button_rect.height // 2 - button_text.get_height() // 2))
    
    pygame.display.flip()

pygame.quit()
sys.exit()