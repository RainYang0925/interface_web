from django.contrib import admin
from interface_platform.models import *


@admin.register(Project, DirectoryTree, TestCase, TestCaseStep, Variable)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(ITStatement, ITBody, ITHeader)
class ITAdmin(admin.ModelAdmin):
    pass


@admin.register(ITLog, TestCaseLog)
class LogAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag, TagMap)
class TagsAdmin(admin.ModelAdmin):
    pass
