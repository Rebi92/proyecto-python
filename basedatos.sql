CREATE DATABASE IF NOT EXISTS master_python;
USE master_python;

/* el proyecto tiene dos tablas una usuarios y otra de las notas */

CREATE TABLE usuarios(
    id          int(255) AUTO_INCREMENT not NULL,
    nombre      VARCHAR (100),
    apellidos   VARCHAR (255),
    email       VARCHAR(255) not NULL ,
    password    VARCHAR(255) NOT NULL,
    fecha       date not NULL ,
    CONSTRAINT pk_usuarios PRIMARY KEY(id), /* clave primaria */
    CONSTRAINT uq_email UNIQUE(email) /* campo unico */
)ENGINE=InnoDb;

CREATE TABLE notas(
    id          int(25) AUTO_INCREMENT NOT  NULL ,
    usuario_id  int(25) NOT NULL,
    titulo      VARCHAR (255) not null,
    descripcion MEDIUMTEXT,
    fecha       date not NULL,
    CONSTRAINT pk_notas PRIMARY KEY(id),
    CONSTRAINT fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id),
    )ENGINE=InnoDb;