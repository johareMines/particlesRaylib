import raylibpy as rl
from simulation import Simulation
import cProfile
import asyncio

# Initialization
screen_width = 2560
screen_height = 1440
rl.init_window(screen_width, screen_height, "Hello Raylib!")

# Set frame rate
rl.set_target_fps(60)


rl._ToggleFullscreen()

# Main game loop
while not rl.window_should_close():  # Detect window close button or ESC key
    # Start drawing
    rl.begin_drawing()
    rl.clear_background(rl.RAYWHITE)
    
    # Draw some text
    rl.draw_text("Welcome to Raylib with Python!", 190, 200, 20, rl.LIGHTGRAY)
    
    
    rl.draw_ring((400, 300), 2, 4, 0, 360, 32, rl.BLACK)  # Stroke
    rl.draw_circle(400, 300, 3, rl.BLUE)                  # Fill
    
    rl.draw_ring((400, 500), 5, 8, 0, 360, 64, rl.BLACK)  # Stroke
    rl.draw_circle(400, 500, 6, rl.BLUE)                  # Fill

    # End drawing
    rl.end_drawing()

# De-Initialization
rl.close_window()

############

async def run_simulation():
    simulation = Simulation.get_instance()
    await simulation.run()

if __name__ == "__main__":
    # Initialize the profiler
    profiler = cProfile.Profile()

    # Start the profiler
    profiler.enable()

    # Run the async function
    asyncio.run(run_simulation())

    # Stop the profiler
    profiler.disable()

    # # Save and print stats
    # profiler.dump_stats("funcStats")
    # p = pstats.Stats("funcStats")
    # p.sort_stats("cumulative").print_stats(100)