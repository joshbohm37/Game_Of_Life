import ctypes
user32 = ctypes.windll.user32

#Screen parameters to be initialized on load
screen_w = user32.GetSystemMetrics(78)
screen_h = user32.GetSystemMetrics(79)

#Grid parameters static
grid_size = 50
grid_padding = 1

# Grid parameters to be initialized on load
cell_size = (screen_h//grid_size)//1.1
grid_width = ((grid_size - 1) * (cell_size + grid_padding)) + cell_size
global_center = (screen_w/3.5, screen_h/2)
grid_top_left = ((global_center[0] - (grid_width/2)), (global_center[1] - (grid_width/2)))