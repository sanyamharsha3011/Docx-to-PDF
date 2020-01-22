import docx2txt
from fpdf import FPDF

#the following code will convert text into capitals and export into pdf file. Modify as per your needs

text = docx2txt.process("address...\\doc1.docx") #upload doc file
upper = text.upper()
file1 = open("address...\\myfile.txt","w")  #create a text file and write content in text file
file1.write(upper)
file1.close()

pdf = FPDF(format='letter', unit='in')
pdf.add_page()
pdf.set_font('Arial','', 16)
effective_page_width = pdf.w - 2*pdf.l_margin

with open("address...\\myfile.txt") as f:   #read text file
    lines = f.read().splitlines()

for i in lines:
    print(i)
    pdf.multi_cell(effective_page_width, 0.35, i)
    pdf.ln(0)
pdf.output('output_address\\tuto1.pdf','F')     #export to pdf file





























 
"""Long meaningless piece of text
loremipsum = Lorem ipsum dolor sit amet, vel ne quando dissentias. \
Ne his oporteat expetendis. Ei tantas explicari quo, sea vidit minimum \
menandri ea. His case errem dicam ex, mel eruditi tibique delicatissimi \
ut. At mea wisi dolorum contentiones, in malis vitae viderer mel.
 
Vis at dolores ocurreret splendide. Noster dolorum repudiare vis ei, te \
augue summo vis. An vim quas torquatos, electram posidonium eam ea, eros \
blandit ea vel. Reque summo assueverit an sit. Sed nibh conceptam cu, pro \
in graeci ancillae constituto, eam eu oratio soleat instructior. No deleniti \
quaerendum vim, assum saepe munere ea vis, te tale tempor sit. An sed debet \
ocurreret adversarium, ne enim docendi mandamus sea.
"""
 
"""
 
pdf.set_font('Times','B',10.0)
pdf.cell(1.0,0.0, 'Without multi_cell using effective page width:')
pdf.ln(0.25)
pdf.set_font('Times','',10.0)
# Cell is as wide as the effective page width
pdf.cell(effective_page_width, 0.0, loremipsum)
pdf.ln(0.5)
pdf.set_font('Times','B',10.0)
pdf.cell(1.0,0.0, 'Using multi_cell and effective page width:')
pdf.ln(0.25)
 
pdf.set_font('Times','',10.0)
# Cell is as wide as the effective page width
# and multi_cell requires declaring the height of the cell.
pdf.multi_cell(effective_page_width, 0.15, loremipsum)
pdf.ln(0.5)
 
# Cell half as wide as the effective page width
# and multi_cell requires declaring the height of the cell.
pdf.set_font('Times','B',10.0)
pdf.cell(1.0,0.0, 'Using multi_cell and half the effective page width:')
pdf.ln(0.25)
 
pdf.set_font('Times','',10.0)
pdf.multi_cell(effective_page_width/2, 0.15, loremipsum)
pdf.ln(0.5)
 
pdf.output('multi_cell.pdf','F')
"""
