# SQUARES.PY

## Functions

    make_move(x, y) => Moves AI square  Randomly .

    make_move_2_rect() Calculates the green square direction vector and normalizes it to move the AI square in the direction of the green square .

    get_distance(x, y) Calculates the distance between AI square and green square .

## Summuray Of The Code

    The code is a game that includes a rectangle
    that can move and walls that surround it. An
    AI-controlled square tries to reach the green
    square while avoiding the walls.The AI square's
    movement is determined by a function that takes
    into account the current position of the square
    and the location of the green square.
    The AI square can move up, down, left, right,
    but cannot pass through the walls.

    The code uses the Pygame library to create the
    game and the Numpy library to generate random
    numbers. The game loop continues until the user
    closes the window. The AI-controlled square's
    movements are determined by a function that
    either makes random moves or calculates the
    direction vector towards the target rectangle
    and moves the AI-controlled square towards it.
    The distance between the AI-controlled square
    and the green square is calculated, and the
    distance values are added to a list for
    graphing purposes.
