import keyboard
import random
import time
import os
import threading

# Game constants
WIDTH = 20
HEIGHT = 10

# Game elements
EMPTY = ' '
SNAKE_BODY = '█'
FOOD = '●'
BORDER = '█'

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Game state
snake = []
food = None
direction = RIGHT
next_direction = RIGHT
score = 0
game_over = False
game_paused = False

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_food():
    global food
    while True:
        x = random.randint(1, WIDTH - 2)
        y = random.randint(1, HEIGHT - 2)
        if (x, y) not in snake:
            food = (x, y)
            break

def draw_board():
    board = []
    
    # Top border
    board.append(BORDER * (WIDTH + 2))
    
    for y in range(HEIGHT):
        row = BORDER
        for x in range(WIDTH):
            if (x, y) in snake:
                row += SNAKE_BODY
            elif (x, y) == food:
                row += FOOD
            else:
                row += EMPTY
        row += BORDER
        board.append(row)
    
    # Bottom border
    board.append(BORDER * (WIDTH + 2))
    
    # Add score
    board.append(f"Score: {score}")
    
    if game_paused:
        board.append("PAUSED - Press SPACE to continue")
    
    return "\n".join(board)

def update():
    global snake, food, score, game_over, direction
    
    if game_over or game_paused:
        return
    
    # Update direction
    direction = next_direction
    
    # Calculate new head position
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])
    new_x, new_y = new_head
    
    # Check for collision with border
    if new_x < 0 or new_x >= WIDTH or new_y < 0 or new_y >= HEIGHT:
        game_over = True
        return
    
    # Check for collision with self (excluding tail if not eating food)
    if new_head in snake[:-1]:
        game_over = True
        return
    
    # Add new head
    snake.insert(0, new_head)
    
    # Check if eating food
    if new_head == food:
        score += 10
        generate_food()
    else:
        # Remove tail if not eating food
        snake.pop()

def handle_input():
    global next_direction, game_over, game_paused
    
    while True:
        if keyboard.is_pressed('up') and direction != DOWN:
            next_direction = UP
        elif keyboard.is_pressed('down') and direction != UP:
            next_direction = DOWN
        elif keyboard.is_pressed('left') and direction != RIGHT:
            next_direction = LEFT
        elif keyboard.is_pressed('right') and direction != LEFT:
            next_direction = RIGHT
        elif keyboard.is_pressed('p'):
            game_paused = not game_paused
            time.sleep(0.2)  # Debounce
        elif keyboard.is_pressed('r') and game_over:
            restart_game()
        elif keyboard.is_pressed('q'):
            os._exit(0)
        
        time.sleep(0.05)  # Reduce CPU usage

def restart_game():
    global snake, direction, next_direction, score, game_over, game_paused
    
    # Reset game state
    snake = [(WIDTH // 2, HEIGHT // 2)]
    direction = RIGHT
    next_direction = RIGHT
    score = 0
    game_over = False
    game_paused = False
    
    # Generate new food
    generate_food()

def show_instructions():
    clear_screen()
    print("SNAKE GAME INSTRUCTIONS")
    print("----------------------")
    print("Arrow keys: Move the snake")
    print("P: Pause/Resume game")
    print("R: Restart game (when game over)")
    print("Q: Quit game")
    print("\nCollect food to grow and earn points.")
    print("Avoid hitting walls or yourself!")
    print("\nPress any key to start...")
    keyboard.read_event()

def start_game():
    # Initialize game
    restart_game()
    
    # Show instructions
    show_instructions()
    
    # Start input thread
    input_thread = threading.Thread(target=handle_input)
    input_thread.daemon = True
    input_thread.start()
    
    # Main game loop
    while True:
        if not game_paused:
            update()
            
        clear_screen()
        print(draw_board())
        
        if game_over:
            print("GAME OVER!")
            print("Press R to restart or Q to quit")
        
        time.sleep(0.1)

if __name__ == "__main__":
    try:
        start_game()
    except KeyboardInterrupt:
        print("\nGame terminated by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        keyboard.unhook_all()

