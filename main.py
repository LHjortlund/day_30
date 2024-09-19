#file not found
# with open("a_file.txt") as file:
#     file.read()
try:
    file = open("a_file.txt")
    a_dictionary = {"key" : "value"}
    print(a_dictionary[blablabla])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")

#keyerror
# a_dictionary = {"Apple", "Banana", "Orange"}
# value = a_dictionary["non_existing_key"]

#indexerror
# fruit_list = ["apple", "banana", "orange"]
# fruit = fruit_list[3]

#typeerror
# text = "abc"
# print(text + 5)