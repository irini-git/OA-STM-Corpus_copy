import re
import string

ARTICLE_DOI = "S0032063312002437"
FILENAMETXT = f"./SimpleText/SimpleText_test/{ARTICLE_DOI}.txt"


class STMCorpus:
    def __init__(self):
        self.text = self.load_text()
        self.preprocess_data()

    def load_text(self):
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

        with open(FILENAMETXT, "r", encoding='utf-8') as file:
            text = file.read()

        return text

    def preprocess_data(self):
        """
        Preprocess data :
        remove punctuation, low case, remove special characters, remove multiple whitespaces
        :return: cleaned text
        """
        # Remove punctuation and change to a low case
        self.text = self.text.lower().translate(str.maketrans('', '', string.punctuation))

        # Replace new line with whitespace
        self.text = re.sub("\\n+", " ", self.text)

        # Remove special characters
        self.text = re.sub("[►∼±×•]", "", self.text)

        # Remove degrees, °n or °
        self.text = re.sub("°(n)?", "", self.text)

        # Remove numbers
        self.text = re.sub("\\d+", "", self.text)

        # Remove multiple whitespaces
        # Might be a result of "of Fig. 1 with" -> "of Fig  with"
        self.text = re.sub("\\s+", " ", self.text)


