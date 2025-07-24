# MCP for Cursor Demo

This is a simple MCP (Model Context Protocol) server that runs locally and communicates over standard input/output (stdio). 
It provides two demonstration tools: 
  - a calculator 
  - a system information retriever

The server is intended for local use only and is designed to be integrated with the Cursor IDE via its MCP support. 
No network communication is used; all interactions happen through stdio between Cursor and the Python process.


## Quick Start

1. Install dependencies:
```bash
pip install -r config/requirements.txt
```

2. Add to Cursor settings:
 - Go Settings / Tools & Integrations → MCP Tools. 
 - Click on "Add a Custom MCP Server"
 - Paste the following JSON into the MCP server configuration field:
```json
{
  "mcpServers": {
    "mcp-demo": {
      "command": "python",
      "args": ["src/server.py"],
      "env": {}
    }
  }
}
```

## Available MCP Tools

- **calculator**: Basic arithmetic (add, subtract, multiply, divide)
- **get_system_info**: System information (CPU, memory, disk)

## Usage from Cursor AI Chat
- Write following in ai chat
  - show me system info
  - 14 plus 56
