import numpy as np


def brownian_motion(arena_size=10.0, steps_per_frame=1):
    """
    Generate a modified Brownian motion that follows challenge requirements.
    Robot starts in center, moves straight, and only changes direction on wall collision.

    Parameters:
    -----------
    arena_size : float
        Size of the square arena (width and height)
    steps_per_frame : int
        Number of simulation steps to compute per animation frame

    Returns:
    --------
    init_func : function
        Initialization function for animation
    update_func : function
        Update function for animation that returns the position and direction of the robot
    """
    # State variables
    position = np.array([arena_size / 2, arena_size / 2])  # Start in the middle of the area

    direction = np.array([1.0, 0.0])  # Start moving right
    speed = 0.1  # Movement speed
    rotation_remaining = 0  # Counter for rotation when hitting a wall

    # Keep track of trajectory history
    trajectory = [position.copy()]

    def init():
        return []

    def update(_):
        # Accessing the variables in the parent scope.
        nonlocal position, direction, rotation_remaining, trajectory

        for _ in range(steps_per_frame):
            if rotation_remaining > 0:
                # Rotate the direction vector by a small amount
                theta = np.random.uniform(0.1, 0.3)  # Random small rotation angle between 0.1 and 0.3
                cos_theta = np.cos(theta)
                sin_theta = np.sin(theta)
                direction = np.array([
                    direction[0] * cos_theta - direction[1] * sin_theta,
                    direction[0] * sin_theta + direction[1] * cos_theta
                ])
                direction = direction / np.linalg.norm(direction)  # Normalize
                rotation_remaining -= 1
            else:
                # Move forward
                new_position = position + direction * speed

                # Check boundary collisions
                collision = False

                # Check x boundaries
                if new_position[0] < 0:
                    new_position[0] = 0
                    collision = True
                elif new_position[0] > arena_size:
                    new_position[0] = arena_size
                    collision = True

                # Check y boundaries
                if new_position[1] < 0:
                    new_position[1] = 0
                    collision = True
                elif new_position[1] > arena_size:
                    new_position[1] = arena_size
                    collision = True

                # Update position
                position = new_position

                # If collision occurred, start rotating for a random duration
                if collision:
                    rotation_remaining = np.random.randint(10, 30)

            # Add current position to trajectory
            trajectory.append(position.copy())

            # Limit trajectory length to prevent memory issues
            if len(trajectory) > 1000:
                trajectory.pop(0)

        return position, direction, np.array(trajectory)

    return init, update