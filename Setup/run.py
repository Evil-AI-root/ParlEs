import nltk
import os


def main():
    try:
        # NLTK
        nltk.download('punkt')
        nltk.download('wordnet')
        # Spacy
        os.system(r"python -m spacy download es_core_news_sm")
        # spacy download es_core_news_md

    except:
        print("Installation failed!")


if __name__ == '__main__':
    main()
