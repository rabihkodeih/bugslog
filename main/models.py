from django.db import models
from django.contrib.auth.models import User #@UnusedImport
from django.utils.datetime_safe import datetime

# Field examples:
#    date_field      = models.DateField(blank=True, null=True, db_index=True)
#    fk_field        = models.ForeignKey('Country')
#    string_field    = models.CharField(max_length=256, blank=True, null=True)
#    text_field      = models.TextField(blank=True, null=True)


def get_default_type():
    if len(Type.objects.all()) == 0:
        Type.objects.create(content="Bug")
        Type.objects.create(content="Issue")
        Type.objects.create(content="Feature")
        Type.objects.create(content="Comment")
    return Type.objects.all()[0] 

def get_default_state():
    if len(State.objects.all()) == 0:
        State.objects.create(content="Opened")
        State.objects.create(content="Closed")
        State.objects.create(content="Under Review")
    return State.objects.all()[0]

def get_default_severity():
    if len(Severity.objects.all()) == 0:
        Severity.objects.create(content="Trivial")
        Severity.objects.create(content="Important")
        Severity.objects.create(content="Critical")
    return Severity.objects.all()[0]

class Issue(models.Model):
    title           = models.CharField(max_length=256)
    summary         = models.TextField(blank=True, null=True)
    notes           = models.TextField(blank=True, null=True)
    date            = models.DateField(default=datetime.now, db_index=True)
    posted_by       = models.ForeignKey(User, blank=True, null=True)
    type            = models.ForeignKey('Type', default=get_default_type)
    appointed_to    = models.ForeignKey(User, related_name='issue_appointed_to', blank=True, null=True)
    severity        = models.ForeignKey('Severity', default=get_default_severity)
    state           = models.ForeignKey('State', default=get_default_state)
    def __unicode__(self):
        return self.title

class Type(models.Model):
    content         = models.CharField(max_length=50)
    def __unicode__(self):
        return self.content

class State(models.Model):
    content         = models.CharField(max_length=50)
    def __unicode__(self):
        return self.content

class Severity(models.Model):
    content         = models.CharField(max_length=50)
    def __unicode__(self):
        return self.content


