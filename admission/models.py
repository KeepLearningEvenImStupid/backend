from slugify import slugify
from django.db import models
from django.contrib.auth.models import *
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Angkatan(models.Model):
    tahun = models.CharField(max_length=4)
    semester = models.CharField(max_length=10)
    deskripsi = models.CharField(max_length=255)

    def __str__(self):
        return self.tahun


class Seleksi(models.Model):
    strata1 = 'S1 - Strata 1'
    strata2 = 'S2 - Strata 2'

    sistem_kuliah_sore_A = 'Reguler Sore Kampus A'
    sistem_kuliah_sore_B = 'Reguler Sore Kampus B'

    sistem_kuliah_pagi_A = 'Reguler Pagi Kampus A'
    sistem_kuliah_pagi_B = 'Reguler Pagi Kampus B'

    program_studi_s1 = 'S1 - Ilmu Hukun (S1) '
    program_studi_s2 = 'S2 - Ilmu Hukun (S2) '

    CHOICES_STRATA = (
        (strata1, strata1),
        (strata2, strata2),
    )

    CHOICES_SISTEM_KULIAH = (
        (sistem_kuliah_pagi_A, sistem_kuliah_pagi_A),
        (sistem_kuliah_pagi_B, sistem_kuliah_pagi_B),
        (sistem_kuliah_sore_A, sistem_kuliah_sore_A),
        (sistem_kuliah_sore_B, sistem_kuliah_sore_B),
    )

    CHOICES_PROGRAMSTUDI = (
        (program_studi_s1, program_studi_s1),
        (program_studi_s2, program_studi_s2),
    )

    kategori = models.CharField(max_length=255)
    deskripsi = models.CharField(max_length=255)
    awal_pendaftaran = models.DateField()
    akhir_pendaftaran = models.DateField()

    strata = models.CharField(
        max_length=255, choices=CHOICES_STRATA, default='--Pilih Salah Satu--')

    sistem_kuliah = models.CharField(
        max_length=255, choices=CHOICES_SISTEM_KULIAH, default='--Pilih Salah Satu--')

    program_studi = models.CharField(
        max_length=255, choices=CHOICES_PROGRAMSTUDI, default='--Pilih Salah Satu--')

    gelombang = models.CharField(max_length=255)

    formulir = models.CharField(max_length=20, default="BERBAYAR")

    daya_tampung = models.CharField(max_length=255, blank=True)

    periode_pendaftaran = models.CharField(
        max_length=255, default='Periode Pendaftaran')

    slug = models.SlugField(max_length=255, blank=True, null=True)

    ujian_hukum = models.CharField(
        max_length=255, blank=True)

    ujian_kemampuan_dasar = models.CharField(
        max_length=255, blank=True)

    tanggal_mulai_ujian_kemampuan_dasar = models.DateField(
        null=True, blank=True)
    tanggal_selesai_ujian_kemampuan_dasar = models.DateField(
        null=True, blank=True)

    tanggal_mulai_ujian_hukum = models.DateField(null=True, blank=True)
    tanggal_selesai_ujian_hukum = models.DateField(null=True, blank=True)

    def save(self, force_insert=False, force_update=False, *args, **kwargs) -> None:
        self.slug = slugify(self.kategori)
        return super().save(force_insert, force_update, *args, **kwargs)


class Admission(models.Model):
    nama = models.CharField(max_length=255)
    alamat = models.CharField(max_length=100)
    asal_sekolah = models.CharField(max_length=30)
    tempat_lahir = models.CharField(max_length=35)
    tanggal_lahir = models.DateField()

    DITERIMA = 'Diterima'
    TDKDITERIMA = 'Tidak Diterima'
    PENDING = 'Pending'

    CHOICES = (
        (DITERIMA, DITERIMA),
        (PENDING, PENDING),
        (TDKDITERIMA, TDKDITERIMA),
    )
    status = models.CharField(
        max_length=255, choices=CHOICES, default=PENDING)
    angkatan_id = models.ForeignKey(
        Angkatan, on_delete=models.RESTRICT, null=True)
    pengguna = models.OneToOneField(
        User, on_delete=models.RESTRICT, null=True, blank=True)

    program_studi = models.ForeignKey(
        Seleksi, on_delete=models.RESTRICT, related_name='Program Studi+',  null=True)

    __original_status = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_status = self.status

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.status != self.__original_status:
            if self.status == "Diterima":
                group = Group.objects.get(name='Mahasiswa')
                group.user_set.add(self.pengguna)
            if self.status == "Tidak Diterima":
                group = Group.objects.get(name='Mahasiswa')
                group.user_set.remove(self.pengguna)
        else:
            pass
        super().save(force_insert, force_update, *args, **kwargs)
        self.__original_status = self.status
