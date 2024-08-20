from django.core.management.base import BaseCommand
from PyPDF2 import PdfReader, PdfWriter
import os

class Command(BaseCommand):
    help = 'Copy the PDF content to a new PDF'

    def handle(self, *args, **kwargs):
        input_pdf_path = "ruta/a/tu/Manual de Usuario-proyecto dental (1).pdf"
        output_pdf_path = "ruta/a/tu/Manual_de_Usuario_Ardecors.pdf"

        reader = PdfReader(input_pdf_path)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        with open(output_pdf_path, "wb") as output_pdf:
            writer.write(output_pdf)

        self.stdout.write(self.style.SUCCESS('Successfully copied the PDF content'))

        