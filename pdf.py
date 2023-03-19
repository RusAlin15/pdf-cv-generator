from fpdf import FPDF
from cv_items import CvChapter


class Custom_PDF(FPDF):
    __DOC_TITLE = ""
    __PHOTO_ADR = ""

    def header(self) -> None:
        if self.page_no() == 1:
            self.set_font('Times', "B", size=24)
            self.set_text_color(0, 0, 60)
            self.cell(w=0, h=10, txt=self.__DOC_TITLE, align="R", new_x="LEFT", new_y="NEXT")
            self.image(self.__PHOTO_ADR, 145, 30, 40, 42)

    def set_doc_title(self, document_title):
        self.__DOC_TITLE = document_title

    def chapter_body(self, cv_chapter: CvChapter):
        self.set_line_width(0.6)
        self.set_font(family="Times", style="B", size=16)
        self.set_text_color(0, 0, 0)
        self.set_x(15)

        self.cell(w=0, h=10, txt=f"{cv_chapter.name}",
                  align="l",
                  new_x="LEFT",
                  new_y="NEXT"
                  )
        self.line(10, self.get_y() - 2, 200, self.get_y() - 2)

        for subchapter in cv_chapter.subchapters:
            if subchapter.name == "Name":
                continue

            self.set_font("Times", "B", size=13)
            self.set_text_color(0, 0, 60)
            self.set_x(20)
            stored_y = self.get_y()
            self.multi_cell(w=27, h=6,
                            txt=subchapter.name,
                            align="l",
                            new_x="LEFT",
                            )

            self.set_y(stored_y)
            self.set_x(50)
            for title in subchapter.titles:
                if subchapter.name in ("GitHub", "Web Site"):
                    self.set_font("Times", "B", size=15)
                self.multi_cell(w=0, h=6,
                                txt=title,
                                align="l",
                                new_x="LEFT",
                                new_y="NEXT"
                                )
            self.set_x(50)
            for subtitle in subchapter.subtitles:
                self.set_font("Times", "I", size=13)
                self.set_text_color(0, 0, 0)
                self.multi_cell(w=0, h=6,
                                txt=subtitle,
                                align="l",
                                new_x="LEFT",
                                new_y="NEXT"
                                )

            self.set_x(60)
            for detail in subchapter.details:
                self.set_font("Times", size=12)
                self.set_text_color(0, 0, 0)
                self.multi_cell(w=0, h=6,
                                txt=f"- {detail}",
                                align="l",
                                new_x="LEFT",
                                new_y="NEXT"
                                )
            if cv_chapter.name != "Personal Information":
                self.ln(4)

    def set_photo_adr(self, photo_adr):
        self.__PHOTO_ADR = photo_adr
