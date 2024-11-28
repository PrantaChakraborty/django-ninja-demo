from ninja import Router


router = Router()

@router.get("/")
def get_app3(request):
    return {"message": "Hello, from app3!"}
