import streamlit as st
import openai
import pptx
from  pptx.util import Inches, Pt
import os 
from dotenv import load_dotenv

# format options
TITLE_FONT_SIZE = Pt(30)
SLIDE_FONT_SIZE = Pt(16)

def slide_title(topic):
    prompt = f"Genera 5 titulos de slides para el tema dado '{topic}'."
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 200
    )
    return response['choices'][0]['text'].split("\n")

def slide_content(slide_title):
    prompt = f"Genera contenido para eltitulo del slide '{slide_title}'."
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 500
    )
    return response['choices'][0]['text']

def create_presentation(topic,slide_titles,slide_contents):
    prs = pptx.Presentation()
    slide_layout = prs.slide_layout[1]

    title_slide = prs.slides.add_slide(prs.slide_layout[0])
    title_slide.shapes.title.text = topic 
    
    for slide_title,slide_content in zip(slide_titles,slide_contents):
        slide = prs.slides.add_slide(slide_layout)
        slide.shapes.title.text = slide_title 
        slide.sahpes.placeholder[1].text = slide_content

        slide.sahpes.title.text_frame.paragraphs[0].font.size = TITLE_FONT_SIZE
        for shape in slide.shapes:
            if shape.has_text_frame:
                text_frame = shape.text_frame
                for paragraph in text_frame.paragraph:
                    paragraph.font.size = SLIDE_FONT_SIZE
    prs.save(f"ppt/{topic}_presentacion.pptx")


    