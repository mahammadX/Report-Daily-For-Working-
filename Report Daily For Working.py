from datetime import datetime

now = datetime.now()

dt_stw = now.strftime("%H:%M:%S")
dt_std = now.strftime("%d/%m/%Y")

# Python program to create
# a pdf file
 
 
from fpdf import FPDF
 
 
# save FPDF() class into a
# variable pdf
pdf = FPDF()
 
# Add a page
pdf.add_page()


# set style and size of font
# that you want in the pdf
#pdf.set_font("Arial", size = 15)
pdf.set_font("Arial", size = 12)
# create a cell
pdf.cell(10, 10,txt = "Your Company",
         ln = 1, align = 'L'
         )
pdf.cell(100, 10, txt = "Report about Working",
         ln = 1, align = 'L')
         
# add another cell
Site = input("Write The Name Site :  ")
pdf.cell(10, 10,txt = "A Report for Sites : " +Site,
         ln = 2, align = 'L'
         )
Date = dt_std       
pdf.cell(10, 10,txt = "Date : "+Date,
         ln = 2, align = 'L')
         
work = input( "Write Report Here  :   ")
 
         
pdf.cell(10, 10,txt = "Report : "+work,
         ln = 3, align = 'L'
         )
                 
        
# save the pdf with name .pdf

Namepdf= input("Input Name for pdf file  : ")
pdf.output(Namepdf+".pdf")  