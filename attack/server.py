from pyModbusTCP.server import ModbusServer
import threading
import time
import random
import logging

# Configure logging
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.INFO)

# Server configuration
SERVER_HOST = "0.0.0.0"  # Listen on all interfaces
SERVER_PORT = 502        # Modbus default port

# Register addresses
PITCH_ANGLE_ADDR = 0     # Holding Register address for Pitch Angle
WIND_SPEED_ADDR = 1      # Holding Register address for Wind Speed

def update_wind_farm_values(server):
    """Continuously generate and update wind farm values in registers 0 and 1."""
    while True:
        # Simulate random values
        pitch_angle = random.uniform(0, 90)   # Pitch angle between 0 and 90 degrees
        wind_speed = random.uniform(0, 25)    # Wind speed between 0 and 25 m/s

        # Scale values to integers (Modbus registers store 16-bit integers)
        pitch_angle_scaled = int(pitch_angle * 100)  # Multiply by 100 for precision
        wind_speed_scaled = int(wind_speed * 100)

        # Update the registers
        server.data_bank.set_holding_registers(PITCH_ANGLE_ADDR, [pitch_angle_scaled])
        server.data_bank.set_holding_registers(WIND_SPEED_ADDR, [wind_speed_scaled])

        # Log the updated values
        logging.info(f"Updated values - Pitch Angle: {pitch_angle:.2f}°, Wind Speed: {wind_speed:.2f} m/s")

        # Wait before updating again
        time.sleep(10)

def run_server():
    """Initialize and start the Modbus server."""
    # Create an instance of ModbusServer
    server = ModbusServer(host=SERVER_HOST, port=SERVER_PORT, no_block=True)

    # Initialize the DataBank with default values
    server.data_bank.set_holding_registers(0, [0] * 100)  # Initialize 100 registers to zero

    # Start the server
    try:
        server.start()
        logging.info(f"Modbus server started on {SERVER_HOST}:{SERVER_PORT}")

        # Start the update thread for random values
        updater_thread = threading.Thread(target=update_wind_farm_values, args=(server,))
        updater_thread.daemon = True
        updater_thread.start()

        # Keep the main thread running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Server is shutting down...")
        server.stop()

if __name__ == "__main__":
    run_server()
