import mammoth
from markdownify import markdownify as md
import argparse
import os


def docx_to_html(docx_path):
    try:
        with open(docx_path, "rb") as docx_file:
            result = mammoth.convert_to_html(docx_file)
            html_content = result.value  # The generated HTML
            return html_content
    except Exception as e:
        print(f"Error converting DOCX to HTML: {e}")
        raise


def docx_to_markdown(docx_path, md_path, verbose=False):
    try:
        # Convert DOCX to HTML
        if verbose:
            print(f"Converting '{docx_path}' to HTML...")
        html_content = docx_to_html(docx_path)

        # Convert HTML to Markdown
        if verbose:
            print(f"Converting HTML to Markdown...")
        md_content = md(html_content)

        # Save the Markdown content to a file
        with open(md_path, "w", encoding="utf-8") as md_file:
            md_file.write(md_content)

        if verbose:
            print(f"Markdown file saved to '{md_path}'")
    except Exception as e:
        print(f"Error converting DOCX to Markdown: {e}")
        raise


def main():
    parser = argparse.ArgumentParser(description="Convert DOCX to Markdown.")
    parser.add_argument("docx_path", type=str, help="Path to the DOCX file")
    parser.add_argument("md_path", type=str, help="Path to save the Markdown file")
    parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity", default=True)

    args = parser.parse_args()

    # Validate DOCX file
    if not os.path.isfile(args.docx_path):
        print(f"Error: The file '{args.docx_path}' does not exist.")
        return

    if not args.docx_path.lower().endswith(".docx"):
        print(f"Error: The file '{args.docx_path}' is not a DOCX file.")
        return

    # Validate Markdown file extension
    if not args.md_path.lower().endswith(".md"):
        print(f"Error: The output file '{args.md_path}' does not have a .md extension.")
        return

    # Check if Markdown file already exists
    if os.path.isfile(args.md_path):
        overwrite = input(f"The file '{args.md_path}' already exists. Do you want to overwrite it? (y/n): ")
        if overwrite.lower() != "y":
            print("Operation cancelled.")
            return

    # Perform the conversion
    if args.verbose:
        print(f"Starting conversion of '{args.docx_path}' to '{args.md_path}'...")

    try:
        docx_to_markdown(args.docx_path, args.md_path, args.verbose)
        if args.verbose:
            print("Conversion completed successfully.")
    except Exception as e:
        print(f"Conversion failed: {e}")


if __name__ == "__main__":
    main()
