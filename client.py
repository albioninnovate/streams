import asyncio
import ast

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    b_dict = ast.literal_eval(data.decode())  # extract the dictionary from the string received
    print(b_dict)
    print(b_dict['2'])


    print('Close the connection')
    writer.close()

asyncio.run(tcp_echo_client('Hello World!'))