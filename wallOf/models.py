from django.db import models

# Create your models here.
from django.utils.functional import cached_property


class ModelPosts(models.Model):
    title = models.CharField(default="", blank=True, max_length=100, null=True)
    frustration = models.TextField(blank=False, max_length=240)
    date_and_time = models.DateTimeField(auto_now_add=True)
    only_date = models.DateField(auto_now_add=True)
    up_vote = models.IntegerField(default=0, blank=True, null=False)
    down_vote = models.IntegerField(default=0, blank=True, null=False)

    # @property
    # def vote(self):
    #     return self.up_vote - (-self.down_vote)

    @property
    def salted_pk(self):
        return self.pk + 3669

    @cached_property
    def vote(self):
        try:
            if self.up_vote is None:
                self.up_vote = 0
                return self.up_vote - (-self.down_vote)

            if self.down_vote is None:
                self.down_vote = 0
                return self.up_vote - (-self.down_vote)

            return self.up_vote - (-self.down_vote)
        except Exception:
            return

    def __str__(self):
        if self.title is None:
            return self.frustration

        else:
            return self.title


class ModelSecretes(models.Model):
    title = models.CharField(default="", blank=True, max_length=100, null=True)
    secrete = models.TextField(blank=False, max_length=240)
    date_and_time = models.DateTimeField(auto_now_add=True)
    only_date = models.DateField(auto_now_add=True)
    up_vote = models.IntegerField(default=0, blank=True, null=False)
    down_vote = models.IntegerField(default=0, blank=True, null=False)

    # @property
    # def vote(self):
    #     return self.up_vote - (-self.down_vote)

    @property
    def salted_pk(self):
        return self.pk + 3669

    @cached_property
    def vote(self):
        try:
            if self.up_vote is None:
                self.up_vote = 0
                return self.up_vote - (-self.down_vote)

            if self.down_vote is None:
                self.down_vote = 0
                return self.up_vote - (-self.down_vote)

            return self.up_vote - (-self.down_vote)
        except Exception:
            return

    def __str__(self):
        if self.title is None:
            return self.secrete

        else:
            return self.title


class ModelAdvice(models.Model):
    title = models.CharField(default="", blank=True, max_length=100, null=True)
    advice = models.TextField(blank=False, max_length=240)
    date_and_time = models.DateTimeField(auto_now_add=True)
    only_date = models.DateField(auto_now_add=True)
    up_vote = models.IntegerField(default=0, blank=True, null=False)
    down_vote = models.IntegerField(default=0, blank=True, null=False)

    # @property
    # def vote(self):
    #     return self.up_vote - (-self.down_vote)

    @property
    def salted_pk(self):
        return self.pk + 3669

    @cached_property
    def vote(self):
        try:
            if self.up_vote is None:
                self.up_vote = 0
                return self.up_vote - (-self.down_vote)

            if self.down_vote is None:
                self.down_vote = 0
                return self.up_vote - (-self.down_vote)

            return self.up_vote - (-self.down_vote)
        except Exception:
            return

    def __str__(self):
        if self.title is None:
            return self.advice

        else:
            return self.title


class ModelComment(models.Model):
    comment = models.TextField(blank=False, max_length=120)
    date_and_time = models.DateTimeField(auto_now_add=True)
    only_date = models.DateField(auto_now_add=True)
    up_vote = models.IntegerField(default=0, blank=True, null=False)
    down_vote = models.IntegerField(default=0, blank=True, null=False)

    # parent_post = models.ForeignKey(ModelPosts)


    def __str__(self):
        return self.comment