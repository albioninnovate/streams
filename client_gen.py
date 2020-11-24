import asyncio
import time

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f'Send: {message!r}')
#    writer.write(message.encode())
    writer.write(message.to_bytes(8, byteorder="big", signed=True))

    # data = await reader.read(100)
    # #print(f'Received: {data.decode()!r}')
    # print(f'Received: {data!r}')

    # print('Close the connection')
    # writer.close()


#asyncio.run(tcp_echo_client('Hello World!'))

if __name__ == '__main__':

    # generate some predictable data to be sent and received
    number = 1
    range = 100
    step = 1

    while True:
        number = number + step

        print(number)
        asyncio.run(tcp_echo_client(number))

        if number >= range or number <= 0:
            step = step * -1
        time.sleep(1)

