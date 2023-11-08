import csv
import fitz
import os

bordercolor = (0.88,0.88,0.88)
border_rect = fitz.Rect(40,140,550,350)
text_rect = fitz.Rect(50,150,550,350)
image_rect = fitz.Rect(350,360,550,450)
image_name = "jingming_sig.png"

red = (0.88,0,0)

with open('data.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        filename = row['filename']
        num = row['num']
        score = row['score']
        text = row['report']
        
        inputfile = "input/"+filename+".pdf"
        outputfile = "output/"+filename+".pdf"
        
        if not os.path.isfile(inputfile) or os.path.isfile(outputfile):
            continue
        
        doc = fitz.open(inputfile)  # new or existing PDF
        page = doc.new_page()  # new or existing page via doc[n]
        # p = fitz.Point(60, 130)  # start point of 1st line
        
        
        shape = page.new_shape()  # create Shape
        shape.draw_rect(border_rect)  # draw rectangles
        shape.finish(width = 0.3, color = bordercolor)
        
        shape.insert_textbox(fitz.Rect(250,100,350,200),"指导老师评语",fontname = "china-ss", fontsize=14, color = red)

        shape.insert_textbox(text_rect, text, fontname = "china-ss", color = (.1,.1,.1))
        
        shape.insert_textbox(fitz.Rect(50,360,550,450),"综合评定成绩："+score,fontname = "china-ss", fontsize=14, color = red)

        shape.commit()
        
        page.insert_image(image_rect,filename=image_name)

        doc.save(outputfile)
        
        