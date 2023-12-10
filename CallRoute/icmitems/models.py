# from django.db import models

# Create your models here.

#
# class Agent(models.Model):
#     SkillTargetID = models.IntegerField(null=False, primary_key=True)
#     PersonID = models.IntegerField(null=False)
#     AgentDeskSettingsID = models.IntegerField(null=True)
#     ScheduleID = models.IntegerField(null=True)
#     PeripheralID = models.IntegerField(null=False)
#     EnterpriseName = models.CharField(max_length=32, null=False)
#     PeripheralNumber = models.CharField(max_length=32, null=False)
#     ConfigParam = models.CharField(max_length=255, null=True)
#     Description = models.CharField(max_length=255, null=True)
#     Deleted = models.CharField(max_length=1, null=False)
#     PeripheralName = models.CharField(max_length=32, null=True)
#     TemporaryAgent = models.CharField(max_length=1, null=False)
#     AgentStateTrace = models.CharField(max_length=1, null=False)
#     SupervisorAgent = models.CharField(max_length=1, null=False)
#     ChangeStamp = models.IntegerField(null=False)
#     UserDeletable = models.CharField(max_length=1, null=False)
#     DefaultSkillGroup = models.IntegerField(null=True)
#     DepartmentID = models.IntegerField(null=True)
#     DateTimeStamp = models.DateTimeField(null=True)
#
#     class Meta:
#         ordering = ('SkillTargetID',)
#
#     def __str__(self):
#         return self.SkillTargetID
