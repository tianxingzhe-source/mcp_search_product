import requests
from typing import Dict, Any

from fastmcp import FastMCP

mcp = FastMCP()

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
    # 启动服务
    print("准备启动 HTTP 服务...")
    mcp.run(
        transport="http",
        host="115.236.46.156",
        port=39010,
        path="/api",
        log_level="debug",
    )