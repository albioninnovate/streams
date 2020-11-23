import asyncio
import time

async def tcp_echo_client():
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    # print(f'Send: {message!r}')
    # writer.write(message.encode())

    data = await reader.read(100)
    print(f'Received: {data!r}')

    # print('Close the connection')
    # writer.close()

if __name__ == '__main__':
    while True:
        asyncio.run(tcp_echo_client())
        #time.sleep(1)