# Generated by Django 3.1.3 on 2020-12-29 11:35

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_student', models.BooleanField(default=False)),
                ('is_lecturer', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('createdon', models.DateTimeField(auto_now_add=True)),
                ('updatedon', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_no', models.CharField(max_length=100)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lecturer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LecturerRemarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_names', models.CharField(max_length=30)),
                ('phase', models.CharField(choices=[('PROJECT_CONCEPT', 'project concept'), ('FIRST_CHAPTERS', 'first chapters'), ('DRAFT_PROJECT', 'draft project'), ('FINAL_PROJECT', 'final project')], default='PROJECT_CONCEPT', max_length=30)),
                ('comment', models.TextField()),
                ('status', models.CharField(choices=[('APPROVED', 'APPROVED'), ('REJECTED', 'REJECTED'), ('APPROVED WITH REMARKS', 'APPROVED WITH REMARKS')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('phase', models.CharField(choices=[('PROJECT_CONCEPT', 'project concept'), ('FIRST_CHAPTERS', 'first chapters'), ('DRAFT_PROJECT', 'draft project'), ('FINAL_PROJECT', 'final project')], default='PROJECT_CONCEPT', max_length=30)),
                ('project_title', models.CharField(max_length=100)),
                ('registration_no', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('project_brief', models.TextField(default='description')),
                ('submission_date', models.DateTimeField()),
                ('pdf', models.FileField(upload_to='projects/pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_no', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=50)),
                ('lecturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.lecturer')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubmitProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
                ('submit', models.FileField(upload_to='submission')),
                ('lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lecturer_submit', to='students.lecturer')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_submit', to='students.student')),
            ],
            options={
                'ordering': ['uploaded_on'],
            },
        ),
        migrations.CreateModel(
            name='StudentRemarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phase', models.CharField(choices=[('PROJECT_CONCEPT', 'project concept'), ('FIRST_CHAPTERS', 'first chapters'), ('DRAFT_PROJECT', 'draft project'), ('FINAL_PROJECT', 'final project')], default='PROJECT_CONCEPT', max_length=30)),
                ('status', models.CharField(choices=[('APPROVED', 'APPROVED'), ('REJECTED', 'REJECTED'), ('APPROVED WITH REMARKS', 'APPROVED WITH REMARKS')], max_length=30)),
                ('remarks_obtained', models.TextField()),
                ('lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lecturer_remarks', to='students.lecturer')),
                ('project_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_projects', to='students.project')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_remarks', to='students.student')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.project')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
    ]
