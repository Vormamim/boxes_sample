import pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0 ,255)

# Display
screen_width, screen_height = 400, 200
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Button Demo")


# Button 
button_width, button_height = 100, 50
button_x, button_y = (screen_width - button_width) // 2, (screen_height - button_height) // 2
button_color = RED
button_text = "OFF"
button_font = pygame.font.Font(None, 36)

# Loop
running = True
button_state = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                button_state = not button_state
                if button_state:
                    button_color = GREEN
                    button_text = "ON"
                    screen_color = BLUE
                else:
                    button_color = RED
                    button_text = "OFF"
                    screen_color = WHITE

    # Clear screen
    screen.fill(WHITE)

    # Draw the button
    pygame.draw.rect(screen, button_color, (button_x, button_y, button_width, button_height))
    button_surface = button_font.render(button_text, True, BLACK)
    button_rect = button_surface.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
    screen.blit(button_surface, button_rect)

    # Update display
    pygame.display.flip()

# Quit
pygame.quit()
