# Nau Microbiome

MicroPython Framework for ESP32 (UART Version). This framework allows to control an ESP32 microcontroller via UART commands. It supports motor control, scenario execution, and extensibility for additional hardware and commands.

---

## Table of Contents
1. [Overview](#overview)
2. [How It Works](#how-it-works)
3. [Classes](#classes)
   - [MotorDriver](#motordriver)
   - [ScenarioCommand](#scenariocommand)
   - [DemoScenario](#demoscenario)
4. [Usage](#usage)
5. [Extending the Framework](#extending-the-framework)
6. [Example](#example)

---

## Overview

The framework consists of:
- **Motor Control**: A `MotorDriver` class to control 2-channel motors using PWM.
- **Command System**: A `ScenarioCommand` class to parse and execute UART commands.
- **Scenarios**: Predefined sequences of actions (e.g., motor movements) that can be triggered by commands.
- **UART Communication**: A simple protocol for sending commands and receiving responses.

---

## How It Works

1. **UART Communication**:
   - The ESP32 listens for commands via UART (115200 baud).
   - Commands are text-based and follow the format: `COMMAND_TYPE PARAM1 PARAM2 ...`
   - Example: `SCENARIO demo_scenario`

2. **Command Parsing**:
   - The `ScenarioCommand` class parses incoming commands.
   - If the command is valid, it executes the corresponding action.

3. **Scenario Execution**:
   - Scenarios are Python classes with a `run()` method.
   - When a scenario is triggered, its `run()` method executes a sequence of actions (e.g., motor movements).

4. **Motor Control**:
   - The `MotorDriver` class controls motors using PWM for speed and direction.

---

## Classes

### MotorDriver
- **Location**: `devices/motor_driver.py`
- **Description**: Controls a 2-channel motor driver using PWM for speed and digital pins for direction.
- **Methods**:
  - `clockwise(speed=100)`: Rotates the motor clockwise at the specified speed (0-100%).
  - `counterclockwise(speed=100)`: Rotates the motor counterclockwise at the specified speed.
  - `stop()`: Stops the motor.
  - `set_speed(speed)`: Sets the motor speed (0-100%).
  - `get_status()`: Returns the current speed and direction.

### ScenarioCommand
- **Location**: `commands/scenario_command.py`
- **Description**: Parses and executes UART commands.
- **Methods**:
  - `__init__(text)`: Parses the command text.
  - `execute()`: Executes the command and returns a response.
- **Supported Commands**:
  - `SCENARIO <name>`: Executes a scenario with the specified name.

### DemoScenario
- **Location**: `scenarios/demo_scenario.py`
- **Description**: A sample scenario that demonstrates motor control.
- **Methods**:
  - `run()`: Executes a sequence of motor movements.

---

## Usage

1. **Upload Code**:
   - Upload the `devices/`, `commands/`, `scenarios/`, and `main.py` files to your ESP32.

2. **Connect via UART**:
   - Use a serial terminal (e.g., Arduino Serial Monitor, `screen`, or `pyserial`) to connect to the ESP32 at 115200 baud.

3. **Send Commands**:
   - Send a command like `SCENARIO demo_scenario` to execute the demo scenario.

4. **Observe Output**:
   - The ESP32 will respond with status messages (e.g., `OK: Executed demo_scenario` or `ERROR: ...`).

---

## Extending the Framework

1. **Add New Scenarios**:
   - Create a new Python file in the `scenarios/` folder.
   - Define a class with a `run()` method.
   - Example:
     ```python
     class NewScenario:
         def __init__(self):
             self.motor = MotorDriver(enable_pin=12, in1_pin=14, in2_pin=27)
         
         def run(self):
             self.motor.clockwise(50)
             time.sleep(2)
             self.motor.stop()
     ```

2. **Add New Commands**:
   - Modify the `ScenarioCommand` class to support additional commands.
   - Example:
     ```python
     if cmd.startswith("MOTOR"):
         return self._handle_motor_command(cmd)
     ```

3. **Add New Devices**:
   - Create new classes in the `devices/` folder for additional hardware (e.g., sensors, LEDs).

---

## Example

### Demo Scenario Execution
1. Send command: `SCENARIO demo_scenario`
2. The ESP32 will:
   - Rotate the motor clockwise at 50% speed for 2 seconds.
   - Stop the motor for 1 second.
   - Rotate the motor counterclockwise at 75% speed for 2 seconds.
   - Stop the motor.
3. Response: `OK: Executed demo_scenario`

### Error Handling
- Invalid command: `ERROR: Invalid command format. Use: SCENARIO <name>`
- Missing scenario: `ERROR: Module not found`

---

## Folder Structure
```
root/
├── devices/
│   └── motor_driver.py
├── commands/
│   └── scenario_command.py
├── scenarios/
│   └── demo_scenario.py
└── main.py
```

---

## Dependencies
- MicroPython firmware for ESP32
- Python 3.x (for testing on PC)
- `pyserial` (optional, for testing on PC)

---

## License
This project is open-source and available under the MIT License. 