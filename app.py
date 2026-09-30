import html
import os
import sys
# Path fix
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "backend"))

import streamlit as st
import requests
from dotenv import load_dotenv

from services.document_service import (
    format_docx
)
from services.export_service import (
    format_pdf,
    format_txt
)
from utils.text_utils import (
    split_text
)