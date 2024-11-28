from ninja import Router


router = Router()

@router.get("/")
def get_app1(request):
    return {"message": "Hello, from app1!"}
