import requests

# 设置API端点
api_url = "http://localhost:8000/api/search_product_info_by_company"

# 要测试的公司名称
company = "百利天恒医药有限公司"

# 发送请求
response = requests.post(
    api_url,
    headers={"Content-Type": "application/json"},
    json={"company": company}
)

print(response.json().get("data", "No data found").get("webPages", {}).get("value", []))