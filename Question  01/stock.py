import asyncio
import websockets
import json
import csv

# WebSocket URL
SOCKET_URL = "wss://ws.coincap.io/prices?assets=bitcoin,ethereum,tether,binance-coin,solana,usd-coin"



async def write_to_csv(data, all_keys):
    """
    Write a batch of dynamically structured data to a CSV file.
    - Set the dynamic header.
    - Write in batches.
    """
    filename = "stock_data.csv"
    fieldnames = sorted(all_keys)

    # Write to CSV with dynamic headers
    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write header if the file is new
        if file.tell() == 0:
            writer.writeheader()

        # Write the rows
        for row in data:
            writer.writerow(row)

    print(f"Batch written to {filename}")



async def connect_and_receive_data():
    """
    Connect to WebSocket and receive data.
    1. Dynamically handle unpredictable data .
    2. Log and process data as per the data fields present there.
    3. Write data in batches to the file.
    """
    batch = []
    BATCH_SIZE = 10  

    # Tracking all the keys in the data to ensure dynamic header
    all_keys = set()

    while True:
        try:
            async with websockets.connect(SOCKET_URL) as websocket:
                print("Connected to WebSocket...")

                while True:
                    message = await websocket.recv()
                    data = json.loads(message)

                    # print raw data
                    print(f"Raw Data Received: {data}")

        
                    processed_data = {}

                    # adding the incoming data into the processed_data dictionary
                    processed_data.update(data)

                    # Update all_keys set , to track new keys
                    all_keys.update(processed_data.keys())

                    
                    print(f"Processed Data: {processed_data}")

                    batch.append(processed_data)

                    # Write batch to file when size is met
                    if len(batch) >= BATCH_SIZE:
                        await write_to_csv(batch, all_keys)
                        batch = []  # Clear batch after writing

        except websockets.exceptions.ConnectionClosedError as e:
            print(f"Connection closed: {e}. Reconnecting...")
            await asyncio.sleep(5) 


        except Exception as e:
            print(f"Error: {e}. Reconnecting...")
            await asyncio.sleep(5)


        finally:
            # Write the remaining data : if any
            if batch:
                print("Writing remaining batch to file...")
                await write_to_csv(batch, all_keys)
                print("Remaining data saved successfully.")


if __name__ == "__main__":
    try:
        asyncio.run(connect_and_receive_data())
    except KeyboardInterrupt:
        print("Shutting down...")
