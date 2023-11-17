## Original Requirements
The boss has requested the creation of a command line interface (CLI) snake game.

## Product Goals
```python
[
    "Create a CLI snake game that is easy to play and understand",
    "Ensure the game is compatible with various operating systems",
    "Implement a scoring system to enhance the game experience"
]
```

## User Stories
```python
[
    "As a user, I want to be able to easily start the game from the command line",
    "As a user, I want to control the snake using my keyboard",
    "As a user, I want the game to keep track of my highest score",
    "As a user, I want the game to end when the snake hits the border or itself",
    "As a user, I want to be able to restart the game once it ends"
]
```

## Competitive Analysis
```python
[
    "Python Snake Game: A simple CLI snake game, but lacks a scoring system",
    "Java Snake Game: A GUI based snake game with scoring system, but not CLI",
    "C++ Snake Game: A CLI snake game with scoring system, but not cross-platform",
    "JavaScript Snake Game: A web-based snake game, but not CLI",
    "Rust Snake Game: A CLI snake game, but lacks a scoring system"
]
```

## Competitive Quadrant Chart
```mermaid
quadrantChart
    title Reach and engagement of campaigns
    x-axis Low Reach --> High Reach
    y-axis Low Engagement --> High Engagement
    quadrant-1 We should expand
    quadrant-2 Need to promote
    quadrant-3 Re-evaluate
    quadrant-4 May be improved
    "Python Snake Game": [0.3, 0.6]
    "Java Snake Game": [0.45, 0.23]
    "C++ Snake Game": [0.57, 0.69]
    "JavaScript Snake Game": [0.78, 0.34]
    "Rust Snake Game": [0.40, 0.34]
    "Our Target Product": [0.5, 0.8]
```

## Requirement Analysis
The product should be a CLI based snake game that is easy to play and understand. It should be compatible with various operating systems and include a scoring system to enhance the game experience. The game should end when the snake hits the border or itself and allow the user to restart the game once it ends.

## Requirement Pool
```python
[
    ("Implement snake movement and control with keyboard", "P0"),
    ("Implement game rules (game ends when snake hits border or itself)", "P0"),
    ("Implement scoring system", "P0"),
    ("Ensure compatibility with various operating systems", "P1"),
    ("Implement game restart option", "P2")
]
```

## UI Design draft
The game will be a CLI application. It will display the game board with the snake and the food. The snake will be represented by a line of characters, and the food by a single character. The score will be displayed at the top of the game board. The game will use simple keyboard controls: up, down, left, right to control the snake.

## Anything UNCLEAR
There are no unclear points.