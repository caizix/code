append_text = "\nThis is appended file."

my_file = open('my file.txt', 'a')
my_file.write(append_text)
my_file.close()
