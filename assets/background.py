import pygame
import os
import random

def create_background_image(width=800, height=600):
    # Create a surface for the background
    image = pygame.Surface((width, height))
    
    # Create a gradient background
    for y in range(height):
        # Calculate gradient color (light blue to darker blue)
        color_value = 255 - int(y * 0.3)
        color = (color_value, color_value, 255)
        pygame.draw.line(image, color, (0, y), (width, y))
    
    # Add some decorative elements
    for _ in range(30):
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(2, 5)
        brightness = random.randint(200, 255)
        pygame.draw.circle(image, (brightness, brightness, brightness), (x, y), size)
    
    # Save the image
    if not os.path.exists('assets'):
        os.makedirs('assets')
    
    pygame.image.save(image, "assets/background.png")
    return image

if __name__ == "__main__":
    pygame.init()
    create_background_image()
    pygame.quit()
