import re
import string
import glob
import os


ARTICLE_DOI = "S0032063312002437"
FILENAMETXT = f"./SimpleText/SimpleText_test/{ARTICLE_DOI}.txt"
TXTFILEFOLDER = "./SimpleText/SimpleText_test/"

class STMCorpus:
    def __init__(self):
        self.text = self.load_txt_files()
        #self.preprocess_data()

    def load_txt_files(self):
        """
        Load all available articles in txt format from the specified folder,
        and contatenate to one string.
        :return: self.text will raw data
        """
        txt_files = glob.glob(os.path.join(TXTFILEFOLDER, '*.txt'))

        text = ''

        for file in txt_files:
            with open(file, 'r', encoding='utf-8') as f:
                text += f.read()

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


