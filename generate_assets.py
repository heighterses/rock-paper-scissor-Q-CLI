import pygame
import os
from assets.rock import create_rock_image
from assets.paper import create_paper_image
from assets.scissors import create_scissors_image
from assets.background import create_background_image

def generate_all_assets():
    pygame.init()
    
    print("Generating rock image...")
    create_rock_image()
    
    print("Generating paper image...")
    create_paper_image()
    
    print("Generating scissors image...")
    create_scissors_image()
    
    print("Generating background image...")
    create_background_image()
    
    print("All assets generated successfully!")
    pygame.quit()

if __name__ == "__main__":
    generate_all_assets()
