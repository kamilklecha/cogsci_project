#### FINAL MODEL FOR COGSCI ARTICLES ####
## code mostly taken from ##
## https://medium.freecodecamp.org/how-to-get-started-with-word2vec-and-then-how-to-make-it-work-d0a2fca9dad3 ##

import gensim
import logging
import os

# creates logging messages' template for terminal to prompt during word2vec training
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

## reading single input
def read_input(input_file):

    logging.info("reading file {0}...this may take a while".format(input_file))
    with open(input_file, 'r') as f:
        doc = list()
        for i, line in enumerate(f):
            if (i % 10000 == 0):
                logging.info("read {0} articles".format(i))
            # do some pre-processing and return list of words for each review
            doc.append(gensim.utils.simple_preprocess(line))
        f.close()
        return doc

## reading multiple inputs
def read_inputs():

    doc = list()

    path = os.getcwd() + "/texts/"
    ls = os.listdir(path)
    ls.sort()
    macFile = ".DS_Store"
    if macFile in ls:
        ls.pop(0)

    for file in ls:
        filepath = " your input " + file
        with open(filepath, 'r') as input_file:
            logging.info("reading file {0}...this may take a while".format(input_file))
            for i, line in enumerate(input_file):
                if (i % 10000 == 0):
                    logging.info("read {0} articles".format(i))
                doc.append(gensim.utils.simple_preprocess(line))
            input_file.close()

    return doc

texts = read_inputs()

# creates model
model = gensim.models.Word2Vec(texts, size=300, window=15, min_count=10, workers=8) # parameters used in project as of May 2020

# trains model
model.train(texts, total_examples=len(texts), epochs=10)

# model = gensim.models.Word2Vec.load(" your model name") -> this loads created model, must be in the same folder as this program
