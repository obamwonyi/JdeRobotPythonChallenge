import matplotlib.pyplot as plt
import matplotlib.animation as animation
from .brownian_motion import brownian_motion


def brownian_motion_matplotlib(arena_size=10.0, max_frames=1000, steps_per_frame=1, interval=50):
    """
    Visualize modified Brownian motion in real-time using matplotlib animation.

    Parameters:
    -----------
    arena_size : float
        Size of the square arena (width and height)
    max_frames : int
        Maximum number of animation frames
    steps_per_frame : int
        Number of simulation steps per animation frame
    interval : int
        Interval between animation frames in milliseconds

    Returns:
    --------
    None
    """
    print("Running real-time matplotlib visualization of modified Brownian motion...")

    # Set up the figure and axis
    fig, ax = plt.figure(figsize=(8, 8)), plt.axes(xlim=(0, arena_size), ylim=(0, arena_size))
    ax.set_aspect('equal')
    ax.grid(True)
    ax.set_title('Modified Brownian Motion Simulation')

    # Create plot elements
    robot, = ax.plot([], [], 'bo', markersize=15)  # Robot (blue circle)
    direction_arrow, = ax.plot([], [], 'r-', linewidth=2)  # Direction vector (red arrow)
    trajectory, = ax.plot([], [], 'b-', alpha=0.3, linewidth=1)  # Trajectory path

    # Text for information display
    info_text = ax.text(0.02, 0.98, '', transform=ax.transAxes, verticalalignment='top')

    # Initialize brownian motion generator
    init_func, update_func = brownian_motion(arena_size, steps_per_frame)

    # Draw arena boundaries
    ax.plot([0, arena_size, arena_size, 0, 0], [0, 0, arena_size, arena_size, 0], 'k-', linewidth=2)

    # Frame counter
    frame_count = 0

    # Animation update function
    def animate(_):
        nonlocal frame_count
        frame_count += 1

        # Get updated position, direction and trajectory
        position, direction, traj = update_func(None)

        # Update robot position
        robot.set_data([position[0]], [position[1]])

        # Update direction arrow
        arrow_length = 0.5  # Length of the direction arrow
        arrow_start = position
        arrow_end = position + direction * arrow_length
        direction_arrow.set_data([arrow_start[0], arrow_end[0]], [arrow_start[1], arrow_end[1]])

        # Update trajectory
        trajectory.set_data(traj[:, 0], traj[:, 1])

        # Update info text
        info_text.set_text(
            f'Frame: {frame_count}/{max_frames}\n'
            f'Position: ({position[0]:.2f}, {position[1]:.2f})'
        )

        # Return all updated artists
        return robot, direction_arrow, trajectory, info_text

    # Create animation
    anim = animation.FuncAnimation(
        fig,
        animate,
        frames=max_frames,
        interval=interval, blit=True
    )

    # Display the animation
    plt.tight_layout()
    plt.show()

    return anim  # Return animation object to prevent garbage collection