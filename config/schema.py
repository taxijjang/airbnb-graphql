import graphene
from graphene_django import DjangoObjectType
from rooms.models import Room

class RoomType(DjangoObjectType):
    class Meta:
        model = Room

class Query(graphene.ObjectType):
    hello = graphene.String()
    taxijjang = graphene.String()
    rooms = graphene.List(RoomType)

    def resolve_hello(self, info):
        print(info)
        return "Hello"

    def resolve_taxijjang(self, info):
        return "택시짱"

    def resolve_rooms(self, info):
        return Room.objects.all()

class Mutaion:
    pass

schema = graphene.Schema(query=Query)