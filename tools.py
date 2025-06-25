import requests
from typing import Dict, Any

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My App")

@mcp.tool()
def search_product_info_by_company(company: str, key: str = "sk-1bfa2fde025242658999421bfe6d10d8") -> Dict[str, Any]:
    """
    通过公司名称搜索近三年的产品信息
    
    此函数调用博查 AI API 来获取指定公司近三年的具体产品信息，并返回搜索结果
    调用格式：
    response = requests.post(
    api_url,   # "http://localhost:8000/api/工具函数名
    headers={"Content-Type": "application/json"},
    json={"company": company}
    )
    Args:
        company: 公司名称
        key: 博查 API 密钥，默认使用内置密钥
        
    Returns:
        Dict[str, Any]: API 返回的 JSON 响应，包含搜索结果
    """
    url = "https://api.bochaai.com/v1/web-search"
    headers = {
        'Authorization': f'Bearer {key}',
        'Content-Type': 'application/json'
    }
    payload = {
        "query": f"{company}近三年的具体产品信息",
        "summary": True,
        "count": 100
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

if __name__ == "__main__":
    # 添加调试输出
    # print("正在启动 FastMCP 服务...")
    
    # # 直接测试函数功能（可选）
    # company = "百利天恒医药有限公司"
    # result = search_product_info_by_company(company)
    # print("API 测试结果:", result)
    
    # 启动服务
    print("准备启动 HTTP 服务...")
    mcp.run()  # 明确指定参数

    # # 运行 FastMCP 服务
    # mcp.run()
    # 如何通过http请求调用这个函数？
    # 通过 FastMCP 提供的 HTTP 接口调用 search_product_info_by_company
    # 例如，使用 curl 命令行工具：
    # curl -X POST http://localhost:8000/tools/search_product_info_by_company \
    # -H "Content-Type: application/json" \
    # -d '{"company": "百利天恒医药有限公司"}'
# 或者使用 requests 库在 Python 中调用：
    # import requests
    # response = requests.post(
    #     "http://localhost:8000/tools/search_product_info_by_company",
    #     headers={"Content-Type": "application/json"},
    #     json={"company": "百利天恒医药有限公司"}
    # )