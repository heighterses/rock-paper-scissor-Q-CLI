# 🚀 Building a Rock Paper Scissors Game with Amazon Q CLI

In this blog post, I'll walk you through my journey of creating a fun Rock Paper Scissors game using Python and Pygame, with the assistance of Amazon Q CLI. I'll cover everything from setting up the development environment to implementing game mechanics and generating custom assets.

## 📋 Table of Contents
- [Installing Amazon Q CLI on macOS](#installing-amazon-q-cli-on-macos)
- [Setting Up the Project](#setting-up-the-project)
- [Designing the Game Structure](#designing-the-game-structure)
- [Implementing Game Mechanics](#implementing-game-mechanics)
- [Creating Custom Assets](#creating-custom-assets)
- [Adding Visual Effects](#adding-visual-effects)
- [Testing and Debugging](#testing-and-debugging)
- [Final Thoughts](#final-thoughts)

## 🔧 Installing Amazon Q CLI on macOS

Amazon Q CLI is a powerful tool that helped me throughout the development process. Here's how I installed it on my macOS:

1. First, I installed the AWS CLI using Homebrew:
   ```bash
   brew install awscli
   ```

2. Then I configured my AWS credentials:
   ```bash
   aws configure
   ```

3. Next, I installed the Amazon Q CLI:
   ```bash
   pip install amazon-q-cli
   ```

4. After installation, I verified it was working:
   ```bash
   q --version
   ```

5. I started using Amazon Q by running:
   ```bash
   q chat
   ```

Amazon Q CLI became my coding companion, helping me generate code snippets, debug issues, and even create project documentation.

## 🏗️ Setting Up the Project

I started by creating a new project directory and setting up a virtual environment:

```bash
mkdir rock-paper-scissor-Q-CLI
cd rock-paper-scissor-Q-CLI
python -m venv pygame_env
source pygame_env/bin/activate  # On macOS/Linux
```

Then I installed the necessary dependencies:

```bash
pip install pygame
```

I used Amazon Q CLI to help me structure the project:

```bash
q chat
```

In the chat, I asked:
```
Can you help me structure a Rock Paper Scissors game using Pygame?
```

Amazon Q provided me with a detailed project structure and initial code snippets that I could build upon.

## 🎮 Designing the Game Structure

Based on Amazon Q's suggestions, I designed the game with three main states:
1. **Menu State**: The main menu where players can start the game
2. **Playing State**: Where players select their move (Rock, Paper, or Scissors)
3. **Result State**: Displaying the outcome and allowing players to play again

I created the main game file structure with Amazon Q's help:

```bash
q chat
```

I asked:
```
Can you help me create a main.py file for my Rock Paper Scissors game with state management?
```

Amazon Q generated a comprehensive main.py file with classes for:
- Game state management
- Button creation and interaction
- Animated text effects
- Particle effects for visual feedback

## 🎯 Implementing Game Mechanics

For the core game mechanics, I needed to implement:
- Player choice selection
- Computer random choice generation
- Winner determination logic

I used Amazon Q to help me with this logic:

```bash
q chat
```

I asked:
```
How can I implement the winner determination logic for Rock Paper Scissors?
```

Amazon Q provided me with the following logic which I incorporated into my code:

```python
def determine_winner(self):
    if self.player_choice == self.computer_choice:
        self.result = "It's a tie!"
    elif (self.player_choice == "Rock" and self.computer_choice == "Scissors") or \
         (self.player_choice == "Paper" and self.computer_choice == "Rock") or \
         (self.player_choice == "Scissors" and self.computer_choice == "Paper"):
        self.result = "You win!"
    else:
        self.result = "You lose!"
```

## 🎨 Creating Custom Assets

I wanted custom assets for my game, so I created a script to generate them:

```bash
q chat
```

I asked:
```
Can you help me create a script to generate custom assets for Rock, Paper, and Scissors?
```

Amazon Q helped me create `generate_assets.py` and the necessary modules in the `assets/` directory:

```python
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
```

I ran the script to generate all the assets:

```bash
python generate_assets.py
```

## ✨ Adding Visual Effects

To make the game more engaging, I wanted to add visual effects like animations, particle effects, and screen shake. Amazon Q helped me implement these features:

```bash
q chat
```

I asked:
```
How can I add particle effects and screen shake to my Pygame game?
```

Amazon Q provided code for the `ParticleEffect` class and screen shake implementation, which I integrated into my game.

## 🐞 Testing and Debugging

During development, I encountered some bugs and performance issues. Amazon Q CLI was incredibly helpful for debugging:

```bash
q chat
```

I asked:
```
I'm getting this error in my Pygame code: [error message]. How can I fix it?
```

Amazon Q analyzed the error and provided solutions that I could implement right away.

## 📝 Creating Documentation

When it was time to document my project, Amazon Q CLI helped me create a comprehensive README.md file:

```bash
q chat
```

I asked:
```
Can you help me create a README.md for my Rock Paper Scissors game with beautiful and meaningful emojis?
```

Amazon Q generated a well-structured README with all the necessary information and emojis to make it visually appealing.

## 🎁 Final Thoughts

Building this Rock Paper Scissors game was a fun and educational experience. Amazon Q CLI significantly accelerated my development process by:

1. Providing code snippets and structure
2. Helping debug issues quickly
3. Generating documentation
4. Offering best practices and optimization tips

The final game includes:
- An intuitive user interface
- Smooth animations and transitions
- Visual feedback with particle effects
- Custom-generated game assets
- Multiple game states for a complete experience

If you're developing games or any software project, I highly recommend giving Amazon Q CLI a try. It's like having an expert developer by your side, ready to help whenever you need it.

To run the game yourself:

```bash
git clone https://github.com/yourusername/rock-paper-scissor-game.git
cd rock-paper-scissor-Q-CLI
pip install pygame
python main.py
```

Enjoy playing Rock Paper Scissors! 🎮
