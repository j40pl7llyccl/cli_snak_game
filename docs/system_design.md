## Implementation approach
We will use the curses library in Python, which is an open-source tool for creating text-based user interfaces and handling multi-window text I/O. This library will be used to create the game board and handle the keyboard inputs for controlling the snake. The snake will be represented as a list of coordinates, and its movement will be implemented by adding a new coordinate to the front of the list and removing the last one. The food will be represented as a single coordinate. The scoring system will be implemented by incrementing a score variable each time the snake eats the food.

## Python package name
```python
"cli_snake_game"
```

## File list
```python
[
    "main.py",
    "game.py",
    "snake.py",
    "food.py",
    "score.py"
]
```

## Data structures and interface definitions
```mermaid
classDiagram
    class Game{
        -int score
        -Snake snake
        -Food food
        +__init__(self)
        +run(self)
        +end_game(self)
    }
    class Snake{
        -List[Tuple[int, int]] body
        +__init__(self)
        +move(self, direction: str)
        +eat(self, food: Food)
        +check_collision(self)
    }
    class Food{
        -Tuple[int, int] position
        +__init__(self)
        +generate(self)
    }
    class Score{
        -int score
        +__init__(self)
        +increment(self)
    }
    Game "1" -- "1" Snake: has
    Game "1" -- "1" Food: has
    Game "1" -- "1" Score: has
```

## Program call flow
```mermaid
sequenceDiagram
    participant M as Main
    participant G as Game
    participant S as Snake
    participant F as Food
    participant Sc as Score
    M->>G: create game
    G->>S: create snake
    G->>F: create food
    G->>Sc: create score
    loop Game Loop
        G->>S: move snake
        S->>S: check collision
        alt collision detected
            G->>G: end game
        else no collision
            S->>F: eat food
            alt food eaten
                Sc->>Sc: increment score
                F->>F: generate new food
            end
        end
    end
```

## Anything UNCLEAR
The requirement is clear to me.