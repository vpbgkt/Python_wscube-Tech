from PyPDF2 import PdfReader, PdfWriter

def rotate_pdf_pages(pdf_path, output_path, start_page, end_page=None, degrees=90, times=1):
    """
    Rotates specified pages of a PDF document by the given degrees a certain number of times.

    Args:
        pdf_path (str): The path to the input PDF file.
        output_path (str): The path to save the modified PDF file.
        start_page (int): The first page to rotate (1-indexed).
        end_page (int, optional): The last page to rotate (1-indexed, defaults to last page).
        degrees (int, optional): The degrees to rotate counter-clockwise (default is 90).
        times (int, optional): The number of times to repeat the rotation (default is 1).
    """
    with open(pdf_path, 'rb') as input_file, open(output_path, 'wb') as output_file:
        pdf_reader = PdfReader(input_file)
        pdf_writer = PdfWriter()

        # Determine the actual end page
        end_page = end_page if end_page else len(pdf_reader.pages)

        for page_num, page in enumerate(pdf_reader.pages, start=1):  # 1-indexed page numbers
            if start_page <= page_num <= end_page:
                # Rotate the page
                page.rotate(degrees * times)  
            pdf_writer.add_page(page)

        pdf_writer.write(output_file)

# Example usage
pdf_file = 'DBMS NOTES.pdf'   # Replace with your PDF file path
rotated_file = 'DBMS_NOTES_rotated_pdf.pdf' 

rotate_pdf_pages(pdf_file, rotated_file, start_page=4, degrees=90, times=3)
print("PDF pages rotated successfully!")
