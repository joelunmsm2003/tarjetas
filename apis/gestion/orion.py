# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class OriAcciones(models.Model):
    accion = models.IntegerField()
    anx_sup = models.CharField(max_length=20)
    anx_age = models.CharField(max_length=20)
    canal = models.CharField(max_length=20)
    flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ori_acciones'


class OriAcd(models.Model):
    id_ori_acd = models.AutoField(primary_key=True)
    did_campana = models.CharField(db_column='DID_Campana', max_length=45)  # Field name made lowercase.
    numero_llamado = models.CharField(db_column='Numero_Llamado', max_length=45)  # Field name made lowercase.
    numero_entrante = models.CharField(db_column='Numero_Entrante', max_length=45)  # Field name made lowercase.
    channel_entrante = models.CharField(db_column='Channel_Entrante', max_length=50)  # Field name made lowercase.
    tiempo = models.CharField(db_column='Tiempo', max_length=15)  # Field name made lowercase.
    flag = models.IntegerField()
    uniqueid = models.CharField(max_length=30)
    fin = models.IntegerField()
    age_nombre = models.CharField(max_length=100, blank=True, null=True)
    tie_ing = models.DateTimeField()
    tie_acd = models.DateTimeField()
    tie_tra = models.DateTimeField()
    tie_con = models.DateTimeField()
    tie_fin = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ori_acd'


class OriCampana(models.Model):
    id_ori_campana = models.AutoField(primary_key=True)
    campana_nombre = models.CharField(max_length=80)
    campana_tipo = models.IntegerField()
    campana_tipo_detalle = models.IntegerField()
    campana_estado = models.IntegerField()
    campana_gestion = models.CharField(max_length=100)
    agregistrados = models.IntegerField(db_column='AgRegistrados')  # Field name made lowercase.
    agocupados = models.IntegerField(db_column='AgOcupados')  # Field name made lowercase.
    agdetenidos = models.IntegerField(db_column='AgDetenidos')  # Field name made lowercase.
    agpausados = models.IntegerField(db_column='AgPausados')  # Field name made lowercase.
    campana_canales = models.IntegerField()
    bas_tot = models.IntegerField()
    bas_pro = models.IntegerField()
    bas_pro_con = models.IntegerField()
    bas_pro_noc = models.IntegerField()
    bas_pro_ocu = models.IntegerField()
    bas_pro_ven = models.IntegerField()
    bas_pro_nov = models.IntegerField()
    bas_pro_age = models.IntegerField()
    campana_activa = models.IntegerField()
    bas_pen = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ori_campana'


class OriChat(models.Model):
    id_ori_chat = models.AutoField(primary_key=True)
    chat_fhora = models.DateTimeField()
    id_ori_usuario = models.IntegerField()
    nombre_usuario = models.CharField(max_length=50)
    id_ori_super = models.IntegerField()
    nombre_super = models.CharField(max_length=50)
    chat_mensaje = models.CharField(max_length=200)
    flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ori_chat'


class OriEstados(models.Model):
    id_ori_estados = models.AutoField(primary_key=True)
    cod_estado = models.IntegerField()
    txt_estado = models.CharField(max_length=15)
    id_ori_usuario = models.IntegerField()
    f_inicio = models.DateTimeField()
    f_fin = models.DateTimeField()
    flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ori_estados'


class OriGrabaciones(models.Model):
    id_ori_grabaciones = models.AutoField(primary_key=True)
    id_ori_campana = models.IntegerField()
    id_ori_usuario = models.IntegerField()
    id_ori_llamadas = models.IntegerField()
    fecha_hora = models.DateTimeField()
    txt_audio = models.CharField(max_length=200)
    tproyecto = models.CharField(max_length=20)
    llam_origen = models.CharField(max_length=20)
    llam_destino = models.CharField(max_length=20)
    flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ori_grabaciones'


class OriLlamadas(models.Model):
    id_ori_llamadas = models.AutoField(primary_key=True)
    age_ip = models.CharField(max_length=20, blank=True, null=True)
    age_codigo = models.CharField(max_length=10, blank=True, null=True)
    cam_codigo = models.IntegerField(blank=True, null=True)
    llam_numero = models.CharField(max_length=20, blank=True, null=True)
    llam_estado = models.IntegerField(blank=True, null=True)
    llam_flag = models.IntegerField(blank=True, null=True)
    llam_uniqueid = models.CharField(max_length=45, blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    f_origen = models.DateTimeField()
    canal1 = models.CharField(max_length=50, blank=True, null=True)
    canal2 = models.CharField(max_length=50, blank=True, null=True)
    flagfin = models.IntegerField(db_column='flagFIN', blank=True, null=True)  # Field name made lowercase.
    v_tring = models.IntegerField(blank=True, null=True)
    v_retry = models.IntegerField(blank=True, null=True)
    v_tipbusc = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    bill = models.IntegerField(blank=True, null=True)
    tregistro = models.CharField(max_length=11)
    gestion_editid1 = models.CharField(max_length=20, blank=True, null=True)
    gestion_editid2 = models.CharField(max_length=20, blank=True, null=True)
    gestion_editid3 = models.CharField(max_length=20, blank=True, null=True)
    f_llam_discador = models.DateTimeField()
    f_llam_resuelve = models.DateTimeField()
    f_llam_fin = models.DateTimeField()
    f_fingestion = models.DateTimeField()
    hc = models.IntegerField(db_column='HC')  # Field name made lowercase.
    dur = models.IntegerField(db_column='DUR')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ori_llamadas'


class OriUsuario(models.Model):
    id_ori_usuario = models.AutoField(primary_key=True)
    usuario_logeo = models.CharField(max_length=20)
    usuario_nombre = models.CharField(max_length=80)
    usuario_clave = models.CharField(max_length=60)
    usuario_tipo = models.CharField(max_length=60)
    id_ori_campana = models.IntegerField()
    usuario_ip = models.CharField(max_length=20)
    usuario_estado = models.IntegerField()
    usuario_gestion = models.IntegerField()
    usuario_destino = models.CharField(max_length=20)
    usuario_canal = models.CharField(max_length=50)
    usuario_anexo = models.CharField(max_length=5)
    usuario_duracion = models.DateTimeField()
    gestion_editid1 = models.CharField(max_length=100)
    gestion_editid2 = models.CharField(max_length=20)
    gestion_editid3 = models.CharField(max_length=200)
    gestion_editid4 = models.CharField(max_length=100)
    gestion_editid5 = models.CharField(max_length=20)
    gestion_editid6 = models.CharField(max_length=20)
    gestion_editid7 = models.CharField(max_length=20)
    gestion_editid8 = models.CharField(max_length=20)
    gestion_editid9 = models.CharField(max_length=20)
    gestion_editid10 = models.CharField(max_length=20)
    incall_cant = models.IntegerField()
    incall_dur = models.IntegerField()
    outcall_cant = models.IntegerField()
    outcall_dur = models.IntegerField()
    in_did = models.BigIntegerField(db_column='in_DID')  # Field name made lowercase.
    in_did2 = models.BigIntegerField()
    cod_int = models.CharField(max_length=11)
    gestion_editid11 = models.CharField(max_length=20)
    usuario_telefonia = models.IntegerField()
    flag_mon = models.IntegerField()
    audio = models.CharField(max_length=100)
    bill = models.IntegerField()
    id_ori_llamadas = models.IntegerField()
    acd = models.IntegerField()
    abandonada_in = models.IntegerField()
    abandonada_out = models.IntegerField()
    age_base = models.IntegerField()
    age_procesadas = models.IntegerField()
    age_pendientes = models.IntegerField()
    checa = models.IntegerField()
    tproyecto = models.CharField(db_column='tProyecto', max_length=20)  # Field name made lowercase.
    tbase = models.CharField(db_column='tBase', max_length=20)  # Field name made lowercase.
    est_ag_predictivo = models.IntegerField()
    contesta = models.IntegerField()
    no_contesta = models.IntegerField()
    colas = models.CharField(max_length=300)
    segmentos = models.CharField(max_length=300)
    skill = models.CharField(max_length=300)
    idusuario_servicio = models.IntegerField()
    kalive01 = models.IntegerField()
    kalive02 = models.IntegerField()
    en_pausa = models.TimeField()
    en_llamada = models.TimeField()
    libre = models.TimeField()
    acw = models.TimeField()
    en_pausa_cnt = models.IntegerField()
    en_llamada_cnt = models.IntegerField()
    libre_cnt = models.IntegerField()
    acw_cnt = models.IntegerField()
    tipo_disc = models.CharField(max_length=10)
    cose_tipo = models.IntegerField()
    cose_id = models.IntegerField()
    cose_valor = models.CharField(max_length=80)
    mod1 = models.IntegerField()
    mod2 = models.IntegerField()
    mod3 = models.IntegerField()
    mod4 = models.IntegerField()
    mod5 = models.IntegerField()
    mod6 = models.IntegerField()
    lis_camp = models.CharField(max_length=300)
    lis_rep = models.CharField(max_length=200)
    mod7 = models.IntegerField()
    mod8 = models.IntegerField()
    mod9 = models.IntegerField()
    mod10 = models.IntegerField()
    mod11 = models.IntegerField()
    mod12 = models.IntegerField()
    usuario_password = models.CharField(max_length=10)
    filtro_campag = models.IntegerField()
    id_chat = models.IntegerField()
    mod13 = models.IntegerField()
    mod14 = models.IntegerField()
    fecha_ingreso = models.DateTimeField()
    dni = models.CharField(max_length=8)
    supervisor = models.IntegerField()
    lis_super = models.CharField(max_length=2000)
    numero_llamado = models.BigIntegerField(db_column='Numero_Llamado')  # Field name made lowercase.
    categoria = models.CharField(max_length=7)
    age_intera = models.IntegerField()
    tie_intera = models.DateTimeField()
    tie_gestion = models.DateTimeField()
    tie_estado = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ori_usuario'
