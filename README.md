# DOCX to Markdown Converter

This project provides a command-line tool to convert DOCX files to Markdown format. It utilizes the `mammoth` library to convert DOCX files to HTML and `markdownify` to convert HTML to Markdown.

## Features

- Converts DOCX files to Markdown.
- Validates file existence and extensions.
- Optional verbosity for detailed output.
- Prompts user for confirmation before overwriting existing Markdown files.

## Requirements

- Python 3.x
- `mammoth` library
- `markdownify` library

You can install the required libraries using pip:

```sh
pip install mammoth markdownify
```

## Installation

To install the `docx2md` command-line tool, clone the repository and use `pip` to install it:

```sh
git clone https://github.com/ChatCRM/docx2md.git
cd docx2md
pip install .
```

This will install the `docx2md` command globally on your system.

## Usage

Run the `docx2md` command from the command line with the following arguments:

```sh
docx2md path_to_docx_file path_to_markdown_file [-v]
```

### Arguments

- `path_to_docx_file`: Path to the DOCX file you want to convert.
- `path_to_markdown_file`: Path where the converted Markdown file will be saved.
- `-v`, `--verbose`: (Optional) Enable verbose output for detailed logging.

### Example

```sh
docx2md example.docx example.md -v
```

### Description

- The script checks if the specified DOCX file exists and has a `.docx` extension.
- It checks if the output file has a `.md` extension.
- If the output file already exists, it prompts the user for confirmation before overwriting it.
- If the verbose flag is set, the script provides detailed output about the conversion process.

## Error Handling

The script handles errors gracefully, providing informative messages in case of issues such as:

- The DOCX file does not exist.
- The specified DOCX file is not in the correct format.
- The output file does not have the correct extension.
- Errors during the conversion process.

## Example Output

```sh
Starting conversion of 'example.docx' to 'example.md'...
Converting 'example.docx' to HTML...
Converting HTML to Markdown...
Markdown file saved to 'example.md'
Conversion completed successfully.
```

## Contributing

We welcome contributions to the DOCX to Markdown Converter project. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
