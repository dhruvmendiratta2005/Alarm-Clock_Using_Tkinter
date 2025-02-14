# Alarm Clock Application

A simple alarm clock application built using Python and Tkinter, allowing users to set multiple alarms, customize alarm sounds, and use the snooze function.

## Features
- **Set Multiple Alarms**: Users can set multiple alarms at different times.
- **Custom Alarm Sounds**: Select a `.wav` file as an alarm sound.
- **Snooze Functionality**: Snooze the alarm for a user-defined number of minutes.
- **User-Friendly Interface**: Simple and intuitive Tkinter-based GUI.

## Installation

### Prerequisites
Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Install Required Modules
Open the terminal and run:
```sh
pip install tk
```
(Tkinter comes pre-installed with most Python versions, but you can install it if needed.)

## Usage
1. Clone the repository:
```sh
git clone https://github.com/your-username/AlarmClock.git
cd AlarmClock
```
2. Run the application:
```sh
python alarm_clock.py
```
3. Enter the alarm time in **HH:MM** format.
4. Set a snooze duration (default is 5 minutes).
5. Choose a custom sound (optional).
6. Click "Set Alarm" to activate it.

## Converting to Executable
To create an `.exe` file for Windows:
```sh
pip install pyinstaller
pyinstaller --onefile --windowed --icon=alarm.ico alarm_clock.py
```
The executable file will be found in the `dist/` directory.

## License
This project is open-source and available under the MIT License.

## Contributing
Feel free to contribute by submitting issues or pull requests.

## Author
[Dhruv Mendiratta](https://github.com/your-username)

