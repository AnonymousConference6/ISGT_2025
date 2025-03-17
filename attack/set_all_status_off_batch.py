# Batch writing (write_multiple_registers()) reduces network overhead by writing 125 registers at once, instead of writing one register per request.
# Faster execution compared to sending 65,536 individual write requests.
# Handles errors gracefully while ensuring all registers are updated.


from pyModbusTCP.client import ModbusClient

# Server configuration
SERVER_HOST = "192.168.168.7"  # Replace with your server's IP if running remotely
SERVER_PORT = 5020

# Register address range
MIN_STATUS_ADDR = 0
MAX_STATUS_ADDR = 65535
BATCH_SIZE = 125  # Max registers per Modbus write operation (Modbus TCP limit)

def set_all_status_off():
    """Function to set all status registers (0-65535) to 'Off' (0) using batch writes."""
    client = ModbusClient(host=SERVER_HOST, port=SERVER_PORT, auto_open=True)
    try:
        for addr in range(MIN_STATUS_ADDR, MAX_STATUS_ADDR + 1, BATCH_SIZE):
            # Create a batch of zero values
            zero_values = [0] * BATCH_SIZE
            success = client.write_multiple_registers(addr, zero_values)
            
            if success:
                print(f"Successfully set registers {addr} to {addr + BATCH_SIZE - 1} to 'Off'.")
            else:
                print(f"Failed to write registers {addr} to {addr + BATCH_SIZE - 1}.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    set_all_status_off()
