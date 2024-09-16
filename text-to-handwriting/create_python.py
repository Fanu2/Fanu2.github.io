from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def create_pdf():
    try:
        # Create a PDF file
        c = canvas.Canvas("example.pdf", pagesize=letter)
        width, height = letter  # Get the dimensions of the page

        # Add a paragraph to the PDF
        c.drawString(100, height - 100, "Hello, PDF!")

        # Save the PDF file
        c.save()
        print("PDF created successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")


# Run the PDF creation function
create_pdf()
