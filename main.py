import pygame
import sys
import random
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Rock Paper Scissors"
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Game states
MENU = 0
PLAYING = 1
RESULT = 2

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.current_color = color
        self.is_hovered = False
        
    def draw(self, surface, font):
        pygame.draw.rect(surface, self.current_color, self.rect, border_radius=10)
        pygame.draw.rect(surface, BLACK, self.rect, 2, border_radius=10)
        
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
        
    def update(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        self.current_color = self.hover_color if self.is_hovered else self.color
        
    def is_clicked(self, event):
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            return self.is_hovered
        return False

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)
        self.clock = pygame.time.Clock()
        self.font_large = pygame.font.SysFont('Arial', 48)
        self.font_medium = pygame.font.SysFont('Arial', 36)
        self.font_small = pygame.font.SysFont('Arial', 24)
        
        # Game state
        self.state = MENU
        self.player_choice = None
        self.computer_choice = None
        self.result = None
        
        # Create buttons
        button_width = 200
        button_height = 60
        button_margin = 30
        
        # Menu buttons
        self.play_button = Button(
            WINDOW_WIDTH // 2 - button_width // 2,
            WINDOW_HEIGHT // 2 - button_height // 2,
            button_width, button_height,
            "Play Game", GRAY, WHITE
        )
        
        # Game buttons
        self.rock_button = Button(
            WINDOW_WIDTH // 2 - button_width * 1.5 - button_margin,
            WINDOW_HEIGHT // 2,
            button_width, button_height,
            "Rock", GRAY, WHITE
        )
        
        self.paper_button = Button(
            WINDOW_WIDTH // 2 - button_width // 2,
            WINDOW_HEIGHT // 2,
            button_width, button_height,
            "Paper", GRAY, WHITE
        )
        
        self.scissors_button = Button(
            WINDOW_WIDTH // 2 + button_width // 2 + button_margin,
            WINDOW_HEIGHT // 2,
            button_width, button_height,
            "Scissors", GRAY, WHITE
        )
        
        # Result button
        self.play_again_button = Button(
            WINDOW_WIDTH // 2 - button_width // 2,
            WINDOW_HEIGHT * 3 // 4,
            button_width, button_height,
            "Play Again", GRAY, WHITE
        )
        
        self.menu_button = Button(
            WINDOW_WIDTH // 2 - button_width // 2,
            WINDOW_HEIGHT * 3 // 4 + button_height + button_margin,
            button_width, button_height,
            "Main Menu", GRAY, WHITE
        )
    
    def run(self):
        running = True
        
        while running:
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                
                if self.state == MENU:
                    if self.play_button.is_clicked(event):
                        self.state = PLAYING
                
                elif self.state == PLAYING:
                    if self.rock_button.is_clicked(event):
                        self.player_choice = "Rock"
                        self.computer_choice = random.choice(["Rock", "Paper", "Scissors"])
                        self.determine_winner()
                        self.state = RESULT
                    
                    elif self.paper_button.is_clicked(event):
                        self.player_choice = "Paper"
                        self.computer_choice = random.choice(["Rock", "Paper", "Scissors"])
                        self.determine_winner()
                        self.state = RESULT
                    
                    elif self.scissors_button.is_clicked(event):
                        self.player_choice = "Scissors"
                        self.computer_choice = random.choice(["Rock", "Paper", "Scissors"])
                        self.determine_winner()
                        self.state = RESULT
                
                elif self.state == RESULT:
                    if self.play_again_button.is_clicked(event):
                        self.state = PLAYING
                    
                    elif self.menu_button.is_clicked(event):
                        self.state = MENU
            
            # Update
            if self.state == MENU:
                self.play_button.update(mouse_pos)
            
            elif self.state == PLAYING:
                self.rock_button.update(mouse_pos)
                self.paper_button.update(mouse_pos)
                self.scissors_button.update(mouse_pos)
            
            elif self.state == RESULT:
                self.play_again_button.update(mouse_pos)
                self.menu_button.update(mouse_pos)
            
            # Draw
            self.screen.fill(WHITE)
            
            if self.state == MENU:
                self.draw_menu()
            
            elif self.state == PLAYING:
                self.draw_game()
            
            elif self.state == RESULT:
                self.draw_result()
            
            pygame.display.flip()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()
    
    def draw_menu(self):
        title_text = self.font_large.render("Rock Paper Scissors", True, BLACK)
        title_rect = title_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
        self.screen.blit(title_text, title_rect)
        
        self.play_button.draw(self.screen, self.font_medium)
    
    def draw_game(self):
        title_text = self.font_medium.render("Choose your move:", True, BLACK)
        title_rect = title_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
        self.screen.blit(title_text, title_rect)
        
        self.rock_button.draw(self.screen, self.font_small)
        self.paper_button.draw(self.screen, self.font_small)
        self.scissors_button.draw(self.screen, self.font_small)
    
    def draw_result(self):
        # Display choices
        player_text = self.font_medium.render(f"You chose: {self.player_choice}", True, BLUE)
        player_rect = player_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 4))
        self.screen.blit(player_text, player_rect)
        
        computer_text = self.font_medium.render(f"Computer chose: {self.computer_choice}", True, RED)
        computer_rect = computer_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
        self.screen.blit(computer_text, computer_rect)
        
        # Display result
        result_color = GREEN if self.result == "You win!" else RED if self.result == "You lose!" else BLACK
        result_text = self.font_large.render(self.result, True, result_color)
        result_rect = result_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        self.screen.blit(result_text, result_rect)
        
        self.play_again_button.draw(self.screen, self.font_small)
        self.menu_button.draw(self.screen, self.font_small)
    
    def determine_winner(self):
        if self.player_choice == self.computer_choice:
            self.result = "It's a tie!"
        elif (self.player_choice == "Rock" and self.computer_choice == "Scissors") or \
             (self.player_choice == "Paper" and self.computer_choice == "Rock") or \
             (self.player_choice == "Scissors" and self.computer_choice == "Paper"):
            self.result = "You win!"
        else:
            self.result = "You lose!"

if __name__ == "__main__":
    game = Game()
    game.run()
