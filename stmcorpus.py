import re
from nltk.tokenize import sent_tokenize

ARTICLE_DOI = "S0032063312002437"
FILENAMETXT = f"./SimpleText/SimpleText_test/{ARTICLE_DOI}.txt"

class STMCorpus:
    def __init__(self):
        self.data = self.load_data()

    def load_data(self):
        """
        Load STM article, from file testSetList.txt
        # S0022314X13001777	Mathematics
        # S0032063312002437	Astronomy
        # S0032386113009889	Materials_Science
        # S0167610513002729	Engineering
        # S0167739X13001349	Computer_Science
        # S016816561300552X	Biology
        # S1161030113001950	Agriculture
        # S1387700313001822	Chemistry
        # S1750583613004192	Earth_Science
        # S2213158213001253	Medicine
        # For more search on web https://www.sciencedirect.com/science/article/pii/S0022314X13001777
        :return: article text
        """

        with open(FILENAMETXT, "r") as file:
            data = file.read()

        print(data)

        # will print ATCAGTGGAAACCCAGTGCTAGAGGATGGAATGACCTTAAATCAGGGACGATATTAAACGGAA

    def preprocess_data(self, text):
        """
        Preprocess data :
        remove punctuation,
        low case,
        add special symbols in the beginning and at the end of each sentence
        :return: cleaned text
        """
        # Remove commas and change to a low case
        text = re.sub(r",", "", text.lower())

        # Remove multiple spaces
        text = re.sub("\\s+", " ", text)

        # Add special symbols in the beginning and at the end of the sentence
        special_symbol_beginning = '<s> '
        special_symbol_end = ' </s>'
        text = sent_tokenize(text.lower())

        # Train corpus has punctuation in the end
        text = [special_symbol_beginning + t[:-1] + special_symbol_end for t in text]

        return  text