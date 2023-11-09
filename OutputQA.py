import json

def outputJSONFile(filename, message):

    with open(filename, 'w') as output_file:
        json.dump(message, output_file)