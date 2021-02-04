from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphqlapp.models import ProductModel
import graphene

class Products(DjangoObjectType):
    class Meta:
        model = ProductModel
        filter_fields = ['id', 'Segment', 'Country']
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    prodinfo = relay.Node.Field(Products)
    all_prodinfo = DjangoFilterConnectionField(Products)

    def resolve_prodinfo(self, info):
        return ProductModel.objects.all()

schema = graphene.Schema(query=Query)