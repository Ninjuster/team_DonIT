from fpdf import FPDF

async def generate_talon(code, ops, purpose, date):
    pdf = FPDF(orientation='P', unit='mm', format=(80, 105))

    pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
    pdf.add_font('DejaVu', 'B', 'DejaVuSans-Bold.ttf', uni=True)

    pdf.add_page()

    logo_width = 20
    logo_x = (80 - logo_width) / 2
    pdf.image('donbass_logo.jpg', x=logo_x, y=10, w=logo_width)

    pdf.set_y(35) 
    pdf.set_font('DejaVu', 'B', 16)
    pdf.cell(0, 5, 'Талон', align='C')

    pdf.set_y(40)
    pdf.set_font('DejaVu', '', 12)
    pdf.cell(0, 5, '-----------------------------', align='C')

    pdf.set_y(43)  
    pdf.set_font('DejaVu', 'B', 20) 
    pdf.cell(0, 10, code, align='C')

    pdf.set_y(50)  
    pdf.set_font('DejaVu', '', 12)
    pdf.cell(0, 5, '-----------------------------', align='C')

    pdf.set_y(55)
    pdf.set_font('DejaVu', '', 12)
    pdf.cell(0, 5, purpose, align='C')

    pdf.set_y(60) 
    pdf.cell(0, 5, '-----------------------------', align='C')

    pdf.set_y(65)
    pdf.cell(0, 5, ops, align='C')

    pdf.set_y(70) 
    pdf.cell(0, 5, '-----------------------------', align='C')


    pdf.set_y(75) 
    pdf.set_font('DejaVu', '', 9)
    pdf.cell(0, 5, f'Действителен: {date}', align='C')

    pdf.output('talon.pdf')

# generate_talon('P-1267', 'ОПС Донецк 8', 'Оплата коммунальных услуг', '19.10.2024')
