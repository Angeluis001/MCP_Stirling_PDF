from mcp.server.fastmcp import FastMCP
import httpx
import os

mcp = FastMCP()

@mcp.tool()
async def convert_file_to_pdf(self, file_path: str):
    """
    Converts a file to PDF by sending it to the specified API endpoint,
    and returns the path to the resulting PDF.
    """
    url = "http://wristirlingv3.eastus.azurecontainer.io:8080/api/v1/convert/file/pdf"

    file_name = os.path.basename(file_path)
    base_name = os.path.splitext(file_name)[0]
    output_pdf_path = f"{base_name}.pdf"

    async with httpx.AsyncClient() as client:
        with open(file_path, 'rb') as f:
            files = {
                'fileInput': (file_name, f, 'application/octet-stream')
            }
            response = await client.post(url, files=files)

    if response.status_code == 200:
        # Save the PDF locally
        with open(output_pdf_path, 'wb') as pdf_file:
            pdf_file.write(response.content)
        return {
            "message": "PDF generated successfully",
            "output_path": os.path.abspath(output_pdf_path)
        }
    else:
        return {
            "error": f"Failed to convert file. Status: {response.status_code}",
            "details": response.text
        }

if __name__ == "__main__":
    mcp.run()
