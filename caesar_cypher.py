alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

plaintext_input = input("Enter a String to Encrypt: ")
input_length = len(plaintext_input)
shift_input = int(input("Enter the key value:"))
print(input_length)
output = ""

for i in range(input_length):
    character = plaintext_input[i]
    location_of_string = alphabets.find(character)
    #print(location_of_string)
    new_location = (location_of_string + shift_input) % 26

    #below if the easy way of doing the above line
    # but it will not work for every case.
    # if new_location >= 26:
    #     new_location = new_location -26

    output = output + alphabets[new_location]

print("Ecrypted String: " + output)
