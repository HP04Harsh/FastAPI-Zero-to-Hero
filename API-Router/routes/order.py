from fastapi import APIRouter

# Create Router Instance with Prefix and Tags
router = APIRouter(prefix="/order", tags=["Orders Module"])

@router.get("/order")
async def get_all_orders():
    return [{"name": "Masala Chai"}, {"name": "Ginger Chai"}]