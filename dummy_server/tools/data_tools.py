from server import mcp
from utils.file_reader import read_csv_data
@mcp.tool()
def read_csv_client_data() -> str:
    """
    Read a CSV file and return the client data.
    This includes the client's name, email, and signup date.
    Args:
        None
    Returns:
        A string describing the file's contents.
    """
    return read_csv_data("sample.csv")