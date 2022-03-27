import graphene
from api.mutations import CreateCategory, CreateProduct, DeleteCategory, DeleteProduct, UpdateCategory, UpdateProduct
from api.type import CategoryType, ProductInput, ProductType
from .models import Category, Product


class Query(graphene.ObjectType):
    all_products = graphene.List(
        ProductType, first=graphene.Int(), skip=graphene.Int())
    product = graphene.Field(ProductType, product_id=graphene.Int())
    all_categories = graphene.List(
        CategoryType, first=graphene.Int(), skip=graphene.Int())
    category = graphene.Field(CategoryType, category_id=graphene.Int())

    def resolve_all_products(self, info, **kwargs):
        products = Product.objects.all()
        if 'skip' in kwargs:
            products = products[kwargs['skip']:]

        if 'first' in kwargs:
            products = products[:kwargs['first']]

        return products

    def resolve_all_categories(self, info, **kwargs):
        categories = Category.objects.all()
        if 'skip' in kwargs:
            categories = categories[kwargs['skip']:]

        if 'first' in kwargs:
            categories = categories[:kwargs['first']]

        return categories

    def resolve_product(self, info, product_id):
        return Product.objects.get(pk=product_id)

    def resolve_category(self, info, category_id):
        return Category.objects.get(pk=category_id)


class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
