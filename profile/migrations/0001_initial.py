# Generated by Django 4.0.3 on 2022-05-26 05:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Upazila',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile.district')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=30)),
                ('etypeBiodata', models.CharField(choices=[('', '----'), ('পাত্রের বায়োডাটা', 'পাত্রের বায়োডাটা'), ('পাত্রীর বায়োডাটা', 'পাত্রীর বায়োডাটা')], default='----', max_length=20)),
                ('emaritalStatus', models.CharField(choices=[('', '----'), ('অবিবাহিত', 'অবিবাহিত'), ('ডিভোর্সড', 'ডিভোর্সড'), ('বিধবা', 'বিধবা'), ('বিপত্নীক', 'বিপত্নীক'), ('বিবাহিত', 'বিবাহিত'), ('বন্ধ্যা', 'বন্ধ্যা')], default='----', max_length=30)),
                ('ebirthYear', models.CharField(choices=[('', '----'), ('১৯৬০', '১৯৬০'), ('১৯৬১', '১৯৬১'), ('১৯৬২', '১৯৬২'), ('১৯৬৩', '১৯৬৩'), ('১৯৬৪', '১৯৬৪'), ('১৯৬৫', '১৯৬৫'), ('১৯৬৬', '১৯৬৬'), ('১৯৬৭', '১৯৬৭'), ('১৯৬৮', '১৯৬৮'), ('১৯৬৯', '১৯৬৯'), ('১৯৭০', '১৯৭০'), ('১৯৭১', '১৯৭১'), ('১৯৭২', '১৯৭২'), ('১৯৭৩', '১৯৭৩'), ('১৯৭৪', '১৯৭৪'), ('১৯৭৫', '১৯৭৫'), ('১৯৭৬', '১৯৭৬'), ('১৯৭৭', '১৯৭৭'), ('১৯৭৮', '১৯৭৮'), ('১৯৭৯', '১৯৭৯'), ('১৯৮০', '১৯৮০'), ('১৯৮১', '১৯৮১'), ('১৯৮২', '১৯৮২'), ('১৯৮৩', '১৯৮৩'), ('১৯৮৪', '১৯৮৪'), ('১৯৮৫', '১৯৮৫'), ('১৯৮৬', '১৯৮৬'), ('১৯৮৭', '১৯৮৭'), ('১৯৮৮', '১৯৮৮'), ('১৯৮৯', '১৯৮৯'), ('১৯৯০', '১৯৯০'), ('১৯৯১', '১৯৯১'), ('১৯৯২', '১৯৯২'), ('১৯৯৩', '১৯৯৩'), ('১৯৯৪', '১৯৯৪'), ('১৯৯৫', '১৯৯৫'), ('১৯৯৬', '১৯৯৬'), ('১৯৯৭', '১৯৯৭'), ('১৯৯৮', '১৯৯৮'), ('১৯৯৯', '১৯৯৯'), ('২০০০', '২০০০'), ('২০০১', '২০০১'), ('২০০২', '২০০২'), ('২০০৩', '২০০৩'), ('২০০৪', '২০০৪'), ('২০০৫', '২০০৫'), ('২০০৬', '২০০৬'), ('২০০৭', '২০০৭'), ('২০০৮', '২০০৮'), ('২০০৯', '২০০৯'), ('২০১০', '২০১০'), ('২০১১', '২০১১'), ('২০১২', '২০১২'), ('২০১৩', '২০১৩'), ('২০১৪', '২০১৪'), ('২০১৫', '২০১৫'), ('২০১৬', '২০১৬'), ('২০১৭', '২০১৭'), ('২০১৮', '২০১৮'), ('২০১৯', '২০১৯'), ('২০২০', '২০২০'), ('২০২১', '২০২১'), ('২০২২', '২০২২'), ('২০২৩', '২০২৩'), ('২০২৪', '২০২৪'), ('২০২৫', '২০২৫')], default='----', max_length=10)),
                ('eskinColor', models.CharField(choices=[('', '----'), ('কালো', 'কালো'), ('শ্যামলা', 'শ্যামলা'), ('উজ্জ্বল শ্যামলা', 'উজ্জ্বল শ্যামলা'), ('ফর্সা', 'ফর্সা'), ('উজ্জ্বল ফর্সা', 'উজ্জ্বল ফর্সা')], default='----', max_length=20)),
                ('ehightF', models.CharField(choices=[('', '----'), ('৩ ফুট', '৩ ফুট'), ('৪ ফুট', '৪ ফুট'), ('৫ ফুট', '৫ ফুট'), ('৬ ফুট', '৬ ফুট'), ('৭ ফুট', '৭ ফুট')], default='----', max_length=20)),
                ('ehightE', models.CharField(choices=[('', '----'), ('০ ইঞ্চি', '০ ইঞ্চি'), ('১ ইঞ্চি', '১ ইঞ্চি'), ('২ ইঞ্চি', '২ ইঞ্চি'), ('৩ ইঞ্চি', '৩ ইঞ্চি'), ('৪ ইঞ্চি', '৪ ইঞ্চি'), ('৫ ইঞ্চি', '৫ ইঞ্চি'), ('৬ ইঞ্চি', '৬ ইঞ্চি'), ('৭ ইঞ্চি', '৭ ইঞ্চি'), ('৮ ইঞ্চি', '৮ ইঞ্চি'), ('৯ ইঞ্চি', '৯ ইঞ্চি'), ('১০ ইঞ্চি', '১০ ইঞ্চি'), ('১১ ইঞ্চি', '১১ ইঞ্চি')], default='----', max_length=20)),
                ('eweight', models.CharField(max_length=150)),
                ('efigure', models.CharField(choices=[('', '----'), ('ফিট', 'ফিট'), ('চিকন', 'চিকন'), ('মোটা', 'মোটা')], default='----', max_length=20)),
                ('ebloodGroup', models.CharField(choices=[('', '----'), ('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')], default='----', max_length=10)),
                ('eparmanentAddress', models.CharField(max_length=200)),
                ('epresentAddress', models.CharField(max_length=200)),
                ('eGrowUpAddress', models.CharField(max_length=200)),
                ('estayNow', models.CharField(choices=[('', '----'), ('বাংলাদেশ', 'বাংলাদেশ'), ('প্রবাসী', 'প্রবাসী')], default='----', max_length=20)),
                ('eporbasi', models.TextField(blank=True, null=True)),
                ('eprobasiWomen', models.TextField(blank=True, null=True)),
                ('emedium', models.CharField(choices=[('', '----'), ('মাদ্রাসা', 'মাদ্রাসা'), ('জেনারেল', 'জেনারেল')], default='----', max_length=20)),
                ('essc', models.CharField(blank=True, choices=[('', '----'), ('হ্যাঁ', 'হ্যাঁ'), ('না', 'না')], max_length=10)),
                ('ewhichClass', models.CharField(blank=True, choices=[('', '----'), ('১০ম', '১০ম'), ('৯ম', '৯ম'), ('৮ম', '৮ম'), ('৭ম', '৭ম'), ('৬ষ্ঠ', '৬ষ্ঠ'), ('৫ম', '৫ম'), ('৪র্থ', '৪র্থ'), ('৩য়', '৩য়'), ('২য়', '২য়'), ('১ম', '১ম')], max_length=10)),
                ('esscPY', models.CharField(blank=True, choices=[('', '----'), ('১৯৬০', '১৯৬০'), ('১৯৬১', '১৯৬১'), ('১৯৬২', '১৯৬২'), ('১৯৬৩', '১৯৬৩'), ('১৯৬৪', '১৯৬৪'), ('১৯৬৫', '১৯৬৫'), ('১৯৬৬', '১৯৬৬'), ('১৯৬৭', '১৯৬৭'), ('১৯৬৮', '১৯৬৮'), ('১৯৬৯', '১৯৬৯'), ('১৯৭০', '১৯৭০'), ('১৯৭১', '১৯৭১'), ('১৯৭২', '১৯৭২'), ('১৯৭৩', '১৯৭৩'), ('১৯৭৪', '১৯৭৪'), ('১৯৭৫', '১৯৭৫'), ('১৯৭৬', '১৯৭৬'), ('১৯৭৭', '১৯৭৭'), ('১৯৭৮', '১৯৭৮'), ('১৯৭৯', '১৯৭৯'), ('১৯৮০', '১৯৮০'), ('১৯৮১', '১৯৮১'), ('১৯৮২', '১৯৮২'), ('১৯৮৩', '১৯৮৩'), ('১৯৮৪', '১৯৮৪'), ('১৯৮৫', '১৯৮৫'), ('১৯৮৬', '১৯৮৬'), ('১৯৮৭', '১৯৮৭'), ('১৯৮৮', '১৯৮৮'), ('১৯৮৯', '১৯৮৯'), ('১৯৯০', '১৯৯০'), ('১৯৯১', '১৯৯১'), ('১৯৯২', '১৯৯২'), ('১৯৯৩', '১৯৯৩'), ('১৯৯৪', '১৯৯৪'), ('১৯৯৫', '১৯৯৫'), ('১৯৯৬', '১৯৯৬'), ('১৯৯৭', '১৯৯৭'), ('১৯৯৮', '১৯৯৮'), ('১৯৯৯', '১৯৯৯'), ('২০০০', '২০০০'), ('২০০১', '২০০১'), ('২০০২', '২০০২'), ('২০০৩', '২০০৩'), ('২০০৪', '২০০৪'), ('২০০৫', '২০০৫'), ('২০০৬', '২০০৬'), ('২০০৭', '২০০৭'), ('২০০৮', '২০০৮'), ('২০০৯', '২০০৯'), ('২০১০', '২০১০'), ('২০১১', '২০১১'), ('২০১২', '২০১২'), ('২০১৩', '২০১৩'), ('২০১৪', '২০১৪'), ('২০১৫', '২০১৫'), ('২০১৬', '২০১৬'), ('২০১৭', '২০১৭'), ('২০১৮', '২০১৮'), ('২০১৯', '২০১৯'), ('২০২০', '২০২০'), ('২০২১', '২০২১'), ('২০২২', '২০২২'), ('২০২৩', '২০২৩'), ('২০২৪', '২০২৪'), ('২০২৫', '২০২৫')], max_length=10)),
                ('esscDept', models.CharField(blank=True, choices=[('', '----'), ('বিজ্ঞান বিভাগ', 'বিজ্ঞান বিভাগ'), ('মানবিক বিভাগ', 'মানবিক বিভাগ'), ('ব্যবসা বিভাগ', 'ব্যবসা বিভাগ'), ('কারিগরি / ভোকেশনাল', 'কারিগরি / ভোকেশনাল')], max_length=28)),
                ('esscResult', models.CharField(blank=True, choices=[('', '----'), ('Golden A+', 'Golden A+'), ('A+', 'A+'), ('A', 'A'), ('A-', 'A-'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=20)),
                ('ehsc', models.CharField(blank=True, choices=[('', '----'), ('হ্যাঁ', 'হ্যাঁ'), ('না', 'না'), ('ডিপ্লোমা পড়েছি', 'ডিপ্লোমা পড়েছি')], max_length=20)),
                ('ehscNotPass', models.CharField(blank=True, choices=[('', '----'), ('HSC দ্বিতীয় বর্ষ', 'HSC দ্বিতীয় বর্ষ'), ('HSC প্রথম বর্ষ', 'HSC প্রথম বর্ষ'), ('HSC পরীক্ষা দিয়ে পাশ করতে পারি নি', 'HSC পরীক্ষা দিয়ে পাশ করতে পারি নি'), ('HSC রেজাল্ট দেয় নি এখনো', 'HSC রেজাল্ট দেয় নি এখনো'), ('SSC এর পর আর পড়াশোনা করা হয় নি', 'SSC এর পর আর পড়াশোনা করা হয় নি')], max_length=50)),
                ('ediploma', models.CharField(blank=True, max_length=254, null=True)),
                ('ediplomaInstitute', models.CharField(blank=True, max_length=200, null=True)),
                ('ediplomaPY', models.CharField(blank=True, max_length=200, null=True)),
                ('ehscPY', models.CharField(blank=True, choices=[('', '----'), ('১৯৬০', '১৯৬০'), ('১৯৬১', '১৯৬১'), ('১৯৬২', '১৯৬২'), ('১৯৬৩', '১৯৬৩'), ('১৯৬৪', '১৯৬৪'), ('১৯৬৫', '১৯৬৫'), ('১৯৬৬', '১৯৬৬'), ('১৯৬৭', '১৯৬৭'), ('১৯৬৮', '১৯৬৮'), ('১৯৬৯', '১৯৬৯'), ('১৯৭০', '১৯৭০'), ('১৯৭১', '১৯৭১'), ('১৯৭২', '১৯৭২'), ('১৯৭৩', '১৯৭৩'), ('১৯৭৪', '১৯৭৪'), ('১৯৭৫', '১৯৭৫'), ('১৯৭৬', '১৯৭৬'), ('১৯৭৭', '১৯৭৭'), ('১৯৭৮', '১৯৭৮'), ('১৯৭৯', '১৯৭৯'), ('১৯৮০', '১৯৮০'), ('১৯৮১', '১৯৮১'), ('১৯৮২', '১৯৮২'), ('১৯৮৩', '১৯৮৩'), ('১৯৮৪', '১৯৮৪'), ('১৯৮৫', '১৯৮৫'), ('১৯৮৬', '১৯৮৬'), ('১৯৮৭', '১৯৮৭'), ('১৯৮৮', '১৯৮৮'), ('১৯৮৯', '১৯৮৯'), ('১৯৯০', '১৯৯০'), ('১৯৯১', '১৯৯১'), ('১৯৯২', '১৯৯২'), ('১৯৯৩', '১৯৯৩'), ('১৯৯৪', '১৯৯৪'), ('১৯৯৫', '১৯৯৫'), ('১৯৯৬', '১৯৯৬'), ('১৯৯৭', '১৯৯৭'), ('১৯৯৮', '১৯৯৮'), ('১৯৯৯', '১৯৯৯'), ('২০০০', '২০০০'), ('২০০১', '২০০১'), ('২০০২', '২০০২'), ('২০০৩', '২০০৩'), ('২০০৪', '২০০৪'), ('২০০৫', '২০০৫'), ('২০০৬', '২০০৬'), ('২০০৭', '২০০৭'), ('২০০৮', '২০০৮'), ('২০০৯', '২০০৯'), ('২০১০', '২০১০'), ('২০১১', '২০১১'), ('২০১২', '২০১২'), ('২০১৩', '২০১৩'), ('২০১৪', '২০১৪'), ('২০১৫', '২০১৫'), ('২০১৬', '২০১৬'), ('২০১৭', '২০১৭'), ('২০১৮', '২০১৮'), ('২০১৯', '২০১৯'), ('২০২০', '২০২০'), ('২০২১', '২০২১'), ('২০২২', '২০২২'), ('২০২৩', '২০২৩'), ('২০২৪', '২০২৪'), ('২০২৫', '২০২৫')], max_length=10)),
                ('ehscDept', models.CharField(blank=True, choices=[('', '----'), ('বিজ্ঞান বিভাগ', 'বিজ্ঞান বিভাগ'), ('মানবিক বিভাগ', 'মানবিক বিভাগ'), ('ব্যবসা বিভাগ', 'ব্যবসা বিভাগ')], max_length=20)),
                ('ehscResult', models.CharField(blank=True, choices=[('', '----'), ('Golden A+', 'Golden A+'), ('A+', 'A+'), ('A', 'A'), ('A-', 'A-'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=20)),
                ('eversitySubject', models.CharField(blank=True, max_length=254, null=True)),
                ('university', models.CharField(blank=True, max_length=254, null=True)),
                ('eversity_passing_Y', models.CharField(blank=True, max_length=200, null=True)),
                ('emastersSubject', models.CharField(blank=True, max_length=200, null=True)),
                ('emastersversity', models.CharField(blank=True, max_length=200, null=True)),
                ('ev_masters_passing_Y', models.CharField(blank=True, max_length=200, null=True)),
                ('ephd', models.TextField(blank=True, null=True)),
                ('emadrasa', models.CharField(blank=True, choices=[('', '----'), ('আলিয়া মাদ্রাসা', 'আলিয়া মাদ্রাসা'), ('কওমি মাদ্রাসা', 'কওমি মাদ্রাসা')], max_length=20)),
                ('ehafez', models.CharField(blank=True, max_length=254, null=True)),
                ('edhakhil', models.CharField(blank=True, choices=[('', '----'), ('হ্যাঁ', 'হ্যাঁ'), ('না', 'না')], max_length=10)),
                ('edhakhilwhichClass', models.CharField(blank=True, choices=[('', '----'), ('১০ম', '১০ম'), ('৯ম', '৯ম'), ('৮ম', '৮ম'), ('৭ম', '৭ম'), ('৬ষ্ঠ', '৬ষ্ঠ'), ('৫ম', '৫ম'), ('৪র্থ', '৪র্থ'), ('৩য়', '৩য়'), ('২য়', '২য়'), ('১ম', '১ম')], max_length=10)),
                ('edhakhilPY', models.CharField(blank=True, choices=[('', '----'), ('১৯৬০', '১৯৬০'), ('১৯৬১', '১৯৬১'), ('১৯৬২', '১৯৬২'), ('১৯৬৩', '১৯৬৩'), ('১৯৬৪', '১৯৬৪'), ('১৯৬৫', '১৯৬৫'), ('১৯৬৬', '১৯৬৬'), ('১৯৬৭', '১৯৬৭'), ('১৯৬৮', '১৯৬৮'), ('১৯৬৯', '১৯৬৯'), ('১৯৭০', '১৯৭০'), ('১৯৭১', '১৯৭১'), ('১৯৭২', '১৯৭২'), ('১৯৭৩', '১৯৭৩'), ('১৯৭৪', '১৯৭৪'), ('১৯৭৫', '১৯৭৫'), ('১৯৭৬', '১৯৭৬'), ('১৯৭৭', '১৯৭৭'), ('১৯৭৮', '১৯৭৮'), ('১৯৭৯', '১৯৭৯'), ('১৯৮০', '১৯৮০'), ('১৯৮১', '১৯৮১'), ('১৯৮২', '১৯৮২'), ('১৯৮৩', '১৯৮৩'), ('১৯৮৪', '১৯৮৪'), ('১৯৮৫', '১৯৮৫'), ('১৯৮৬', '১৯৮৬'), ('১৯৮৭', '১৯৮৭'), ('১৯৮৮', '১৯৮৮'), ('১৯৮৯', '১৯৮৯'), ('১৯৯০', '১৯৯০'), ('১৯৯১', '১৯৯১'), ('১৯৯২', '১৯৯২'), ('১৯৯৩', '১৯৯৩'), ('১৯৯৪', '১৯৯৪'), ('১৯৯৫', '১৯৯৫'), ('১৯৯৬', '১৯৯৬'), ('১৯৯৭', '১৯৯৭'), ('১৯৯৮', '১৯৯৮'), ('১৯৯৯', '১৯৯৯'), ('২০০০', '২০০০'), ('২০০১', '২০০১'), ('২০০২', '২০০২'), ('২০০৩', '২০০৩'), ('২০০৪', '২০০৪'), ('২০০৫', '২০০৫'), ('২০০৬', '২০০৬'), ('২০০৭', '২০০৭'), ('২০০৮', '২০০৮'), ('২০০৯', '২০০৯'), ('২০১০', '২০১০'), ('২০১১', '২০১১'), ('২০১২', '২০১২'), ('২০১৩', '২০১৩'), ('২০১৪', '২০১৪'), ('২০১৫', '২০১৫'), ('২০১৬', '২০১৬'), ('২০১৭', '২০১৭'), ('২০১৮', '২০১৮'), ('২০১৯', '২০১৯'), ('২০২০', '২০২০'), ('২০২১', '২০২১'), ('২০২২', '২০২২'), ('২০২৩', '২০২৩'), ('২০২৪', '২০২৪'), ('২০২৫', '২০২৫')], max_length=10)),
                ('edhakhilDept', models.CharField(blank=True, choices=[('', '----'), ('বিজ্ঞান বিভাগ', 'বিজ্ঞান বিভাগ'), ('মানবিক বিভাগ', 'মানবিক বিভাগ'), ('ব্যবসা বিভাগ', 'ব্যবসা বিভাগ')], max_length=20)),
                ('edhakhilResult', models.CharField(blank=True, choices=[('', '----'), ('Golden A+', 'Golden A+'), ('A+', 'A+'), ('A', 'A'), ('A-', 'A-'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=20)),
                ('ealim', models.CharField(blank=True, choices=[('', '----'), ('হ্যাঁ', 'হ্যাঁ'), ('না', 'না'), ('ডিপ্লোমা পড়েছি', 'ডিপ্লোমা পড়েছি')], max_length=20)),
                ('ealimNotPass', models.CharField(blank=True, choices=[('', '----'), ('আলিম দ্বিতীয় বর্ষ', 'আলিম দ্বিতীয় বর্ষ'), ('আলিম প্রথম বর্ষ', 'আলিম প্রথম বর্ষ'), ('আলিম পরীক্ষা দিয়ে পাশ করতে পারি নি', 'আলিম পরীক্ষা দিয়ে পাশ করতে পারি নি'), ('আলিম রেজাল্ট দেয় নি এখনো', 'আলিম রেজাল্ট দেয় নি এখনো'), ('দাখিল এর পর আর পড়াশোনা করা হয় নি', 'দাখিল এর পর আর পড়াশোনা করা হয় নি')], max_length=50)),
                ('ealimPY', models.CharField(blank=True, choices=[('', '----'), ('১৯৬০', '১৯৬০'), ('১৯৬১', '১৯৬১'), ('১৯৬২', '১৯৬২'), ('১৯৬৩', '১৯৬৩'), ('১৯৬৪', '১৯৬৪'), ('১৯৬৫', '১৯৬৫'), ('১৯৬৬', '১৯৬৬'), ('১৯৬৭', '১৯৬৭'), ('১৯৬৮', '১৯৬৮'), ('১৯৬৯', '১৯৬৯'), ('১৯৭০', '১৯৭০'), ('১৯৭১', '১৯৭১'), ('১৯৭২', '১৯৭২'), ('১৯৭৩', '১৯৭৩'), ('১৯৭৪', '১৯৭৪'), ('১৯৭৫', '১৯৭৫'), ('১৯৭৬', '১৯৭৬'), ('১৯৭৭', '১৯৭৭'), ('১৯৭৮', '১৯৭৮'), ('১৯৭৯', '১৯৭৯'), ('১৯৮০', '১৯৮০'), ('১৯৮১', '১৯৮১'), ('১৯৮২', '১৯৮২'), ('১৯৮৩', '১৯৮৩'), ('১৯৮৪', '১৯৮৪'), ('১৯৮৫', '১৯৮৫'), ('১৯৮৬', '১৯৮৬'), ('১৯৮৭', '১৯৮৭'), ('১৯৮৮', '১৯৮৮'), ('১৯৮৯', '১৯৮৯'), ('১৯৯০', '১৯৯০'), ('১৯৯১', '১৯৯১'), ('১৯৯২', '১৯৯২'), ('১৯৯৩', '১৯৯৩'), ('১৯৯৪', '১৯৯৪'), ('১৯৯৫', '১৯৯৫'), ('১৯৯৬', '১৯৯৬'), ('১৯৯৭', '১৯৯৭'), ('১৯৯৮', '১৯৯৮'), ('১৯৯৯', '১৯৯৯'), ('২০০০', '২০০০'), ('২০০১', '২০০১'), ('২০০২', '২০০২'), ('২০০৩', '২০০৩'), ('২০০৪', '২০০৪'), ('২০০৫', '২০০৫'), ('২০০৬', '২০০৬'), ('২০০৭', '২০০৭'), ('২০০৮', '২০০৮'), ('২০০৯', '২০০৯'), ('২০১০', '২০১০'), ('২০১১', '২০১১'), ('২০১২', '২০১২'), ('২০১৩', '২০১৩'), ('২০১৪', '২০১৪'), ('২০১৫', '২০১৫'), ('২০১৬', '২০১৬'), ('২০১৭', '২০১৭'), ('২০১৮', '২০১৮'), ('২০১৯', '২০১৯'), ('২০২০', '২০২০'), ('২০২১', '২০২১'), ('২০২২', '২০২২'), ('২০২৩', '২০২৩'), ('২০২৪', '২০২৪'), ('২০২৫', '২০২৫')], max_length=10)),
                ('ealimDept', models.CharField(blank=True, choices=[('', '----'), ('বিজ্ঞান বিভাগ', 'বিজ্ঞান বিভাগ'), ('মানবিক বিভাগ', 'মানবিক বিভাগ'), ('ব্যবসা বিভাগ', 'ব্যবসা বিভাগ')], max_length=20)),
                ('ealimResult', models.CharField(blank=True, choices=[('', '----'), ('Golden A+', 'Golden A+'), ('A+', 'A+'), ('A', 'A'), ('A-', 'A-'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=20)),
                ('efazilSubject', models.CharField(blank=True, max_length=254, null=True)),
                ('efaziluniversity', models.CharField(blank=True, max_length=200, null=True)),
                ('efazil_passing_Y', models.CharField(blank=True, max_length=200, null=True)),
                ('ekamilSubject', models.CharField(blank=True, max_length=200, null=True)),
                ('ekamilversity', models.CharField(blank=True, max_length=200, null=True)),
                ('ekamil_passing_Y', models.CharField(blank=True, max_length=200, null=True)),
                ('edaoraya', models.CharField(blank=True, choices=[('', '----'), ('হ্যাঁ', 'হ্যাঁ'), ('না', 'না'), ('না, এখনো পড়ছি', 'না, এখনো পড়ছি')], max_length=20)),
                ('edaorayaYear', models.CharField(blank=True, max_length=200, null=True)),
                ('edaorayaPassingYear', models.CharField(blank=True, max_length=200, null=True)),
                ('ehadiserNotija', models.CharField(blank=True, choices=[('', '----'), ('মুমতায', 'মুমতায'), ('জায়্যিদ জিদ্দান', 'জায়্যিদ জিদ্দান'), ('জায়্যিদ', 'জায়্যিদ'), ('মকবূল', 'মকবূল')], max_length=20)),
                ('etakhassus', models.CharField(blank=True, choices=[('', '----'), ('হ্যাঁ', 'হ্যাঁ'), ('না', 'না')], max_length=10)),
                ('etakhassusSubject', models.CharField(blank=True, max_length=200, null=True)),
                ('etakhassus_P_Year', models.CharField(blank=True, max_length=200, null=True)),
                ('ehighestdegree', models.TextField(blank=True, null=True)),
                ('eotherEducation', models.TextField(blank=True, null=True)),
                ('eoccupation', models.CharField(max_length=50)),
                ('eincome', models.CharField(blank=True, max_length=180, null=True)),
                ('eworkingPlace', models.CharField(max_length=120)),
                ('edetailsOccupation', models.TextField(blank=True, null=True)),
                ('edetailsOccupationWomen', models.TextField(blank=True, null=True)),
                ('efathername', models.CharField(max_length=50)),
                ('emothername', models.CharField(max_length=50)),
                ('efatherOccupation', models.CharField(max_length=120)),
                ('emotherOccupation', models.CharField(max_length=120)),
                ('ehavingBrother', models.CharField(choices=[('', '----'), ('ভাই নেই', 'ভাই নেই'), ('১ জন', '১ জন'), ('২ জন', '২ জন'), ('৩ জন', '৩ জন'), ('৪ জন', '৪ জন'), ('৫ জন', '৫ জন'), ('৬ জন', '৬ জন'), ('৭ জন', '৭ জন'), ('৮ জন', '৮ জন'), ('৯ জন', '৯ জন'), ('১০ জন', '১০ জন'), ('১১ জন', '১১ জন'), ('১২ জন', '১২ জন'), ('১৩ জন', '১৩ জন'), ('১৪ জন', '১৪ জন'), ('১৫ জন', '১৫ জন')], default='----', max_length=10)),
                ('edetailsBrother', models.TextField(blank=True, null=True)),
                ('ehavingSister', models.CharField(choices=[('', '----'), ('বোন নেই', 'বোন নেই'), ('১ জন', '১ জন'), ('২ জন', '২ জন'), ('৩ জন', '৩ জন'), ('৪ জন', '৪ জন'), ('৫ জন', '৫ জন'), ('৬ জন', '৬ জন'), ('৭ জন', '৭ জন'), ('৮ জন', '৮ জন'), ('৯ জন', '৯ জন'), ('১০ জন', '১০ জন'), ('১১ জন', '১১ জন'), ('১২ জন', '১২ জন'), ('১৩ জন', '১৩ জন'), ('১৪ জন', '১৪ জন'), ('১৫ জন', '১৫ জন')], default='----', max_length=10)),
                ('edetailsSister', models.TextField(blank=True, null=True)),
                ('esocialStatus', models.CharField(choices=[('', '----'), ('নিম্নবিত্ত', 'নিম্নবিত্ত'), ('নিম্ন মধ্যবিত্ত', 'নিম্ন মধ্যবিত্ত'), ('মধ্যবিত্ত', 'মধ্যবিত্ত'), ('উচ্চ মধ্যবিত্ত', 'উচ্চ মধ্যবিত্ত'), ('উচ্চবিত্ত', 'উচ্চবিত্ত')], default='----', max_length=20)),
                ('euncle', models.CharField(blank=True, max_length=254, null=True)),
                ('efamily', models.TextField()),
                ('edari', models.CharField(blank=True, max_length=120, null=True)),
                ('edhaknu', models.CharField(blank=True, max_length=154, null=True)),
                ('eclothMan', models.CharField(blank=True, max_length=184, null=True)),
                ('eclothWomen', models.CharField(blank=True, max_length=214, null=True)),
                ('esalat', models.CharField(max_length=154)),
                ('esalatstart', models.CharField(max_length=154)),
                ('emahram', models.TextField()),
                ('equran', models.CharField(max_length=154)),
                ('emazhab', models.CharField(max_length=154)),
                ('epolitics', models.CharField(max_length=154)),
                ('emovie', models.CharField(max_length=154)),
                ('emehnot', models.CharField(max_length=154)),
                ('emurid', models.CharField(max_length=254)),
                ('emazar', models.CharField(max_length=254)),
                ('eislamicbook', models.CharField(max_length=254)),
                ('escholar', models.CharField(max_length=254)),
                ('especialqualification', models.TextField(blank=True, null=True)),
                ('eaboutyourself', models.TextField()),
                ('edivorce', models.TextField(blank=True, null=True)),
                ('emarried', models.TextField(blank=True, null=True)),
                ('ebipotnik', models.TextField(blank=True, null=True)),
                ('ebidoba', models.TextField(blank=True, null=True)),
                ('ebonda', models.TextField(blank=True, null=True)),
                ('eobivabokMotamot', models.TextField()),
                ('ereasonMarry', models.CharField(max_length=254)),
                ('ewifeporda', models.CharField(blank=True, max_length=254, null=True)),
                ('ewifeeducation', models.CharField(blank=True, max_length=254, null=True)),
                ('ewifejob', models.CharField(blank=True, max_length=254, null=True)),
                ('ewifestay', models.CharField(blank=True, max_length=254, null=True)),
                ('ewifeDowry', models.CharField(blank=True, max_length=254, null=True)),
                ('ejob', models.CharField(blank=True, max_length=254, null=True)),
                ('eeducation', models.CharField(blank=True, max_length=254, null=True)),
                ('ejobcontinue', models.CharField(blank=True, max_length=254, null=True)),
                ('ebiyeSunnat', models.CharField(max_length=254)),
                ('edenmohar', models.CharField(max_length=254)),
                ('especialKichu', models.TextField(blank=True, null=True)),
                ('eLPYear', models.CharField(max_length=120)),
                ('eLPHeight', models.CharField(max_length=120)),
                ('eLPSkinColor', models.CharField(max_length=120)),
                ('eLPEducationalQualification', models.CharField(max_length=180)),
                ('eLPDistrict', models.CharField(max_length=120)),
                ('eLPMaritalStatus', models.CharField(max_length=120)),
                ('eLPOccupation', models.TextField()),
                ('eLPFamilyStatus', models.CharField(max_length=200)),
                ('eLPVehabiour', models.TextField()),
                ('eshopot', models.CharField(choices=[('', '----'), ('হ্যাঁ', 'হ্যাঁ'), ('না', 'না')], default='----', max_length=10)),
                ('eFalseInformation', models.CharField(choices=[('', '----'), ('হ্যাঁ', 'হ্যাঁ'), ('না', 'না')], default='----', max_length=10)),
                ('eguardianNumber', models.CharField(max_length=120)),
                ('eguardianRelation', models.CharField(max_length=120)),
                ('econtactEmail', models.EmailField(blank=True, max_length=154, null=True)),
                ('econtactNumber', models.CharField(max_length=120)),
                ('estatus', models.BooleanField(blank=True, null=True)),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profile.district')),
                ('upazila', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profile.upazila')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
