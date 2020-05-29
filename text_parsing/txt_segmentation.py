import os

## prepare list of files for segmentation
path = os.getcwd() + "/texts/"
ls = os.listdir(path)
ls.sort()
macFile = ".DS_Store"
print(ls)
if macFile in ls:
    ls.pop(0)

## segment files
for file in ls:
    filename = file + '_rework.txt'
    filepath = 'texts/' + filename
    orig_filepath = 'texts/' + file
    final = open(filepath, 'w+')
    with open(orig_filepath, 'r') as cogsci:
        sentences = cogsci.readlines()
        for i in range(0, len(sentences)):
            sentences[i] = sentences[i].replace('\n', '') # remove newlines
            sentences[i] = sentences[i].replace('-', '') # remove hyphens
            if '.' in sentences[i]:
                sentences[i] = sentences[i].replace('.', '.\n')
                final.write(sentences[i])
                pass
            else:
                final.write(sentences[i])
            if i % 1000 == 0:
                print('read {0} lines'.format(i))
    final.close()
