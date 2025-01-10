from ninja import Router
from .schemas import LinksSchema

shortener_router = Router()

@shortener_router.post('create/')
def create(request, link_schema: LinksSchema):
    print(link_schema.dict())
    return {'status': 'OK'}