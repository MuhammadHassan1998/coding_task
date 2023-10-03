from django.contrib import admin
from .models import Book, Collaboration, Section, Subsection

admin.site.register(Book)
admin.site.register(Section)
admin.site.register(Subsection)
admin.site.register(Collaboration)
