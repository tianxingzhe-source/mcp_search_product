import asyncio
from fastmcp import Client

async def call_search_tool():
    print("正在连接到 FastMCP 服务...")

    async with Client("http://115.236.46.156:39010/api") as client:
        print("连接成功，正在调用工具函数...")
        
        # 调用 search_product_info_by_company 工具函数
        result = await client.call_tool(
            "search_product_info_by_company",  # 工具名称
            {
                "company": "百利天恒医药有限公司"  # 工具参数
            }
        )
        print(result)
if __name__ == "__main__":
    asyncio.run(call_search_tool())