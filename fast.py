import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from tools import search_product_info_by_company
from typing import Dict, Any, Optional

# 创建 FastAPI 应用
app = FastAPI(
    title="产品信息搜索 API",
    description="提供公司产品信息搜索功能的 API 服务",
    version="1.0.0"
)

# 定义请求模型
class CompanySearchRequest(BaseModel):
    company: str
    key: Optional[str] = "sk-1bfa2fde025242658999421bfe6d10d8"

# 定义响应模型
class SearchResponse(BaseModel):
    results: Dict[str, Any]

@app.post("/api/search_product_info_by_company", response_model=Dict[str, Any], tags=["搜索"])
async def search_product_info_api(request: CompanySearchRequest):
    """
    通过公司名称搜索近三年的产品信息
    
    此 API 调用博查 AI 接口来获取指定公司近三年的具体产品信息，并返回搜索结果
    
    - **company**: 公司名称
    - **key**: 博查 API 密钥 (可选)
    """
    try:
        # 调用原始函数
        result = search_product_info_by_company(request.company, request.key)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"搜索失败: {str(e)}")

# 根路由，提供 API 基本信息
@app.get("/")
async def root():
    return {
        "message": "产品信息搜索 API",
        "endpoints": {
            "搜索公司产品信息": "/api/search_product_info_by_company"
        },
        "documentation": "/docs"
    }

# 启动服务
if __name__ == "__main__":
    print("启动 FastAPI 服务...")
    uvicorn.run(app, host="0.0.0.0", port=8000)