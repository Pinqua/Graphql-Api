from api.models import Category, Product
import graphene
from graphene_django import DjangoObjectType, DjangoListField



class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        field = "__all__"


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryInput(graphene.InputObjectType):
    id =graphene.ID()
    name = graphene.String()


class ProductInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    price=graphene.Int()
    description=graphene.String()
    category = graphene.Field(CategoryInput)
