import pygame
import os

def create_scissors_image():
    # Create a surface for the scissors image
    image = pygame.Surface((200, 200), pygame.SRCALPHA)
    
    # Colors
    handle_color = (70, 70, 70)
    blade_color = (200, 200, 200)
    highlight_color = (240, 240, 240)
    
    # Draw the scissors handles
    pygame.draw.circle(image, handle_color, (60, 140), 30)
    pygame.draw.circle(image, handle_color, (140, 140), 30)
    
    # Draw the finger holes
    pygame.draw.circle(image, (30, 30, 30), (60, 140), 30, 2)
    pygame.draw.circle(image, (30, 30, 30), (140, 140), 30, 2)
    pygame.draw.circle(image, (0, 0, 0, 0), (60, 140), 15)
    pygame.draw.circle(image, (0, 0, 0, 0), (140, 140), 15)
    
    # Draw the blades
    pygame.draw.polygon(image, blade_color, [(60, 140), (100, 40), (110, 50), (70, 130)])
    pygame.draw.polygon(image, blade_color, [(140, 140), (100, 40), (90, 50), (130, 130)])
    
    # Add highlights
    pygame.draw.line(image, highlight_color, (100, 40), (110, 50), 2)
    pygame.draw.line(image, highlight_color, (100, 40), (90, 50), 2)
    
    # Save the image
    if not os.path.exists('assets'):
        os.makedirs('assets')
    
    pygame.image.save(image, "assets/scissors.png")
    return image

if __name__ == "__main__":
    pygame.init()
    create_scissors_image()
    pygame.quit()
