
import io
import time
import ast

def make_data():
    # generate some predictable data to be sent and received
    number = 1
    range = 10
    step = 1
    count = 0

    a_dict = {}

    while count <= 100:
        number = number + step

        index = str(number)
        print(number)

        a_dict[index] =  number

        inmemoryfile = io.StringIO(str(a_dict))

        if number >= range or number <= 0:
            step = step * -1
        time.sleep(0.01)
        count +=1

    return inmemoryfile

def read_file(file):
    content = file.read()
    b_dict = ast.literal_eval(content)  # extract the dictionary from the string received
    print(b_dict)
    # print('content : ', b_dict['reading'])
    return content

def main():
    inmemoryfile = make_data()
    return read_file(inmemoryfile)


if __name__ == '__main__':
    main()




