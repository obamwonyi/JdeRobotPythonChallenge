import sys
import argparse
from app.implementation_with_matplotlib import brownian_motion_matplotlib


def main():
    parser = argparse.ArgumentParser(description='Modified Brownian Motion Visualization')
    parser.add_argument('--arena-size', type=float, default=10.0,
                        help='Size of the square arena (default: 10.0)')
    parser.add_argument('--frames', type=int, default=500,
                        help='Number of frames for the animation (default: 500)')
    parser.add_argument('--steps-per-frame', type=int, default=5,
                        help='Simulation steps per animation frame (default: 5)')
    parser.add_argument('--interval', type=int, default=50,
                        help='Interval between frames in milliseconds (default: 50)')

    args = parser.parse_args()

    brownian_motion_matplotlib(
        arena_size=args.arena_size,
        max_frames=args.frames,
        steps_per_frame=args.steps_per_frame,
        interval=args.interval
    )


if __name__ == "__main__":
    main()