# MCP Stirling PDF Conversion Server

This repository contains the MCP Stirling server, which connects to an API from Stirling to convert files to PDF.

## Features
- Converts files to PDF using an external API.
- Built with FastMCP for efficient server management.

## Requirements
- Python 3.8 or higher
- `httpx` library

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Angeluis001/MCP_Stirling_PDF.git
   ```

2. Navigate to the project directory:
   ```bash
   cd MCP_Stirling_PDF
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the server:
```bash
python server.py
```

## License
This project is licensed under the MIT License.
