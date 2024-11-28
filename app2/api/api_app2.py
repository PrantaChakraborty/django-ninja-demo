from ninja import Router


router = Router()

@router.get("/")
def get_app2(request):
    return {"message": "Hello, from app2!"}
