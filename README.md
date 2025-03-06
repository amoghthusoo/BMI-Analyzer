# BMI Analyzer

BMI Analyzer is a Python-based application developed to calculate and analyze Body Mass Index (BMI). The application is built using KivyMD for the user interface and is compatible with Windows, macOS, Linux, and Android.

## Features

- Calculate BMI based on user input (weight and height).
- Display BMI status (Underweight, Healthy, Overweight, Obese).
- User-friendly interface with theme customization.
- Cross-platform compatibility (Windows, macOS, Linux, Android).

## Installation

### Prerequisites

- Python 3.x
- Kivy
- KivyMD

### Installation Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/amoghthusoo/BMI-Analyzer.git
   cd BMI-Analyzer
   ```

2. Install the required dependencies:

   ```bash
   pip install kivy kivymd
   ```

## Usage

1. Run the application:

   ```bash
   python main.py
   ```

2. For Windows, macOS, or Linux, ensure the `Windows_Mode` is set to `True` in the `main.py` file:

   ```python
   Windows_Mode = True
   ```

3. For Android, set the `Windows_Mode` to `False` before packaging:

   ```python
   Windows_Mode = False
   ```

## Application Structure

- `main.py`: Contains the main application code and methods bound to respective buttons to provide different functionalities.
- `ui_home.py`: Contains the UI layout code for the application.

## How It Works

- The user inputs their name, weight, and height.
- The `callback_calculate` method calculates the BMI and displays the status.
- The application uses `MDDialog` to show the BMI result and status.
- The theme of the application can be changed using the `callback_change_theme` method.

## Screenshots

![BMI Analyzer](screenshot.png)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- **Amogh Thusoo** - *Initial work* - [amoghthusoo](https://github.com/amoghthusoo)
