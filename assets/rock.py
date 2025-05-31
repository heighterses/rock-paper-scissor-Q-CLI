import pygame
import os

def create_rock_image():
    # Create a surface for the rock image
    image = pygame.Surface((200, 200), pygame.SRCALPHA)
    
    # Colors
    rock_color = (139, 137, 137)  # Gray
    shadow_color = (100, 100, 100)
    highlight_color = (180, 180, 180)
    
    # Draw the main rock shape
    pygame.draw.ellipse(image, shadow_color, (20, 30, 160, 150))
    pygame.draw.ellipse(image, rock_color, (10, 20, 160, 150))
    
    # Add some details to make it look more like a rock
    pygame.draw.ellipse(image, highlight_color, (30, 40, 40, 30))
    pygame.draw.ellipse(image, highlight_color, (100, 50, 30, 20))
    pygame.draw.ellipse(image, shadow_color, (50, 100, 60, 40))
    
    # Save the image
    if not os.path.exists('assets'):
        os.makedirs('assets')
    
    pygame.image.save(image, "assets/rock.png")
    return image

if __name__ == "__main__":
    pygame.init()
    create_rock_image()
    pygame.quit()
