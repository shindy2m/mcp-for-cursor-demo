#!/usr/bin/env python3
"""
MCP Demo Server

A simple MCP server implementation demonstrating:
- System information retrieval
- Calculator functionality
- Proper MCP protocol handling
"""

import asyncio
import logging
import sys
import os
import platform
import psutil
from typing import Any, Sequence
from pathlib import Path

from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions, Server
from mcp.types import (
    Resource,
    Tool,
    TextContent,
    ImageContent,
    EmbeddedResource,
    LoggingLevel
)
import mcp.types as types
from pydantic import AnyUrl
import mcp.server.stdio

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mcp-demo")

# Initialize the server
server = Server("mcp-demo")

@server.list_tools()
async def handle_list_tools() -> list[Tool]:
    """
    List available tools.
    Each tool specifies its arguments using JSON Schema validation.
    """
    return [
        Tool(
            name="calculator",
            description="Perform basic arithmetic calculations",
            inputSchema={
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": ["add", "subtract", "multiply", "divide"],
                        "description": "The arithmetic operation to perform"
                    },
                    "a": {
                        "type": "number",
                        "description": "First number"
                    },
                    "b": {
                        "type": "number",
                        "description": "Second number"
                    }
                },
                "required": ["operation", "a", "b"]
            }
        ),
        Tool(
            name="get_system_info",
            description="Get system information including OS, CPU, memory, and disk usage",
            inputSchema={
                "type": "object",
                "properties": {
                    "detailed": {
                        "type": "boolean",
                        "description": "Whether to include detailed system information",
                        "default": False
                    }
                }
            }
        ),

    ]

@server.call_tool()
async def handle_call_tool(name: str, arguments: dict | None) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """
    Handle tool execution requests.
    """
    if arguments is None:
        arguments = {}
        
    try:
        if name == "calculator":
            return await handle_calculator(arguments)
        elif name == "get_system_info":
            return await handle_system_info(arguments)

        else:
            raise ValueError(f"Unknown tool: {name}")
            
    except Exception as e:
        logger.error(f"Error in tool {name}: {str(e)}")
        return [types.TextContent(type="text", text=f"Error: {str(e)}")]

async def handle_calculator(arguments: dict) -> list[types.TextContent]:
    """Handle calculator operations."""
    operation = arguments.get("operation")
    a = arguments.get("a")
    b = arguments.get("b")
    
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            return [types.TextContent(type="text", text="Error: Division by zero")]
        result = a / b
    else:
        return [types.TextContent(type="text", text=f"Error: Unknown operation {operation}")]
    
    return [types.TextContent(
        type="text", 
        text=f"Result: {a} {operation} {b} = {result}"
    )]

async def handle_system_info(arguments: dict) -> list[types.TextContent]:
    """Handle system information requests."""
    detailed = arguments.get("detailed", False)
    
    try:
        # Basic system information
        info = {
            "System": platform.system(),
            "Release": platform.release(),
            "Version": platform.version(),
            "Machine": platform.machine(),
            "Processor": platform.processor(),
            "Python Version": platform.python_version(),
        }
        
        # Memory information
        memory = psutil.virtual_memory()
        info["Memory Total"] = f"{memory.total / (1024**3):.2f} GB"
        info["Memory Available"] = f"{memory.available / (1024**3):.2f} GB"
        info["Memory Used"] = f"{memory.percent}%"
        
        # CPU information
        info["CPU Count"] = psutil.cpu_count()
        info["CPU Usage"] = f"{psutil.cpu_percent(interval=1)}%"
        
        # Disk information
        disk = psutil.disk_usage('/')
        info["Disk Total"] = f"{disk.total / (1024**3):.2f} GB"
        info["Disk Free"] = f"{disk.free / (1024**3):.2f} GB"
        info["Disk Used"] = f"{(disk.used / disk.total) * 100:.1f}%"
        
        if detailed:
            # Additional detailed information
            info["Boot Time"] = psutil.boot_time()
            info["Load Average"] = os.getloadavg() if hasattr(os, 'getloadavg') else "N/A"
            
        # Format the output
        result = "System Information:\n"
        result += "=" * 50 + "\n"
        for key, value in info.items():
            result += f"{key}: {value}\n"
            
        return [types.TextContent(type="text", text=result)]
        
    except Exception as e:
        return [types.TextContent(type="text", text=f"Error retrieving system info: {str(e)}")]



async def main():
    """Main entry point for the server."""
    # Running with stdio transport
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="mcp-demo",
                server_version="1.0.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )

if __name__ == "__main__":
    asyncio.run(main()) 