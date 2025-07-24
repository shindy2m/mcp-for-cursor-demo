# MCP Demo

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

3. Restart Cursor

## Available Tools

- **calculator**: Basic arithmetic (add, subtract, multiply, divide)
- **get_system_info**: System information (CPU, memory, disk)

## Usage
- Write following in ai chat
  - show me system info
  - 14 plus 56
