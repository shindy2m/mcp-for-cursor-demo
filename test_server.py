#!/usr/bin/env python3
"""
Test script for MCP Demo Server
"""

import asyncio
import sys
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from server import handle_list_tools, handle_calculator, handle_system_info

async def test_tools():
    """Test all tools functionality"""
    print("Testing MCP Demo Server Tools")
    print("=" * 40)
    
    # Test list tools
    print("\n1. Testing tool listing:")
    tools = await handle_list_tools()
    for tool in tools:
        print(f"   - {tool.name}: {tool.description}")
    
    # Test calculator
    print("\n2. Testing calculator:")
    calc_result = await handle_calculator({
        "operation": "add",
        "a": 15,
        "b": 27
    })
    print(f"   Calculator result: {calc_result[0].text}")
    
    # Test division by zero
    div_zero = await handle_calculator({
        "operation": "divide", 
        "a": 10,
        "b": 0
    })
    print(f"   Division by zero: {div_zero[0].text}")
    
    # Test system info
    print("\n3. Testing system information:")
    sys_info = await handle_system_info({"detailed": False})
    print("   System info retrieved successfully")
    print(f"   First few lines: {sys_info[0].text[:200]}...")
    

    
    print("\n" + "=" * 40)
    print("All tests completed successfully!")

if __name__ == "__main__":
    asyncio.run(test_tools()) 