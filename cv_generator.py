from cv_items import load_cv_from_csv
from datetime import datetime
from pdf import Custom_PDF


def main(photo_adr="resources/CV-Photo.png", csv_adr="resources/Rus-Alin-CV.csv"):
    cv = load_cv_from_csv(cv_path=csv_adr)
    name = cv['Personal Information'].subchapters[0].titles[0]
    year = datetime.now().year
    pdf = Custom_PDF()
    pdf.set_title(f"{name}-{year}.pdf")
    pdf.set_author("Automated Script by Alin")
    pdf.set_photo_adr(photo_adr)
    pdf.set_doc_title(name)
    pdf.add_page()

    for key, value in cv.items():
        pdf.chapter_body(value)

    pdf.output(f"{name}-{year}.pdf")


if __name__ == '__main__':
    main()
