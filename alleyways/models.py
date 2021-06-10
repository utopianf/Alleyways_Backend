from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

# Create your models here.

class Shard(models.Model):

    """Shard"""
    
    # id = models.IntegerField(_("Shard's id"), primary_key=True)
    name = models.CharField(_("Shard's name"), max_length=50)
    author = models.ForeignKey("User", verbose_name=_("Author"), on_delete=models.CASCADE)
    thumbnail_url = models.URLField(_("Shard's thumbnail"), max_length=200)
    pak_url = models.URLField(_("Shard's URL"), max_length=200)

    class Meta:
        verbose_name = _("Shard")
        verbose_name_plural = _("Shards")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Shard_detail", kwargs={"pk": self.pk})


class User(models.Model):

    """User"""
    
    name = models.CharField(_("User's name"), max_length=50)
    following_users = models.ManyToManyField("self", verbose_name=_("Following users"), symmetrical=False, blank=True)
    bookmarked_shards = models.ManyToManyField("Shard", verbose_name=_("Bookmarked shards"), blank=True)
    bookmarked_lists = models.ManyToManyField("ShardList", verbose_name=_("Bookmarked shard lists"), blank=True)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("User_detail", kwargs={"pk": self.pk})


class ShardList(models.Model):

    """Shard List"""

    shard = models.ManyToManyField("Shard", verbose_name=_("shard"))
    author = models.ForeignKey("User", verbose_name=_("Shard List Author"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Shard List")
        verbose_name_plural = _("Shard Lists")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ShardList_detail", kwargs={"pk": self.pk})
