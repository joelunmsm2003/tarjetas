# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Accion(models.Model):
    nombre = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accion'


class BasePrueba(models.Model):
    id_orig_base1 = models.IntegerField()
    id_orig_base = models.AutoField(primary_key=True)
    nombre_orig_base = models.CharField(max_length=50, blank=True, null=True)
    telefono_orig_base = models.IntegerField(blank=True, null=True)
    direccion_orig_base = models.CharField(max_length=50, blank=True, null=True)
    provincia_orig_base = models.CharField(max_length=20, blank=True, null=True)
    localidad_orig_base = models.CharField(max_length=10, blank=True, null=True)
    cpostal_orig_base = models.IntegerField(db_column='Cpostal_orig_base', blank=True, null=True)  # Field name made lowercase.
    res_gestion_orig_base = models.CharField(max_length=10, blank=True, null=True)
    observ_orig_base = models.CharField(max_length=500, blank=True, null=True)
    fmagenda_orig_base = models.CharField(db_column='FMagenda_orig_base', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lestado = models.IntegerField(db_column='lEstado')  # Field name made lowercase.
    id_campana = models.IntegerField(db_column='ID_Campana')  # Field name made lowercase.
    llam_estado = models.IntegerField()
    id_ori_usuario = models.IntegerField()
    fechaproceso = models.DateTimeField()
    pre_flag = models.IntegerField()
    pre_estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'base_prueba'


class Contacto(models.Model):
    nombre = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacto'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Estado(models.Model):
    nombre = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado'


class Lote(models.Model):
    file = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lote'


class OrigBase(models.Model):
    id_orig_base = models.AutoField(primary_key=True)
    telefono = models.IntegerField(blank=True, null=True)
    orden = models.IntegerField()
    cliente = models.CharField(max_length=100)
    id_orig_base_c = models.IntegerField(db_column='id_orig_base_C', blank=True, null=True)  # Field name made lowercase.
    lestado = models.IntegerField(db_column='lEstado')  # Field name made lowercase.
    cod_cam = models.IntegerField()
    llam_estado = models.IntegerField()
    id_ori_usuario = models.IntegerField()
    fechaproceso = models.DateTimeField()
    pre_flag = models.IntegerField()
    pre_estado = models.IntegerField()
    nombre_agente = models.CharField(max_length=100, blank=True, null=True)
    contacto = models.IntegerField(blank=True, null=True)
    accion = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    fagenda = models.DateTimeField(blank=True, null=True)
    observacion = models.CharField(max_length=300, blank=True, null=True)
    fgestion = models.DateTimeField(blank=True, null=True)
    tadicional = models.CharField(max_length=100, blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orig_base'


class OrigBase1(models.Model):
    id_orig_base = models.AutoField(primary_key=True)
    nombre_orig_base = models.CharField(max_length=50, blank=True, null=True)
    telefono_orig_base = models.IntegerField(blank=True, null=True)
    direccion_orig_base = models.CharField(max_length=50, blank=True, null=True)
    provincia_orig_base = models.CharField(max_length=20, blank=True, null=True)
    localidad_orig_base = models.CharField(max_length=10, blank=True, null=True)
    cpostal_orig_base = models.IntegerField(db_column='Cpostal_orig_base', blank=True, null=True)  # Field name made lowercase.
    res_gestion_orig_base = models.CharField(max_length=10, blank=True, null=True)
    observ_orig_base = models.CharField(max_length=500, blank=True, null=True)
    fmagenda_orig_base = models.CharField(db_column='FMagenda_orig_base', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lestado = models.IntegerField(db_column='lEstado')  # Field name made lowercase.
    id_campana = models.IntegerField(db_column='ID_Campana')  # Field name made lowercase.
    llam_estado = models.IntegerField()
    id_ori_usuario = models.IntegerField()
    fechaproceso = models.DateTimeField()
    pre_flag = models.IntegerField()
    pre_estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orig_base1'


class OrigBaseC01(models.Model):
    fecha_recepcion_bbdd = models.CharField(db_column='FECHA_RECEPCION_BBDD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    call = models.CharField(db_column='CALL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fecha = models.CharField(db_column='FECHA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='APELLIDO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dni = models.CharField(db_column='DNI', max_length=100, blank=True, null=True)  # Field name made lowercase.
    plan_cobertura = models.CharField(db_column='PLAN_COBERTURA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='DIRECCION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    distrito = models.CharField(db_column='DISTRITO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    provincia = models.CharField(db_column='PROVINCIA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    departamento = models.CharField(db_column='DEPARTAMENTO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    zona = models.CharField(db_column='ZONA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono1 = models.CharField(db_column='TELEFONO1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono2 = models.CharField(db_column='TELEFONO2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mail = models.CharField(db_column='MAIL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tipo_envio = models.CharField(db_column='TIPO_ENVIO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    campana = models.CharField(db_column='CAMPANA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    comercial = models.CharField(db_column='COMERCIAL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cobertura = models.CharField(db_column='COBERTURA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cant_afiliados = models.CharField(db_column='CANT_AFILIADOS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fecha_nacimiento = models.CharField(db_column='FECHA_NACIMIENTO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pap = models.CharField(db_column='PAP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tipo_tarjeta = models.CharField(db_column='TIPO_TARJETA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono3 = models.CharField(db_column='TELEFONO3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono4 = models.CharField(db_column='TELEFONO4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono5 = models.CharField(db_column='TELEFONO5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono6 = models.CharField(db_column='TELEFONO6', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono7 = models.CharField(db_column='TELEFONO7', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefonofijo = models.IntegerField(db_column='TELEFONOFIJO', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='OBSERVACIONES', max_length=100, blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    prima_mensual = models.CharField(db_column='PRIMA_MENSUAL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    todo_prima = models.CharField(db_column='TODO_PRIMA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cod_cam = models.IntegerField()
    lote = models.IntegerField()
    id = models.AutoField()
    t_ins = models.DateTimeField(db_column='T_INS')  # Field name made lowercase.
    flagdesplegar = models.IntegerField(db_column='flagDesplegar')  # Field name made lowercase.
    flag = models.IntegerField()
    cantidad = models.IntegerField(db_column='CANTIDAD', blank=True, null=True)  # Field name made lowercase.
    nombredelproducto = models.CharField(db_column='NOMBREDELPRODUCTO', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tipodecobertura = models.CharField(db_column='TIPODECOBERTURA', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tipodedocumento = models.CharField(db_column='TIPODEDOCUMENTO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nrotarjetaencriptada = models.CharField(db_column='NROTARJETAENCRIPTADA', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tienetarjetadecredito = models.CharField(db_column='TIENETARJETADECREDITO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tarjetasadicionales = models.CharField(db_column='TARJETASADICIONALES', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    recibects = models.CharField(db_column='RECIBECTS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    facebook = models.CharField(max_length=100, blank=True, null=True)
    tienelpdp = models.CharField(db_column='TIENELPDP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fecha_vencimiento = models.CharField(max_length=1000, blank=True, null=True)
    nombre_agente = models.CharField(max_length=1000, blank=True, null=True)
    observacion = models.CharField(max_length=1000, blank=True, null=True)
    contacto = models.IntegerField(blank=True, null=True)
    deacuerdo = models.CharField(max_length=100, blank=True, null=True)
    accion = models.IntegerField(blank=True, null=True)
    fecha_actualizar_bbva = models.DateTimeField(blank=True, null=True)
    fecha_venta_bbva = models.DateTimeField(blank=True, null=True)
    fecha_tipifica_bbva = models.DateTimeField(blank=True, null=True)
    audio = models.CharField(max_length=100, blank=True, null=True)
    fagenda = models.DateTimeField(blank=True, null=True)
    usuario_anexo = models.CharField(max_length=1000, blank=True, null=True)
    tarjetacredito = models.CharField(max_length=10000, blank=True, null=True)
    sexo = models.CharField(max_length=10, blank=True, null=True)
    codigoautorizacion = models.CharField(max_length=1000, blank=True, null=True)
    primernombre = models.CharField(max_length=1000, blank=True, null=True)
    fechaefectividad = models.CharField(max_length=100, blank=True, null=True)
    segundonombre = models.CharField(max_length=1000, blank=True, null=True)
    apellidos = models.CharField(max_length=1000, blank=True, null=True)
    pregunta1 = models.CharField(max_length=100, blank=True, null=True)
    pregunta2 = models.CharField(max_length=100, blank=True, null=True)
    pregunta3 = models.CharField(max_length=100, blank=True, null=True)
    pregunta4 = models.CharField(max_length=100, blank=True, null=True)
    ticket = models.CharField(max_length=10000, blank=True, null=True)
    audiofinal = models.CharField(max_length=1000, blank=True, null=True)
    id_unique = models.IntegerField(unique=True, blank=True, null=True)
    cod_interno = models.CharField(max_length=100, blank=True, null=True)
    ape_paterno = models.CharField(max_length=100, blank=True, null=True)
    ape_materno = models.CharField(max_length=100, blank=True, null=True)
    cic_facturacion = models.CharField(max_length=100, blank=True, null=True)
    tip_direc = models.CharField(max_length=100, blank=True, null=True)
    est_direc = models.CharField(max_length=100, blank=True, null=True)
    tip_via = models.CharField(max_length=100, blank=True, null=True)
    nom_via = models.CharField(max_length=100, blank=True, null=True)
    nro_dom = models.CharField(max_length=100, blank=True, null=True)
    tip_edif = models.CharField(max_length=100, blank=True, null=True)
    nom_edif = models.CharField(max_length=100, blank=True, null=True)
    tip_piso = models.CharField(max_length=100, blank=True, null=True)
    nom_piso = models.CharField(max_length=100, blank=True, null=True)
    tip_comuna = models.CharField(max_length=100, blank=True, null=True)
    nom_comuna = models.CharField(max_length=100, blank=True, null=True)
    num_mzn = models.CharField(max_length=100, blank=True, null=True)
    num_lote = models.CharField(max_length=100, blank=True, null=True)
    tip_zona = models.CharField(max_length=100, blank=True, null=True)
    nom_zona = models.CharField(max_length=100, blank=True, null=True)
    ubigeo = models.CharField(max_length=100, blank=True, null=True)
    des_ubigeo = models.CharField(max_length=100, blank=True, null=True)
    ref_direc = models.CharField(max_length=100, blank=True, null=True)
    celular = models.CharField(max_length=100, blank=True, null=True)
    trabajo = models.CharField(max_length=100, blank=True, null=True)
    flagmp3 = models.IntegerField(db_column='flagMP3', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orig_base_C01'


class OrigBaseC01280417(models.Model):
    fecha_recepcion_bbdd = models.CharField(db_column='FECHA_RECEPCION_BBDD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    call = models.CharField(db_column='CALL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fecha = models.CharField(db_column='FECHA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='APELLIDO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dni = models.CharField(db_column='DNI', max_length=100, blank=True, null=True)  # Field name made lowercase.
    plan_cobertura = models.CharField(db_column='PLAN_COBERTURA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='DIRECCION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    distrito = models.CharField(db_column='DISTRITO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    provincia = models.CharField(db_column='PROVINCIA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    departamento = models.CharField(db_column='DEPARTAMENTO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    zona = models.CharField(db_column='ZONA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono1 = models.CharField(db_column='TELEFONO1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono2 = models.CharField(db_column='TELEFONO2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mail = models.CharField(db_column='MAIL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tipo_envio = models.CharField(db_column='TIPO_ENVIO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    campana = models.CharField(db_column='CAMPANA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    comercial = models.CharField(db_column='COMERCIAL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cobertura = models.CharField(db_column='COBERTURA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cant_afiliados = models.CharField(db_column='CANT_AFILIADOS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fecha_nacimiento = models.CharField(db_column='FECHA_NACIMIENTO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pap = models.CharField(db_column='PAP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tipo_tarjeta = models.CharField(db_column='TIPO_TARJETA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono3 = models.CharField(db_column='TELEFONO3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono4 = models.CharField(db_column='TELEFONO4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono5 = models.CharField(db_column='TELEFONO5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono6 = models.CharField(db_column='TELEFONO6', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono7 = models.CharField(db_column='TELEFONO7', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefonofijo = models.IntegerField(db_column='TELEFONOFIJO', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='OBSERVACIONES', max_length=100, blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    prima_mensual = models.CharField(db_column='PRIMA_MENSUAL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    todo_prima = models.CharField(db_column='TODO_PRIMA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cod_cam = models.IntegerField()
    lote = models.IntegerField()
    id = models.AutoField()
    t_ins = models.DateTimeField(db_column='T_INS')  # Field name made lowercase.
    flagdesplegar = models.IntegerField(db_column='flagDesplegar')  # Field name made lowercase.
    flag = models.IntegerField()
    cantidad = models.IntegerField(db_column='CANTIDAD', blank=True, null=True)  # Field name made lowercase.
    nombredelproducto = models.CharField(db_column='NOMBREDELPRODUCTO', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tipodecobertura = models.CharField(db_column='TIPODECOBERTURA', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tipodedocumento = models.CharField(db_column='TIPODEDOCUMENTO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nrotarjetaencriptada = models.CharField(db_column='NROTARJETAENCRIPTADA', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tienetarjetadecredito = models.CharField(db_column='TIENETARJETADECREDITO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tarjetasadicionales = models.CharField(db_column='TARJETASADICIONALES', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    recibects = models.CharField(db_column='RECIBECTS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    facebook = models.CharField(max_length=100, blank=True, null=True)
    tienelpdp = models.CharField(db_column='TIENELPDP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fecha_vencimiento = models.CharField(max_length=1000, blank=True, null=True)
    nombre_agente = models.CharField(max_length=1000, blank=True, null=True)
    observacion = models.CharField(max_length=1000, blank=True, null=True)
    contacto = models.IntegerField(blank=True, null=True)
    deacuerdo = models.CharField(max_length=100, blank=True, null=True)
    accion = models.IntegerField(blank=True, null=True)
    fecha_actualizar_bbva = models.DateTimeField(blank=True, null=True)
    fecha_venta_bbva = models.DateTimeField(blank=True, null=True)
    fecha_tipifica_bbva = models.DateTimeField(blank=True, null=True)
    audio = models.CharField(max_length=100, blank=True, null=True)
    fagenda = models.DateTimeField(blank=True, null=True)
    usuario_anexo = models.CharField(max_length=1000, blank=True, null=True)
    tarjetacredito = models.CharField(max_length=10000, blank=True, null=True)
    sexo = models.CharField(max_length=10, blank=True, null=True)
    codigoautorizacion = models.CharField(max_length=1000, blank=True, null=True)
    primernombre = models.CharField(max_length=1000, blank=True, null=True)
    fechaefectividad = models.CharField(max_length=100, blank=True, null=True)
    segundonombre = models.CharField(max_length=1000, blank=True, null=True)
    apellidos = models.CharField(max_length=1000, blank=True, null=True)
    pregunta1 = models.CharField(max_length=100, blank=True, null=True)
    pregunta2 = models.CharField(max_length=100, blank=True, null=True)
    pregunta3 = models.CharField(max_length=100, blank=True, null=True)
    pregunta4 = models.CharField(max_length=100, blank=True, null=True)
    ticket = models.CharField(max_length=10000, blank=True, null=True)
    audiofinal = models.CharField(max_length=1000, blank=True, null=True)
    id_unique = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orig_base_C01_280417'


class OrigBaseC01X(models.Model):
    fecha_recepcion_bbdd = models.CharField(db_column='FECHA_RECEPCION_BBDD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    call = models.CharField(db_column='CALL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fecha = models.CharField(db_column='FECHA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='APELLIDO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dni = models.CharField(db_column='DNI', max_length=100, blank=True, null=True)  # Field name made lowercase.
    plan_cobertura = models.CharField(db_column='PLAN_COBERTURA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='DIRECCION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    distrito = models.CharField(db_column='DISTRITO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    provincia = models.CharField(db_column='PROVINCIA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    departamento = models.CharField(db_column='DEPARTAMENTO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    zona = models.CharField(db_column='ZONA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono1 = models.CharField(db_column='TELEFONO1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono2 = models.CharField(db_column='TELEFONO2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mail = models.CharField(db_column='MAIL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tipo_envio = models.CharField(db_column='TIPO_ENVIO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    campana = models.CharField(db_column='CAMPANA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    comercial = models.CharField(db_column='COMERCIAL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cobertura = models.CharField(db_column='COBERTURA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cant_afiliados = models.CharField(db_column='CANT_AFILIADOS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fecha_nacimiento = models.CharField(db_column='FECHA_NACIMIENTO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pap = models.CharField(db_column='PAP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tipo_tarjeta = models.CharField(db_column='TIPO_TARJETA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono3 = models.CharField(db_column='TELEFONO3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono4 = models.CharField(db_column='TELEFONO4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono5 = models.CharField(db_column='TELEFONO5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono6 = models.CharField(db_column='TELEFONO6', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono7 = models.CharField(db_column='TELEFONO7', max_length=100, blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='OBSERVACIONES', max_length=100, blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    prima_mensual = models.CharField(db_column='PRIMA_MENSUAL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    todo_prima = models.CharField(db_column='TODO_PRIMA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(unique=True)
    cod_cam = models.IntegerField()
    lote = models.IntegerField()
    t_ins = models.DateTimeField(db_column='T_INS')  # Field name made lowercase.
    flagdesplegar = models.IntegerField(db_column='flagDesplegar')  # Field name made lowercase.
    flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orig_base_C01_x'


class OrigBaseCopia(models.Model):
    id_orig_base = models.AutoField(primary_key=True)
    telefono = models.IntegerField(blank=True, null=True)
    orden = models.IntegerField()
    cliente = models.CharField(max_length=11)
    id_orig_base_c = models.IntegerField(db_column='id_orig_base_C', blank=True, null=True)  # Field name made lowercase.
    lestado = models.IntegerField(db_column='lEstado')  # Field name made lowercase.
    cod_cam = models.IntegerField()
    llam_estado = models.IntegerField()
    id_ori_usuario = models.IntegerField()
    fechaproceso = models.DateTimeField()
    pre_flag = models.IntegerField()
    pre_estado = models.IntegerField()
    nombre_agente = models.CharField(max_length=100, blank=True, null=True)
    contacto = models.IntegerField(blank=True, null=True)
    accion = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    fagenda = models.DateTimeField(blank=True, null=True)
    observacion = models.CharField(max_length=300, blank=True, null=True)
    fgestion = models.DateTimeField(blank=True, null=True)
    tadicional = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orig_base_copia'


class OrigResulta(models.Model):
    id_resulta = models.AutoField(db_column='id_resultA', primary_key=True)  # Field name made lowercase.
    id_ori_usuario = models.IntegerField()
    id_ori_campana = models.IntegerField()
    id_orig_base = models.IntegerField()
    fecha = models.DateTimeField()
    nombre_orig_resulta = models.CharField(db_column='nombre_orig_resultA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    apellido_orig_resulta = models.CharField(db_column='apellido_orig_resultA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    apoderado_orig_resulta = models.CharField(db_column='apoderado_orig_resultA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    docid_orig_resulta = models.CharField(db_column='docid_orig_resultA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ndocid_orig_resulta = models.CharField(db_column='Ndocid_orig_resultA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    calle_orig_resulta = models.CharField(db_column='calle_orig_resultA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ncalle_orig_resulta = models.CharField(db_column='Ncalle_orig_resultA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pisletra_orig_resulta = models.CharField(db_column='pisletra_orig_resultA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    localidad_orig_resulta = models.CharField(db_column='localidad_orig_resultA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    provincia_orig_resulta = models.CharField(db_column='provincia_orig_resultA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cpostal_orig_resulta = models.IntegerField(db_column='Cpostal_orig_resultA', blank=True, null=True)  # Field name made lowercase.
    perscontac_orig_resulta = models.CharField(db_column='perscontac_orig_resultA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fechanac_orig_resulta = models.IntegerField(db_column='fechanac_orig_resultA', blank=True, null=True)  # Field name made lowercase.
    telefonof_orig_resulta = models.IntegerField(db_column='telefonoF_orig_resultA', blank=True, null=True)  # Field name made lowercase.
    telefonom_orig_resulta = models.IntegerField(db_column='telefonoM_orig_resultA', blank=True, null=True)  # Field name made lowercase.
    email_orig_resulta = models.CharField(db_column='email_orig_resultA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nomban_orig_resulta = models.CharField(db_column='NomBAN_orig_resultA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    titcuenta_orig_resulta = models.CharField(db_column='titcuenta_orig_resultA', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ncuenta_orig_resulta = models.CharField(db_column='Ncuenta_orig_resultA', max_length=500, blank=True, null=True)  # Field name made lowercase.
    plan_orig_resulta = models.CharField(db_column='plan_orig_resultA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    telefr_orig_resulta = models.CharField(db_column='telefR_orig_resultA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    adsl_orig_resulta = models.CharField(db_column='ADSL_orig_resultA', max_length=500, blank=True, null=True)  # Field name made lowercase.
    compa_ia_orig_resulta = models.CharField(db_column='compa\xf1ia_orig_resultA', max_length=500, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jaztel_orig_resulta = models.CharField(db_column='jaztel_orig_resultA', max_length=500, blank=True, null=True)  # Field name made lowercase.
    direcr_orig_resulta = models.CharField(db_column='direcR_orig_resultA', max_length=500, blank=True, null=True)  # Field name made lowercase.
    direcrinst_orig_resulta = models.CharField(db_column='direcRinst_orig_resultA', max_length=500, blank=True, null=True)  # Field name made lowercase.
    guias_orig_resulta = models.CharField(db_column='guias_orig_resultA', max_length=500, blank=True, null=True)  # Field name made lowercase.
    secion_orig_resulta = models.CharField(db_column='secion_orig_resultA', max_length=500, blank=True, null=True)  # Field name made lowercase.
    hora_orig_resulta = models.CharField(db_column='hora_orig_resultA', max_length=500, blank=True, null=True)  # Field name made lowercase.
    protabilidad_orig_resulta = models.CharField(db_column='protabilidad_orig_resultA', max_length=500, blank=True, null=True)  # Field name made lowercase.
    tecnico_orig_resulta = models.CharField(db_column='tecnico_orig_resultA', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orig_resultA'


class Rellamadas(models.Model):
    id_rellamadas = models.AutoField(primary_key=True)
    tproyecto = models.CharField(db_column='tProyecto', max_length=6)  # Field name made lowercase.
    tregistro = models.IntegerField(db_column='tRegistro')  # Field name made lowercase.
    tresultado = models.CharField(db_column='tResultado', max_length=2)  # Field name made lowercase.
    tcodigo = models.CharField(db_column='tCodigo', max_length=5)  # Field name made lowercase.
    ffechar = models.DateField(db_column='fFechaR')  # Field name made lowercase.
    fhorar = models.TimeField(db_column='fHoraR')  # Field name made lowercase.
    ffecha = models.DateTimeField(db_column='fFecha')  # Field name made lowercase.
    tusuario = models.CharField(db_column='tUsuario', max_length=15)  # Field name made lowercase.
    lestado = models.IntegerField(db_column='lEstado')  # Field name made lowercase.
    ttelefono = models.CharField(db_column='tTelefono', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rellamadas'


class Ticket(models.Model):
    numero = models.CharField(max_length=10000, blank=True, null=True)
    dni = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    base = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket'


class Tipificacion(models.Model):
    contacto = models.ForeignKey(Contacto, models.DO_NOTHING, db_column='contacto', blank=True, null=True)
    accion = models.ForeignKey(Accion, models.DO_NOTHING, db_column='accion', blank=True, null=True)
    estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='estado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipificacion'


class Ubigeo(models.Model):
    departamento = models.CharField(max_length=1000, blank=True, null=True)
    cod_departamento = models.CharField(max_length=100, blank=True, null=True)
    provincia = models.CharField(max_length=1000, blank=True, null=True)
    cod_provincia = models.CharField(max_length=100, blank=True, null=True)
    distrito = models.CharField(max_length=1000, blank=True, null=True)
    cod_distrito = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ubigeo'


class Ventarecupero(models.Model):
    fecha_recepcion_bbdd = models.CharField(db_column='FECHA_RECEPCION_BBDD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    call = models.CharField(db_column='CALL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fecha = models.CharField(db_column='FECHA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='APELLIDO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dni = models.CharField(db_column='DNI', max_length=100, blank=True, null=True)  # Field name made lowercase.
    plan_cobertura = models.CharField(db_column='PLAN_COBERTURA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='DIRECCION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    distrito = models.CharField(db_column='DISTRITO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    provincia = models.CharField(db_column='PROVINCIA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    departamento = models.CharField(db_column='DEPARTAMENTO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    zona = models.CharField(db_column='ZONA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono1 = models.CharField(db_column='TELEFONO1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono2 = models.CharField(db_column='TELEFONO2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mail = models.CharField(db_column='MAIL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tipo_envio = models.CharField(db_column='TIPO_ENVIO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    campana = models.CharField(db_column='CAMPANA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    comercial = models.CharField(db_column='COMERCIAL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cobertura = models.CharField(db_column='COBERTURA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cant_afiliados = models.CharField(db_column='CANT_AFILIADOS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fecha_nacimiento = models.CharField(db_column='FECHA_NACIMIENTO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pap = models.CharField(db_column='PAP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tipo_tarjeta = models.CharField(db_column='TIPO_TARJETA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono3 = models.CharField(db_column='TELEFONO3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono4 = models.CharField(db_column='TELEFONO4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono5 = models.CharField(db_column='TELEFONO5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono6 = models.CharField(db_column='TELEFONO6', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono7 = models.CharField(db_column='TELEFONO7', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefonofijo = models.IntegerField(db_column='TELEFONOFIJO', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='OBSERVACIONES', max_length=100, blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    prima_mensual = models.CharField(db_column='PRIMA_MENSUAL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    todo_prima = models.CharField(db_column='TODO_PRIMA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cod_cam = models.IntegerField()
    lote = models.IntegerField()
    id = models.AutoField()
    t_ins = models.DateTimeField(db_column='T_INS', blank=True, null=True)  # Field name made lowercase.
    flagdesplegar = models.IntegerField(db_column='flagDesplegar', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(blank=True, null=True)
    cantidad = models.IntegerField(db_column='CANTIDAD', blank=True, null=True)  # Field name made lowercase.
    nombredelproducto = models.CharField(db_column='NOMBREDELPRODUCTO', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tipodecobertura = models.CharField(db_column='TIPODECOBERTURA', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tipodedocumento = models.CharField(db_column='TIPODEDOCUMENTO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nrotarjetaencriptada = models.CharField(db_column='NROTARJETAENCRIPTADA', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tienetarjetadecredito = models.CharField(db_column='TIENETARJETADECREDITO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tarjetasadicionales = models.CharField(db_column='TARJETASADICIONALES', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    recibects = models.CharField(db_column='RECIBECTS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    facebook = models.CharField(max_length=100, blank=True, null=True)
    tienelpdp = models.CharField(db_column='TIENELPDP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fecha_vencimiento = models.CharField(max_length=1000, blank=True, null=True)
    nombre_agente = models.CharField(max_length=1000, blank=True, null=True)
    observacion = models.CharField(max_length=1000, blank=True, null=True)
    contacto = models.IntegerField(blank=True, null=True)
    deacuerdo = models.CharField(max_length=100, blank=True, null=True)
    accion = models.IntegerField(blank=True, null=True)
    fecha_actualizar_bbva = models.DateTimeField(blank=True, null=True)
    fecha_venta_bbva = models.DateTimeField(blank=True, null=True)
    fecha_tipifica_bbva = models.DateTimeField(blank=True, null=True)
    audio = models.CharField(max_length=100, blank=True, null=True)
    fagenda = models.DateTimeField(blank=True, null=True)
    usuario_anexo = models.CharField(max_length=1000, blank=True, null=True)
    tarjetacredito = models.CharField(max_length=10000, blank=True, null=True)
    sexo = models.CharField(max_length=10, blank=True, null=True)
    codigoautorizacion = models.CharField(max_length=1000, blank=True, null=True)
    primernombre = models.CharField(max_length=1000, blank=True, null=True)
    fechaefectividad = models.CharField(max_length=100, blank=True, null=True)
    segundonombre = models.CharField(max_length=1000, blank=True, null=True)
    apellidos = models.CharField(max_length=1000, blank=True, null=True)
    pregunta1 = models.CharField(max_length=100, blank=True, null=True)
    pregunta2 = models.CharField(max_length=100, blank=True, null=True)
    pregunta3 = models.CharField(max_length=100, blank=True, null=True)
    pregunta4 = models.CharField(max_length=100, blank=True, null=True)
    bbva = models.IntegerField(blank=True, null=True)
    audiofinal = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ventarecupero'
