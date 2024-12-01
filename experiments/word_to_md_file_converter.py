from docx import Document

def docx_to_md(input_file, output_file):
    """
    Convert a Word document (.docx) to a Markdown file (.md).

    :param input_file: Path to the input .docx file.
    :param output_file: Path to the output .md file.
    """
    try:
        # Load the .docx file
        document = Document(input_file)
        
        md_lines = []  # List to hold markdown lines

        # Process each paragraph in the document
        for paragraph in document.paragraphs:
            text = paragraph.text.strip()
            
            if not text:  # Skip empty paragraphs
                continue

            # Check the style of the paragraph
            if paragraph.style.name.startswith('Heading'):
                # Extract heading level (e.g., 'Heading 1')
                level = int(paragraph.style.name.split()[1])
                md_lines.append(f"{'#' * level} {text}")
            elif paragraph.runs and any(run.bold for run in paragraph.runs):
                # Bold text
                md_lines.append(f"**{text}**")
            elif paragraph.runs and any(run.italic for run in paragraph.runs):
                # Italic text
                md_lines.append(f"*{text}*")
            else:
                # Regular text
                md_lines.append(text)

        # Write to the Markdown file
        with open(output_file, 'w', encoding='utf-8') as md_file:
            md_file.write('\n'.join(md_lines))

        print(f"Successfully converted '{input_file}' to '{output_file}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_docx = "example.docx"  # Replace with your Word file path
output_md = "example.md"     # Replace with your desired Markdown file path
docx_to_md(input_docx, output_md)
