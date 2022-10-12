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
pdf.cell(10, 10, txt = "Report about Working",
         ln = 1, align = 'L')
pdf.cell(10, 25, txt = "",
         ln = 1, align = 'L')         
# add another cell
Site = input("Write The Name Site :  ")
pdf.cell(10, 10,txt = "A Report for Sites : " +Site,
         ln = 1, align = 'L'
         )
Date = dt_std       
pdf.cell(10,10,txt = "Date : "+Date,
         ln = 1, align = 'L')
         

print("Choose Type of Report :  Check Or Status  ")       
ch = input( "Write Answer Here  :   ")

if ch == "Check" :
     Check = input("Write Type of Checking : ")    
     pdf.cell(10,10,txt = "Checking : "+Check,
             ln = 1, align = 'L'
             )
     pro = input( "Write Problem Here  :   ")
 
         
     pdf.cell(10,10,txt = "Report : "+pro,
             ln = 1, align = 'L'
         ) 
     Chk2 = input( " ") 
         
     pdf.cell(10,10,txt = Chk2,ln = 1, align = 'L')
     Chk3 = input( " ") 
         
     pdf.cell(10,10,txt = Chk3,ln = 1, align = 'L')
     Chk4 = input( " ") 
         
     pdf.cell(10,10,txt = Chk4,ln = 1, align = 'L')

     print('Is There Other Problems ? : Yes or No' )
     x = input("Answer is  : ")
     if x == "Yes":
          Check2 = input( "Write Type Check Other Here  :   ") 
         
          pdf.cell(10,10,txt = "Checking : "+Check2,ln = 1, align = 'L')
                 
        
          pro2 = input( "Write Problem Here  :   ")
          pdf.cell(10,10,txt = "Problem : "+pro2,ln = 1, align = 'L')
                 
 
     else :
          pdf.cell(10,10,txt = "Not have Checking Other yet ",ln = 1, align = 'L')

else :

     ST = input( "Write Status Here  :   ")
 
         
     pdf.cell(10,10,txt = "Status : "+ST,
              ln = 1, align = 'L')

pdf.cell(10, 25, txt = "",
         ln = 1, align = 'L') 
pdf.cell(10, 25, txt = "",
         ln = 1, align = 'L') 
pdf.cell(10, 50,txt = "Programmer By Eng. Mahammad Qassem ",
         ln = 1, align = 'L'
         )         
# save the pdf with name .pdf

Namepdf= input("Input Name for pdf file  : ")
pdf.output(Namepdf+".pdf")  
