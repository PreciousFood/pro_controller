# Pro Controller

## Overview
The `pro_controller.py` script is designed to interface with and control a Nintendo Switch Pro Controller. This script provides functionalities to read inputs from the controller, process them, and execute corresponding actions.


I primarily designed this to control my raspberry pi, so the default initialisation is geared towards that usecase, but it can be used in other contexts as well. 

## Features

- **Input Handling**: Reads inputs from various buttons, joysticks, and triggers.
- **Action Mapping**: Maps controller inputs to specific actions or commands.
- **Cross-Platform**: Compatible with multiple operating systems. So far only tested on Windows 11, but should work on anything that pygame-ce works on. 

> **Note**: This script does NOT handle connecting the controller to your system. It assumes that the controller has already been connected and recognized by your operating system.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/PreciousFood/pro_controller.git
    ```

2. Install the required dependencies (pygame-ce):
    ```sh
    pip install -r requirements.txt
    ```

    or

    ```sh
    pip install pygame-ce
    ```


    > **Note**: If you have the original `pygame` installed, you must uninstall it or use a virtual environment (venv) to avoid dependency clashes with `pygame-ce`.

## Usage

1. Import the `pro_controller` module and initialize the controller:
    ```python
    from pro_controller import ProController

    # Initialize the controller (index is 0 if it is the only controller)
    controller = ProController(index=0)
    ```

2. Start reading inputs and processing actions:
    ```python
    while True:
        controller.update()
        # Add your custom logic here to handle controller inputs
    ```

## Contributing and Licens

This project is open source and contributions are welcome. Feel free to fork the repository, make improvements, and submit pull requests. You can also use the code as you see fit under the terms of the MIT License.

For more details, please refer to the `LICENSE` file in the repository.

## Contact

For any questions or support, please open an issue on the GitHub repository.