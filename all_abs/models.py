from django.db import models

class Biology(models.Model):
    image = models.ImageField(upload_to='all_abs/biology/')

class Chemistry(models.Model):
    image = models.ImageField(upload_to='all_abs/chemistry/')

class English(models.Model):
    image = models.ImageField(upload_to='all_abs/english/')

class History(models.Model):
    image = models.ImageField(upload_to='all_abs/history/')

class Information(models.Model):
    image = models.ImageField(upload_to='all_abs/information/')

class Literature(models.Model):
    image = models.ImageField(upload_to='all_abs/literature/')

class Math(models.Model):
    image = models.ImageField(upload_to='all_abs/math/')

class OBZ(models.Model):
    image = models.ImageField(upload_to='all_abs/obz/')

class OID(models.Model):
    image = models.ImageField(upload_to='all_abs/oid/')

class Physics(models.Model):
    image = models.ImageField(upload_to='all_abs/physics/')

class Russian_language(models.Model):
    image = models.ImageField(upload_to='all_abs/russian_language/')

class Social_studies(models.Model):
    image = models.ImageField(upload_to='all_abs/social_studies/')

