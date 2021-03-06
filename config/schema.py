import graphene

class Query(graphene.ObjectType):
    pass

class Mutaion:
    pass

schema = graphene.Schema(query=Query)