from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    descripcion = models.TextField(blank=True)
    sitio_web = models.URLField(blank=True)

    def __str__(self):
        return self.user.username

# ✅ Solo una señal para crear perfil si no existe
@receiver(post_save, sender=User)
def crear_o_actualizar_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        # Solo guardar si ya existe el perfil
        if hasattr(instance, 'userprofile'):
            instance.userprofile.save()