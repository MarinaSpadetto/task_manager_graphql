import graphene
from graphene_django.types import DjangoObjectType
from task_manager.models import Task


class TaskType(DjangoObjectType):
    class Meta:
        model = Task


class Query(graphene.ObjectType):
    all_tasks = graphene.List(TaskType)

    def resolve_all_tasks(self, info):
        return Task.objects.all()


class CreateTask(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()
    completed = graphene.Boolean()

    class Arguments:
        title = graphene.String()
        completed = graphene.Boolean()

    def mutate(self, info, title, completed):
        task = Task(title=title, completed=completed)
        task.save()

        return CreateTask(
            id=task.id,
            title=task.title,
            completed=task.completed,
        )


class Mutation(graphene.ObjectType):
    create_task = CreateTask.Field()
