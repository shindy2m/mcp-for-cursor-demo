# MCP Demo Application Specification

## Overview
Simple demo application implementing an MCP (Model Context Protocol) server using the standard SDK to ensure correct MCP implementation.

## Requirements

### Core Functionality
- Implement MCP server using official SDK
- Provide basic tools/resources for demonstration
- Enable connection from Cursor IDE
- Follow MCP protocol standards

### Technical Requirements
- Implement application in Python
- Use standard MCP SDK for implementation
- Support JSON-RPC communication
- Implement required MCP methods (initialize, tools/list, tools/call, etc.)
- Handle authentication and connection management

### Demo Features
- Basic system information retrieval
- Calculator functionality

### Integration
- Connectable from Cursor IDE
- Proper error handling and logging
- Configuration via environment variables or config file
- Health check endpoint

### Development Goals
- Clean, maintainable code structure
- Comprehensive documentation
- Easy setup and deployment
- Extensible architecture for adding new tools

## Success Criteria
- MCP server starts successfully
- Cursor can establish connection
- All demo tools work correctly
- Protocol compliance verified
- Clear documentation for usage
