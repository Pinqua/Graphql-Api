import graphene
from api.type import CategoryInput, CategoryType, ProductInput, ProductType
from .models import Category, Product


class CreateProduct(graphene.Mutation):
    '''
    Add new product to database
    '''

    class Arguments:
        product_data = ProductInput(required=True)

    product = graphene.Field(ProductType)

    @staticmethod
    def mutate(root, info, product_data=None):
        category, _ = Category.objects.get_or_create(
            **product_data["category"])
        product_instance = Product.objects.create(
            name=product_data.name,
            price=product_data.price,
            description=product_data.description,
            category=category
        )
        return CreateProduct(product=product_instance)


class UpdateProduct(graphene.Mutation):
    '''
    update a product by its ID
    '''

    class Arguments:
        product_data = ProductInput(required=True)

    product = graphene.Field(ProductType)

    @staticmethod
    def mutate(root, info, product_data=None):

        product_instance = Product.objects.get(pk=product_data.id)
        if product_instance:
            if "name" in product_data:
                product_instance.name = product_data.name
            if "description" in product_data:
                product_instance.description = product_data.description
            if "price" in product_data:
                product_instance.price = product_data.price
            if "category" in product_data:
                category, _ = Category.objects.get_or_create(
                    **product_data["category"])
                product_instance.category = category
            product_instance.save()

            return UpdateProduct(product=product_instance)
        return UpdateProduct(product=None)


class DeleteProduct(graphene.Mutation):
    '''
    Delete a product in the database
    '''

    class Arguments:
        id = graphene.ID()

    product = graphene.Field(ProductType)

    @staticmethod
    def mutate(root, info, id):
        product_instance = Product.objects.get(pk=id)
        product_instance.delete()

        return None


class CreateCategory(graphene.Mutation):
    '''
    Add new category to database
    '''

    class Arguments:
        category_data = CategoryInput(required=True)

    category = graphene.Field(CategoryType)

    @staticmethod
    def mutate(root, info, category_data=None):
        category_instance = Category.objects.create(name=category_data.name)
        return CreateCategory(category=category_instance)


class UpdateCategory(graphene.Mutation):
    '''
    update a category by its ID
    '''

    class Arguments:
        category_data = CategoryInput(required=True)

    category = graphene.Field(CategoryType)

    @staticmethod
    def mutate(root, info, category_data=None):

        category_instance = Category.objects.get(pk=category_data.id)
        if category_instance:
            if "name" in category_data:
                category_instance.name = category_data.name
            category_instance.save()

            return UpdateCategory(category=category_instance)
        return UpdateCategory(category=None)


class DeleteCategory(graphene.Mutation):
    '''
    Delete a category in the database
    '''

    class Arguments:
        id = graphene.ID()

    category = graphene.Field(CategoryType)

    @staticmethod
    def mutate(root, info, id):
        category_instance = Category.objects.get(pk=id)
        category_instance.delete()

        return None
