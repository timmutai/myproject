from users.models import users
from django.db import models


# Model to store student application status
class applications(models.Model):
    
    user=models.ForeignKey(users,on_delete=models.PROTECT)    
    school_name=models.CharField(max_length=200 )
    school_address=models.CharField(max_length=200 )
    academic_level=models.CharField(max_length=100 )
    year_of_completion=models.DateField(null=True)
    reason_for_application=models.TextField()
    recomendation=models.FileField(upload_to='recomendation')
    birth_certificate=models.FileField(upload_to='files')
    national_id=models.FileField(upload_to='files')
    sponsor=models.TextField(max_length=200, null=True)
    applicationDate=models.DateField(auto_now_add=True)
    staffapproval=models.BooleanField(default=False)
    sponsorshipApproval=models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)