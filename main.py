import pygame
import sys
import random
import os
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
LIGHT_BLUE = (173, 216, 230)
GOLD = (255, 215, 0)

# Game states
MENU = 0
PLAYING = 1
RESULT = 2

# Load images
def load_images():
    images = {}
    
    # Check if assets directory exists
    if not os.path.exists('assets'):
        os.makedirs('assets')
    
    # Load background
    try:
        images['background'] = pygame.image.load('assets/background.png').convert()
    except:
        # Create a default background if image doesn't exist
        bg = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        bg.fill(LIGHT_BLUE)
        images['background'] = bg
    
    # Load rock, paper, scissors images
    try:
        images['rock'] = pygame.image.load('assets/rock.png').convert_alpha()
        images['paper'] = pygame.image.load('assets/paper.png').convert_alpha()
        images['scissors'] = pygame.image.load('assets/scissors.png').convert_alpha()
    except:
        # Create default images if they don't exist
        default = pygame.Surface((100, 100), pygame.SRCALPHA)
        pygame.draw.circle(default, GRAY, (50, 50), 40)
        images['rock'] = default
        
        default = pygame.Surface((100, 100), pygame.SRCALPHA)
        pygame.draw.rect(default, WHITE, (10, 10, 80, 80))
        images['paper'] = default
        
        default = pygame.Surface((100, 100), pygame.SRCALPHA)
        pygame.draw.line(default, GRAY, (30, 30), (70, 70), 5)
        pygame.draw.line(default, GRAY, (30, 70), (70, 30), 5)
        images['scissors'] = default
    
    return images

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, image=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.current_color = color
        self.is_hovered = False
        self.image = image
        self.alpha = 255  # For fade effects
        
    def draw(self, surface, font):
        # Draw button background with rounded corners
        pygame.draw.rect(surface, self.current_color, self.rect, border_radius=15)
        pygame.draw.rect(surface, BLACK, self.rect, 2, border_radius=15)
        
        # Draw image if available
        if self.image:
            # Scale image to fit button with some padding
            scaled_image = pygame.transform.scale(self.image, (self.rect.width - 20, self.rect.height - 20))
            image_rect = scaled_image.get_rect(center=self.rect.center)
            surface.blit(scaled_image, image_rect)
        
        # Draw text
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        
        # If there's an image, move text below the image
        if self.image:
            text_rect.centery = self.rect.centery + self.rect.height // 3
            
        surface.blit(text_surface, text_rect)
        
    def update(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        target_color = self.hover_color if self.is_hovered else self.color
        
        # Smooth color transition
        r1, g1, b1 = self.current_color
        r2, g2, b2 = target_color
        self.current_color = (
            r1 + (r2 - r1) // 5,
            g1 + (g2 - g1) // 5,
            b1 + (b2 - b1) // 5
        )
        
    def is_clicked(self, event):
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            return self.is_hovered
        return False

class AnimatedText:
    def __init__(self, text, font, color, target_pos):
        self.text = text
        self.font = font
        self.color = color
        self.target_pos = target_pos
        self.current_pos = (target_pos[0], target_pos[1] - 50)  # Start above target
        self.alpha = 0
        self.scale = 0.5
        self.done = False
        
    def update(self):
        if self.done:
            return True
            
        # Move towards target position
        dx = (self.target_pos[0] - self.current_pos[0]) * 0.1
        dy = (self.target_pos[1] - self.current_pos[1]) * 0.1
        self.current_pos = (self.current_pos[0] + dx, self.current_pos[1] + dy)
        
        # Increase alpha (fade in)
        if self.alpha < 255:
            self.alpha += 15
            if self.alpha > 255:
                self.alpha = 255
                
        # Increase scale
        if self.scale < 1.0:
            self.scale += 0.05
            if self.scale > 1.0:
                self.scale = 1.0
                
        # Check if animation is complete
        if abs(self.current_pos[1] - self.target_pos[1]) < 1 and self.alpha == 255 and self.scale == 1.0:
            self.done = True
            
        return False
        
    def draw(self, surface):
        text_surface = self.font.render(self.text, True, self.color)
        text_surface.set_alpha(self.alpha)
        
        # Scale the text
        scaled_width = int(text_surface.get_width() * self.scale)
        scaled_height = int(text_surface.get_height() * self.scale)
        scaled_surface = pygame.transform.scale(text_surface, (scaled_width, scaled_height))
        
        # Draw at current position
        rect = scaled_surface.get_rect(center=self.current_pos)
        surface.blit(scaled_surface, rect)

class ParticleEffect:
    def __init__(self, x, y, color, count=20):
        self.particles = []
        for _ in range(count):
            particle = {
                'pos': [x, y],
                'vel': [random.uniform(-3, 3), random.uniform(-5, -1)],
                'size': random.randint(3, 8),
                'color': color,
                'alpha': 255,
                'gravity': 0.1
            }
            self.particles.append(particle)
            
    def update(self):
        for particle in self.particles[:]:
            # Apply gravity
            particle['vel'][1] += particle['gravity']
            
            # Update position
            particle['pos'][0] += particle['vel'][0]
            particle['pos'][1] += particle['vel'][1]
            
            # Fade out
            particle['alpha'] -= 5
            if particle['alpha'] <= 0:
                self.particles.remove(particle)
                
    def draw(self, surface):
        for particle in self.particles:
            s = pygame.Surface((particle['size'], particle['size']), pygame.SRCALPHA)
            pygame.draw.circle(s, (*particle['color'], particle['alpha']), 
                              (particle['size']//2, particle['size']//2), 
                              particle['size']//2)
            surface.blit(s, (int(particle['pos'][0]), int(particle['pos'][1])))
            
    def is_complete(self):
        return len(self.particles) == 0

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)
        self.clock = pygame.time.Clock()
        self.font_large = pygame.font.SysFont('Arial', 48, bold=True)
        self.font_medium = pygame.font.SysFont('Arial', 36)
        self.font_small = pygame.font.SysFont('Arial', 24)
        
        # Load images
        self.images = load_images()
        
        # Game state
        self.state = MENU
        self.player_choice = None
        self.computer_choice = None
        self.result = None
        
        # Animation elements
        self.animations = []
        self.particles = []
        self.shake_frames = 0
        self.shake_intensity = 5
        
        # Create buttons
        button_width = 200
        button_height = 150
        button_margin = 30
        
        # Menu buttons
        self.play_button = Button(
            WINDOW_WIDTH // 2 - button_width // 2,
            WINDOW_HEIGHT // 2 - button_height // 2,
            button_width, button_height // 2,
            "Play Game", GOLD, WHITE
        )
        
        # Game buttons
        self.rock_button = Button(
            WINDOW_WIDTH // 2 - button_width * 1.5 - button_margin,
            WINDOW_HEIGHT // 2,
            button_width, button_height,
            "Rock", GRAY, WHITE,
            self.images['rock']
        )
        
        self.paper_button = Button(
            WINDOW_WIDTH // 2 - button_width // 2,
            WINDOW_HEIGHT // 2,
            button_width, button_height,
            "Paper", GRAY, WHITE,
            self.images['paper']
        )
        
        self.scissors_button = Button(
            WINDOW_WIDTH // 2 + button_width // 2 + button_margin,
            WINDOW_HEIGHT // 2,
            button_width, button_height,
            "Scissors", GRAY, WHITE,
            self.images['scissors']
        )
        
        # Result buttons
        self.play_again_button = Button(
            WINDOW_WIDTH // 2 - button_width // 2,
            WINDOW_HEIGHT * 3 // 4,
            button_width, button_height // 2,
            "Play Again", GRAY, WHITE
        )
        
        self.menu_button = Button(
            WINDOW_WIDTH // 2 - button_width // 2,
            WINDOW_HEIGHT * 3 // 4 + button_height // 2 + 10,
            button_width, button_height // 2,
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
                        self.add_animation("Choose Your Move!", GREEN, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
                
                elif self.state == PLAYING:
                    if self.rock_button.is_clicked(event):
                        self.player_choice = "Rock"
                        self.computer_choice = random.choice(["Rock", "Paper", "Scissors"])
                        self.determine_winner()
                        self.state = RESULT
                        self.shake_frames = 10
                        self.add_particles()
                    
                    elif self.paper_button.is_clicked(event):
                        self.player_choice = "Paper"
                        self.computer_choice = random.choice(["Rock", "Paper", "Scissors"])
                        self.determine_winner()
                        self.state = RESULT
                        self.shake_frames = 10
                        self.add_particles()
                    
                    elif self.scissors_button.is_clicked(event):
                        self.player_choice = "Scissors"
                        self.computer_choice = random.choice(["Rock", "Paper", "Scissors"])
                        self.determine_winner()
                        self.state = RESULT
                        self.shake_frames = 10
                        self.add_particles()
                
                elif self.state == RESULT:
                    if self.play_again_button.is_clicked(event):
                        self.state = PLAYING
                        self.add_animation("Choose Your Move!", GREEN, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
                    
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
            
            # Update animations
            for anim in self.animations[:]:
                if anim.update():
                    self.animations.remove(anim)
                    
            # Update particles
            for particle in self.particles[:]:
                particle.update()
                if particle.is_complete():
                    self.particles.remove(particle)
                    
            # Update screen shake
            if self.shake_frames > 0:
                self.shake_frames -= 1
            
            # Draw
            self.draw()
            
            pygame.display.flip()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()
        
    def add_animation(self, text, color, position):
        self.animations.append(AnimatedText(text, self.font_large, color, position))
        
    def add_particles(self):
        if self.result == "You win!":
            color = (0, 255, 0)  # Green for win
        elif self.result == "You lose!":
            color = (255, 0, 0)  # Red for loss
        else:
            color = (255, 215, 0)  # Gold for tie
            
        for _ in range(3):
            x = random.randint(WINDOW_WIDTH // 4, WINDOW_WIDTH * 3 // 4)
            y = random.randint(WINDOW_HEIGHT // 4, WINDOW_HEIGHT * 3 // 4)
            self.particles.append(ParticleEffect(x, y, color))
    
    def draw(self):
        # Apply screen shake
        offset_x, offset_y = 0, 0
        if self.shake_frames > 0:
            offset_x = random.randint(-self.shake_intensity, self.shake_intensity)
            offset_y = random.randint(-self.shake_intensity, self.shake_intensity)
        
        # Draw background
        self.screen.blit(self.images['background'], (offset_x, offset_y))
        
        if self.state == MENU:
            self.draw_menu(offset_x, offset_y)
        
        elif self.state == PLAYING:
            self.draw_game(offset_x, offset_y)
        
        elif self.state == RESULT:
            self.draw_result(offset_x, offset_y)
            
        # Draw animations
        for anim in self.animations:
            anim.draw(self.screen)
            
        # Draw particles
        for particle in self.particles:
            particle.draw(self.screen)
    
    def draw_menu(self, offset_x=0, offset_y=0):
        # Draw title with shadow effect
        shadow_offset = 3
        title_text = self.font_large.render("Rock Paper Scissors", True, BLACK)
        title_shadow = self.font_large.render("Rock Paper Scissors", True, (50, 50, 50))
        title_rect = title_text.get_rect(center=(WINDOW_WIDTH // 2 + offset_x, WINDOW_HEIGHT // 3 + offset_y))
        shadow_rect = title_shadow.get_rect(center=(WINDOW_WIDTH // 2 + offset_x + shadow_offset, 
                                                   WINDOW_HEIGHT // 3 + offset_y + shadow_offset))
        
        self.screen.blit(title_shadow, shadow_rect)
        self.screen.blit(title_text, title_rect)
        
        # Draw decorative elements
        pygame.draw.circle(self.screen, GRAY, (WINDOW_WIDTH // 4 + offset_x, WINDOW_HEIGHT // 5 + offset_y), 40)
        pygame.draw.rect(self.screen, WHITE, (WINDOW_WIDTH // 2 - 40 + offset_x, WINDOW_HEIGHT // 5 - 40 + offset_y, 80, 80))
        pygame.draw.line(self.screen, GRAY, (WINDOW_WIDTH * 3 // 4 - 30 + offset_x, WINDOW_HEIGHT // 5 - 30 + offset_y), 
                        (WINDOW_WIDTH * 3 // 4 + 30 + offset_x, WINDOW_HEIGHT // 5 + 30 + offset_y), 5)
        pygame.draw.line(self.screen, GRAY, (WINDOW_WIDTH * 3 // 4 - 30 + offset_x, WINDOW_HEIGHT // 5 + 30 + offset_y), 
                        (WINDOW_WIDTH * 3 // 4 + 30 + offset_x, WINDOW_HEIGHT // 5 - 30 + offset_y), 5)
        
        # Draw play button
        self.play_button.draw(self.screen, self.font_medium)
    
    def draw_game(self, offset_x=0, offset_y=0):
        # Draw title
        title_text = self.font_medium.render("Choose your move:", True, BLACK)
        title_rect = title_text.get_rect(center=(WINDOW_WIDTH // 2 + offset_x, WINDOW_HEIGHT // 4 + offset_y))
        self.screen.blit(title_text, title_rect)
        
        # Draw choice buttons
        self.rock_button.draw(self.screen, self.font_small)
        self.paper_button.draw(self.screen, self.font_small)
        self.scissors_button.draw(self.screen, self.font_small)
    
    def draw_result(self, offset_x=0, offset_y=0):
        # Display choices with images
        player_text = self.font_medium.render("You chose:", True, BLUE)
        player_rect = player_text.get_rect(center=(WINDOW_WIDTH // 4 + offset_x, WINDOW_HEIGHT // 5 + offset_y))
        self.screen.blit(player_text, player_rect)
        
        computer_text = self.font_medium.render("Computer chose:", True, RED)
        computer_rect = computer_text.get_rect(center=(WINDOW_WIDTH * 3 // 4 + offset_x, WINDOW_HEIGHT // 5 + offset_y))
        self.screen.blit(computer_text, computer_rect)
        
        # Draw player choice image
        player_image = self.images[self.player_choice.lower()]
        player_image = pygame.transform.scale(player_image, (100, 100))
        player_image_rect = player_image.get_rect(center=(WINDOW_WIDTH // 4 + offset_x, WINDOW_HEIGHT // 3 + offset_y))
        self.screen.blit(player_image, player_image_rect)
        
        # Draw computer choice image
        computer_image = self.images[self.computer_choice.lower()]
        computer_image = pygame.transform.scale(computer_image, (100, 100))
        computer_image_rect = computer_image.get_rect(center=(WINDOW_WIDTH * 3 // 4 + offset_x, WINDOW_HEIGHT // 3 + offset_y))
        self.screen.blit(computer_image, computer_image_rect)
        
        # Draw VS text
        vs_text = self.font_large.render("VS", True, BLACK)
        vs_rect = vs_text.get_rect(center=(WINDOW_WIDTH // 2 + offset_x, WINDOW_HEIGHT // 3 + offset_y))
        self.screen.blit(vs_text, vs_rect)
        
        # Display result with appropriate color
        result_color = GREEN if self.result == "You win!" else RED if self.result == "You lose!" else GOLD
        result_text = self.font_large.render(self.result, True, result_color)
        result_rect = result_text.get_rect(center=(WINDOW_WIDTH // 2 + offset_x, WINDOW_HEIGHT // 2 + offset_y))
        
        # Add glow effect to result text
        glow_surf = pygame.Surface((result_text.get_width() + 20, result_text.get_height() + 20), pygame.SRCALPHA)
        pygame.draw.rect(glow_surf, (*result_color, 100), glow_surf.get_rect(), border_radius=10)
        glow_rect = glow_surf.get_rect(center=result_rect.center)
        self.screen.blit(glow_surf, glow_rect)
        self.screen.blit(result_text, result_rect)
        
        # Draw buttons
        self.play_again_button.draw(self.screen, self.font_small)
        self.menu_button.draw(self.screen, self.font_small)
    
    def determine_winner(self):
        if self.player_choice == self.computer_choice:
            self.result = "It's a tie!"
            self.add_animation(self.result, GOLD, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        elif (self.player_choice == "Rock" and self.computer_choice == "Scissors") or \
             (self.player_choice == "Paper" and self.computer_choice == "Rock") or \
             (self.player_choice == "Scissors" and self.computer_choice == "Paper"):
            self.result = "You win!"
            self.add_animation(self.result, GREEN, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        else:
            self.result = "You lose!"
            self.add_animation(self.result, RED, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

if __name__ == "__main__":
    game = Game()
    game.run()
