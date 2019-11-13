from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
from import_export.widgets import ForeignKeyWidget
from import_export.fields import Field

# Register your models here.
from .models import Iom, Speciality, Subject

admin.site.site_header = 'IOM手册'
admin.site.site_title = 'IOM手册管理'

class IomResource(resources.ModelResource):
    class Meta:
        model = Iom
        exclude = ('subject',)

class SpecialityResource(resources.ModelResource):
    class Meta:
        model = Speciality

class SubjectResource(resources.ModelResource):
    speciality = Field(
        attribute='speciality',
        column_name='speciality',
        widget=ForeignKeyWidget(Speciality,'speciality')
    )
    speciality_Chn = Field()
    class Meta:
        model = Subject
        skip_unchanged= True
        report_skipped = True
        fields=('id','subject','subject_Chn','speciality','speciality_Chn')
        export_order = ('id','speciality','subject_Chn','speciality_Chn')
    def dehydrate_specility_Chn(self, subject):
        return '%s' % (subject.speciality.speciality_Chn)

class SubjectAdmin(ImportExportModelAdmin):
    resources_class = SubjectResource
    list_display = ['speciality','subject','subject_Chn',
    ]
    list_filter = ['speciality']
    search_fields = ['speciality',
    ]
    


class IomAdmin(ImportExportModelAdmin):
    resources_class = IomResource
    list_display = ['name','RFI','PO_Description','title_Chn','title',
    'equipment','speciality', 'subject',
    'title']
    list_filter = ['speciality','subject']
    search_fields = ['name','RFI','PO_Description','title_Chn','title',
    'equipment',
    'title']
    def speciality_Chn(self, obj):
        return obj.speciality.speciality_Chn
    speciality_Chn.short_description = '专业' 



class SubjectInline(admin.TabularInline):
    model = Subject
    fields = ('subject','subject_Chn',)


class SpecialityAdmin(ImportExportModelAdmin):
    resources_class = SpecialityResource
    list_display = ['speciality','speciality_Chn',
    ]
    list_filter = ['speciality']
    search_fields = ['speciality','speciality_Chn',
    ]
    inlines = [SubjectInline]


admin.site.register(Iom,IomAdmin)
admin.site.register(Speciality,SpecialityAdmin)
admin.site.register(Subject,SubjectAdmin)