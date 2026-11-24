from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()

# 1. Dependency Function (API Key Validator)
def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != "secret-chai-123":
        raise HTTPException(status_code=401, detail="Invalid API Key!")
    return x_api_key

# 2. Dependency Function (Common Pagination Query Params)
def common_pagination_params(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

# 3. Inject Dependencies in Endpoints
@app.get("/admin/chai-stats", dependencies=[Depends(verify_api_key)])
async def get_chai_stats(pagination: dict = Depends(common_pagination_params)):
    return {
        "status": "Authorized",
        "skip": pagination["skip"],
        "limit": pagination["limit"],
        "total_sales": 1500
    }