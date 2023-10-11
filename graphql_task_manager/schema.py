import graphene
import task_manager.schema


class Query(task_manager.schema.Query, graphene.ObjectType):
    pass


class Mutation(task_manager.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
