from data_capture import DataCapture
import readline
import shlex

print('Welcome to DataCapture.')
print('''The DataCapture object accepts numbers and returns an object for querying statistics about the inputs. 
Specifically, the returned object supports querying how many numbers in the collection are less than a value, greater than a value, or within a range.''')
print('To get help, enter `help`.')


help_text = '''

Commands:
add N, where N is a positive integer from 0 to 1000
build_stats, DataCapture prepare your data for your queries.
less N, where N is a positive integer from 0 to 1000. It will return values less than N.
greater N, where N is a positive integer from 0 to 1000. It will return values greater than N.
between N M, where N and M are integers from 0 to 1000. It will return values between N and M.

exit, exit the program

'''
data_capture = DataCapture()

while True:

    try:    
        cmd, *args = shlex.split(input('> '))

        if cmd=='exit':
            print('bye')
            break

        elif cmd=='help':
            print(help_text)

        elif cmd=='add':
            num = int(args[0])
            if len(args) > 1:
                print(f'add command only receives 1 argument. Adding only "{args[0]}"')
            data_capture.add(num)

        elif cmd=='build_stats':
            if data_capture.is_builded:
                print('your data is already builded')
                continue

            data_capture.build_stats()
            print('Data prepared!')

        elif cmd=='less':
            num = int(args[0])
            if args and len(args) > 1 :
                print(f'less command only receives 1 argument. Showing results only for "{args[0]}"')
            
            print(data_capture.less(num))

        elif cmd=='greater':
            num = int(args[0])
            if args and len(args) > 1 :
                print(f'greater command only receives 1 argument. Showing results only for "{args[0]}"')
            
            print(data_capture.greater(num))

        elif cmd=='between':
            num1, num2 = args
            num1 = int(num1)
            num2 = int(num2)
            if args and len(args) > 2 :
                print(f'between command only receives 2 arguments. Showing results only for "{args[0]}" "{args[1]}"')
            
            print(data_capture.between(num1, num2))


        elif cmd=='between':
            num1, num2 = args
            num1 = int(num1)
            num2 = int(num2)
            if args and len(args) > 2 :
                print(f'between command only receives 2 arguments. Showing results only for "{args[0]}" "{args[1]}"')
            
            print(data_capture.between(num1, num2))

        

        else:
            print(f'Unknown command: {cmd}')

    except Exception as e:
        print(e)

