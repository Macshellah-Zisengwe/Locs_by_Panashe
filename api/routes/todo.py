from fastapi import APIRouter

locs_router = APIRouter(prefix="/api", tags = ["Newcustomer"])


@locs_router.get("/")
def all_locs():
    return "Not Implemented"

@locs_router.post("/")
def post_locs():
    return "Not Implemented"

@locs_router.put("/{key}")
def update_locs(key:int):
    return "not Implemented"

@locs_router.delete("/{key}")
def delete_locs(key:int):
    return "Not Implemented"