from ninja import ModelSchema, Schema
from .models import Links

class LinksSchema(ModelSchema):
    
    class Meta: 
        model = Links
        fields = ['redirect_link', 'token', 'expiration_time', 'max_uniques_cliques']