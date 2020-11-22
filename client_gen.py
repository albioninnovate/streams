import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f'Send: {message!r}')
#    writer.write(message.encode())
    writer.write(message.to_bytes(32, byteorder="big", signed=True))

    # data = await reader.read(100)
    # print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()

data = 1641

#asyncio.run(tcp_echo_client('Hello World!'))
asyncio.run(tcp_echo_client(data))