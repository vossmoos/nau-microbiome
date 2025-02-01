import machine
from commands.scenario_command import ScenarioCommand

# Initialize UART for command input
uart = machine.UART(0, 115200)
uart.init(115200, bits=8, parity=None, stop=1)

def process_command(raw_command):
    # Trim and uppercase the command
    cmd = raw_command.strip().upper()
    
    if cmd.startswith("SCENARIO"):
        return ScenarioCommand(cmd).execute()
    else:
        return "ERROR: Unknown command"

def main():
    while True:
        if uart.any():
            # Read command
            raw = uart.readline().decode().strip()
            
            # Process and get response
            response = process_command(raw)
            
            # Send back via UART
            uart.write(response + "\n")

if __name__ == "__main__":
    main()