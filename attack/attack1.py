from pyModbusTCP.client import ModbusClient
import time

# Server configuration
SERVER_HOST = "192.168.168.7"  # Replace with your server's IP if running remotely
SERVER_PORT = 502

# Register address range
MIN_STATUS_ADDR = 0
MAX_STATUS_ADDR = 65535
BATCH_SIZE = 123  # Max registers per Modbus write operation (Modbus TCP limit)

def set_all_registers_to_zero():
    """Continuously set all registers (0-65535) to 0 in an infinite loop."""
    client = ModbusClient(host=SERVER_HOST, port=SERVER_PORT, auto_open=True)
    try:
        while True:  # Infinite loop
            for addr in range(MIN_STATUS_ADDR, MAX_STATUS_ADDR + 1, BATCH_SIZE):
                # Calculate the number of registers to write (handle the last batch correctly)
                num_registers = min(BATCH_SIZE, MAX_STATUS_ADDR - addr + 1)

                # Create a batch of zero values
                zero_values = [0] * num_registers
                success = client.write_multiple_registers(addr, zero_values)
                # time.sleep(0.01)

                if success:
                    print(f"Successfully set registers {addr} to {addr + num_registers - 1} to 0.")
                else:
                    print(f"Failed to write registers {addr} to {addr + num_registers - 1}.")

            #print("All registers set to 0. Restarting the process in 5 seconds...")
            # time.sleep(1)  # Delay before the next iteration

    except KeyboardInterrupt:
        print("\nProcess interrupted. Exiting gracefully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    set_all_registers_to_zero()
