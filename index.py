import json
employee = {'name': 'John Doe', 'age': 30, 'position': 'Software Engineer'};
output = ('output.json');
# txt = ('Hello, this is a sample text file.\nThis file is used to demonstrate file operations in Python.\nHave a great day!\n');
try:
    with open (output, 'w') as file:
        json.dump(employee, file, indent=6);
        # file.write(txt);
        print("File created and text written successfully. 'myFile'");
except FileExistsError: 
    print("File already exists. 'myFile'");