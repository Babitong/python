# with open('nonexistent.txt','w') as file: file.write('hello eeworld')

# try:
#     with open ('nonexistent.txt','r') as file :
#         data = file.read()
#         print(data)
# except FileNotFoundError:
#     print('file not found. please check the name')

# finally:
#     file.close()


# WRITING AND UPDATING CONTENT IN A FILE

with open('main.txt','w') as file: file.write('first message\n')
try:
    with open('main.txt','a') as file:
        data = "new message"
        data = file.write(data)
except FileNotFoundError:
    print('file does not exist')


# USING USER NAME FILE AND HANDLING ERROR
file_name = str(input('enter file name  '))
try:
    with open(file_name,'r') as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print('file does not exist')



