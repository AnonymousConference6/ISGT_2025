from pyModbusTCP.client import ModbusClient
import time

# Server configuration
SERVER_HOST = "192.168.168.7"  # Replace with your server's IP if running remotely
SERVER_PORT = 502

# Register to reset
TARGET_REGISTER = 1  # Change this to the desired register number

def set_register_to_zero():
    """Continuously set the given Modbus register to 0 in an infinite loop."""
    client = ModbusClient(host=SERVER_HOST, port=SERVER_PORT, auto_open=True)
    try:
        while True:  # Infinite loop
            success = client.write_single_register(TARGET_REGISTER, 0)  # Set register to 0

            if success:
                print(f"Successfully set register {TARGET_REGISTER} to 0.")
            else:
                print(f"Failed to set register {TARGET_REGISTER} to 0.")

            #time.sleep(1)  # Delay before the next iteration

    except KeyboardInterrupt:
        print("\nProcess interrupted. Exiting gracefully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    set_register_to_zero()
