import pygame
import os

def create_paper_image():
    # Create a surface for the paper image
    image = pygame.Surface((200, 200), pygame.SRCALPHA)
    
    # Colors
    paper_color = (250, 250, 250)  # White
    shadow_color = (220, 220, 220)
    edge_color = (200, 200, 200)
    
    # Draw the main paper shape
    pygame.draw.polygon(image, shadow_color, [(20, 20), (180, 20), (180, 180), (20, 180)])
    pygame.draw.polygon(image, paper_color, [(10, 10), (170, 10), (170, 170), (10, 170)])
    
    # Add some details to make it look more like paper
    pygame.draw.line(image, edge_color, (30, 40), (150, 40), 1)
    pygame.draw.line(image, edge_color, (30, 60), (150, 60), 1)
    pygame.draw.line(image, edge_color, (30, 80), (150, 80), 1)
    pygame.draw.line(image, edge_color, (30, 100), (150, 100), 1)
    pygame.draw.line(image, edge_color, (30, 120), (150, 120), 1)
    pygame.draw.line(image, edge_color, (30, 140), (150, 140), 1)
    
    # Save the image
    if not os.path.exists('assets'):
        os.makedirs('assets')
    
    pygame.image.save(image, "assets/paper.png")
    return image

if __name__ == "__main__":
    pygame.init()
    create_paper_image()
    pygame.quit()
