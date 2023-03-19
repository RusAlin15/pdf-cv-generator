import pandas as pd


class CvChapter():
    def __init__(self, name: str, subchapters=[]):
        self.__name = name
        self.__subchapters = subchapters.copy()

    @property
    def subchapters(self):
        return self.__subchapters

    @property
    def name(self):
        return self.__name

    @subchapters.setter
    def add_subchapter(self, subchapter):
        self.__subchapters.append(subchapter)

    def __repr__(self):
        return f"Name: {self.__name} ; Subchapters: {self.__subchapters}"


class SubCvChapter():
    def __init__(self, name: str, titles: list, subtitles=[], details=[]):
        self.__name = name
        self.__titles = titles
        self.__subtitles = subtitles.copy()
        self.__details = details.copy()

    @property
    def print_titles(self):
        txt = ""
        for title in self.__titles:
            txt = txt + str(title) + "\n"
        return txt

    @property
    def print_subtitles(self):
        txt = ""
        for subtitle in self.__subtitles:
            txt = txt + str(subtitle) + "\n"
        return txt

    @property
    def name(self):
        return self.__name

    @property
    def titles(self):
        return self.__titles

    @property
    def subtitles(self):
        return self.__subtitles

    @property
    def details(self):
        return self.__details

    def __repr__(self):
        return f"Subchapters -> {self.__name} ; Title: {self.__titles} ; Subtitles:" \
               f" {self.__subtitles} ; " \
               f"Details" \
               f" {self.__details}"


def load_cv_from_csv(cv_path) -> dict:
    df = pd.read_csv(cv_path)
    cv_informations = {}
    for index, row in df.iterrows():
        chapter_name = row["Chapter-name"]
        subchapter_name = row["SubChapter-name"]
        subchapter_titles = row["Titles"]
        subchapter_subtitles = row["Subtitles"] if not pd.isna(row["Subtitles"]) else None
        subchapter_details = row["Details"] if not pd.isna(row["Details"]) else None

        if chapter_name not in cv_informations.keys():
            new = CvChapter(chapter_name)
            cv_informations[chapter_name] = new

        try:
            titles = subchapter_titles.split(';')
        except AttributeError:
            titles = []
        try:
            subtitles = subchapter_subtitles.split(';')
        except AttributeError:
            subtitles = []
        try:
            details = subchapter_details.split(';')
        except AttributeError:
            details = []
            
        sub_chapter = SubCvChapter(subchapter_name, titles, subtitles,
                                   details)
        cv_informations[chapter_name].add_subchapter = sub_chapter
    return cv_informations
