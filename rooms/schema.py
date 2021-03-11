import graphene
from graphene_django import DjangoObjectType
from rooms.models import Room


class RoomType(DjangoObjectType):
    class Meta:
        model = Room

class RoomListResponse(graphene.ObjectType):
    arr = graphene.List(RoomType)
    total = graphene.Int()
    maxpage = graphene.Int()

class Query(object):
    rooms = graphene.Field(RoomListResponse, page=graphene.Int())

    def resolve_rooms(self, info, page=1):
        magic = 5
        start_page, end_page = (page - 1) * magic, page * magic
        rooms = Room.objects.all()[start_page:end_page]

        total = Room.objects.count()
        maxpage = total // magic if total % magic == 0 else (total // magic) + 1
        return RoomListResponse(arr=rooms,total=total, maxpage=maxpage)