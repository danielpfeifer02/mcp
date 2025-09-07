from server import mcp

import tools.csv_tools
import tools.parquet_tools
import tools.data_tools

# Entry point to run the server
if __name__ == "__main__":
    mcp.run()