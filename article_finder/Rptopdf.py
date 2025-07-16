from fpdf import FPDF
 

class Rptopdf :
    def __init__(self, response):

        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_font('DejaVu', '', 'article_finder\\fonts\\dejavu-fonts-ttf-2.37\\ttf\\DejaVuSans.ttf', uni=True)
        pdf.set_font('DejaVu', '', 12)

        # Diviser le texte en lignes gérables
        for line in response.split('\n'):
            pdf.multi_cell(0, 10, line)
        pdf.output("test.pdf")

        