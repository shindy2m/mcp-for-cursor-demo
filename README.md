# MCP Demo Application

A simple demonstration MCP (Model Context Protocol) server implementation using the official MCP SDK.

## Features

- **Calculator Tool**: Perform basic arithmetic operations (add, subtract, multiply, divide)
- **System Information**: Get detailed system information including CPU, memory, and disk usage

- **Standard MCP Protocol**: Full compliance with MCP protocol standards
- **Cursor IDE Integration**: Easy connection from Cursor IDE

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd mcp-demo
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Alternatively, install as a package:
```bash
pip install -e .
```

## Usage

### Running the Server

Run the MCP server directly:
```bash
python src/server.py
```

### Cursor IDE Integration

1. Copy the configuration to your Cursor settings:
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

2. Restart Cursor IDE
3. The MCP server tools will be available in your coding session

### Available Tools

#### Calculator
Perform basic arithmetic calculations:
- **Operations**: add, subtract, multiply, divide
- **Parameters**: 
  - `operation` (string): The arithmetic operation
  - `a` (number): First number
  - `b` (number): Second number

Example usage:
```
Use the calculator to add 15 and 27
```

#### System Information
Get detailed system information:
- **Parameters**:
  - `detailed` (boolean, optional): Include detailed system information

Example usage:
```
Get system information with detailed stats
```



## Development

### Project Structure
```
mcp-demo/
├── src/
│   ├── __init__.py
│   └── server.py          # Main MCP server implementation
├── config.json            # Cursor IDE configuration
├── requirements.txt       # Python dependencies
├── setup.py              # Package installation
├── .env.example          # Environment variables example
└── README.md             # This documentation
```

### Configuration

Environment variables can be set in a `.env` file:
```bash
cp .env.example .env
```

### Extending the Server

To add new tools:

1. Add the tool definition to `handle_list_tools()`
2. Implement the tool handler function
3. Add the handler to `handle_call_tool()`

Example:
```python
Tool(
    name="my_new_tool",
    description="Description of what this tool does",
    inputSchema={
        "type": "object",
        "properties": {
            "param1": {
                "type": "string",
                "description": "Parameter description"
            }
        },
        "required": ["param1"]
    }
)
```

## Requirements

- Python 3.8+
- MCP SDK 1.0.0+
- psutil for system information
- See `requirements.txt` for full list

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Troubleshooting

### Common Issues

1. **Server won't start**: Check that all dependencies are installed
2. **Cursor can't connect**: Verify the configuration in Cursor settings
3. **Tools not working**: Check the server logs for error messages

### Logs

The server uses standard Python logging. Increase verbosity by setting:
```bash
export LOG_LEVEL=DEBUG
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

For more information about MCP protocol, visit: https://modelcontextprotocol.io/ 