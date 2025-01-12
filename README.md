# Aim Assist Script for Rounds

This script is an automated aim assist tool designed for the game "Rounds." It detects enemies on the screen based on specific color ranges and moves the mouse cursor to their location. The script supports dynamic switching between detecting red and blue-colored enemies.

## Features

- **Color-Based Enemy Detection**: Detects enemies using color filtering in HSV format.
- **Dynamic Color Switching**: Switch between red and blue detection using keyboard shortcuts.
- **Excluded Areas**: Avoids moving the mouse to pre-defined screen regions.
- **Fast Execution**: Optimized for quick screenshot analysis and cursor movement.

## Prerequisites

- Python 3.x
- Required Python Libraries:
  - `pyautogui`
  - `cv2` (OpenCV)
  - `numpy`
  - `keyboard`

Install the libraries using:
```bash
pip install -r requirements.txt
or run file
install.bat
```

## How to Use

1. **Run the Script**: Execute the script using Python.
   ```bash
   python main.py
   ```

2. **Switch Target Colors**:
   - Press `1` to target red enemies.
   - Press `2` to target blue enemies.

3. **Excluded Areas**:
   - The script avoids specific screen regions defined in `excluded_areas`.
   - You can customize these regions by modifying the `excluded_areas` list.

4. **Terminate the Script**:
   - Press `Ctrl + C` in the terminal to stop the script.

## Configuration

### Color Ranges
- Adjust the HSV color ranges for red and blue enemies in the following variables:
  - `lower_red` and `upper_red`
  - `lower_blue` and `upper_blue`
