from tika import parser
import os

## scans each .pdf file into a joint .txt file
def scanner_joint():
    path = os.getcwd() + "/texts/" # takes files from 'texts' subfolder
    ls = os.listdir(path)
    ls.sort()
    macFile = ".DS_Store"
    print(ls)
    if macFile in ls:
        ls.pop(0)

    output_path = " your desired output " + "/final.txt"

    with open(output_path, "w+") as final:
        for filename in ls:
            print(filename)
            file_path = path + filename
            with open(file_path, "rb") as f:
                file_data = parser.from_file(f)
                print("almost there")
                text = file_data['content']
                final.write(text)

    final.close()

## scans each .pdf file into a separate .txt file
def scanner_separate():
    path = os.getcwd() + "/texts/" # takes files from 'texts' subfolder
    ls = os.listdir(path)
    ls.pop(0)

    for filename in ls:
        final_file = filename[:-4] + ".txt"
        output_path = " your desired output " + final_file
        with open(output_path, "w+") as final:
            print(filename)
            file_path = path + filename
            with open(file_path, "rb") as f:
                file_data = parser.from_file(f)
                text = file_data['content']
                print(type(file_data['content']))
                final.write(text)
        final.close()

## doesn't work, needs changes
def referenceCleaner():
    path = os.getcwd() + "/output/"
    ls = os.listdir(path)

    for filename in ls:
        output_path = " your desired output " + filename
        with open(output_path, "+r") as file:
            for line in file:
                for word in line.split():
                    if word == "References":
                        file.truncate()
                        break
        file.close()
