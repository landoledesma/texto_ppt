import streamlit as st
import openai
import pptx
from  pptx.util import Inches, Pt
import os 
from dotenv import load_dotenv

# format options
TITLE_FONT_SIZE = Pt(30)
