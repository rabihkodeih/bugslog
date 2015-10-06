'''
Created on Nov 8, 2011

@author: Rabih Kodeih
'''

from django.contrib import admin
from main.models import Issue, Type, Severity, State


class IssueAdmin(admin.ModelAdmin):
    
    def issueId(self, obj): return obj.id
    issueId.allow_tags = True
    issueId.short_description = 'Issue Id'
    issueId.admin_order_field = 'id'
    
    fields = ('issueId', 'title', 'summary', 'notes', 'date', 'type', 'appointed_to', 'severity', 'state', 'posted_by')
    
    list_display = ('id', 'date', 'title', 'posted_by', 'appointed_to', 'type', 'severity', 'state')
    list_filter = ('posted_by', 'appointed_to', 'type', 'severity', 'state') 
    list_editable = ('state', )
    search_fields = ('title',)
    readonly_fields = ('issueId', 'posted_by', )

    #list_display_links = ('name',)
    #
    
    def save_form(self, request, form, change):
        obj = super(IssueAdmin, self).save_form(request, form, change)
        if not change:
            obj.posted_by = request.user
        return obj


admin.site.register(Issue, IssueAdmin)
admin.site.register(Severity)
admin.site.register(Type)
admin.site.register(State)
