from fastapi import FastAPI, HTTPException, status

app = FastAPI()

# Database Mock Data
PINCODES = {"411001": "Pune", "400001": "Mumbai", "110001": "Delhi"}

@app.get("/pincode/{code}")
async def lookup_pincode(code: str):
    # 1. Validation check
    if len(code) != 6 or not code.isdigit():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Pincode must be exactly 6 digits."
        )

    # 2. Check in database
    city = PINCODES.get(code)
    if not city:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pincode '{code}' not found in our records."
        )

    return {"pincode": code, "city": city}