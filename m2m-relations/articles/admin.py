from .models import Article, Tag, Scope
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class TagInlineFormset(BaseInlineFormSet):
    def clean(self):
        a=0
        for form in self.forms:
            if form.cleaned_data['is_main']== True:
                a=+1
            if a>1:
                raise ValidationError('Тут всегда ошибка')
        return super().clean()

class TagInline(admin.TabularInline):
    model = Tag
    formset = TagInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagInline]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass


