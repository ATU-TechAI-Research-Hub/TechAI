from django.db import models
from django.utils.text import slugify


class Person(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    email = models.EmailField()

    class Meta:
        abstract = True

    # TODO: add uploading of profile picture

    def __str__(self):
        return self.name


class Mentor(Person):
    INSTRUCTOR = 'I'
    ASSISTANT_PROFESSOR = 'AP'
    ASSOCIATE_PROFESSOR = 'AOP'
    PROFESSOR = 'P'
    PROFESSOR_TYPE_CHOICES = [
        (INSTRUCTOR, 'Instructor'),
        (ASSISTANT_PROFESSOR, 'Assistant Professor'),
        (ASSOCIATE_PROFESSOR, 'Associate Professor'),
        (PROFESSOR, 'Professor'),
    ]

    department = models.CharField(max_length=255)
    professor_type = models.CharField(max_length=3, choices=PROFESSOR_TYPE_CHOICES, default=INSTRUCTOR)


class Peer(Person):
    UNDERGRADUATE = 'UG'
    GRADUATE = 'GR'
    POSTGRADUATE = 'PG'
    DOCTORATE = 'PHD'
    DEGREE_LEVEL_CHOICES = [
        (UNDERGRADUATE, 'Undergraduate'),
        (GRADUATE, 'Graduate'),
        (POSTGRADUATE, 'Postgraduate'),
        (DOCTORATE, 'Doctorate'),
    ]

    major = models.CharField(max_length=255)
    degree_level = models.CharField(max_length=3, choices=DEGREE_LEVEL_CHOICES, default=UNDERGRADUATE)


class Publication(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.url


class Project(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    publication = models.OneToOneField(Publication, on_delete=models.CASCADE, blank=True, null=True,
                                       related_name='project')
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='mentored_projects')
    peers = models.ManyToManyField(Peer, related_name='peer_projects')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
