/* MODELAGEM FÍSICA */

/* CRIAR BANCO DE DADOS*/
CREATE DATABASE PROJETO;

/* CONECTAR AO BANCO DE DADOS */
USE PROJETO;

/* CRIAR TABELA */
CREATE TABLE CLIENTE(
    NOME VARCHAR(30),
    SEXO CHAR(1),
    EMAIL VARCHAR(30),
    CPF INT(11),
    TELEFONE VARCHAR(30),
    ENDERECO VARCHAR(100)
);

/* CONSULTAR TABELAS */
SHOW TABLES;

/* CONSULTAR ESTRUTURAS DE TABELAS */
DESC CLIENTE;

/* INSERIR DADOS NA TABELA */
/* OMITINDO COLUNAS*/
INSERT INTO CLIENTE VALUES('JOHN DOE', 'M', NULL, 123456789, '123456789', 'JOHN DOE HOUSE STREET - NEW YORK - USA');

/* NÃO OMITINDO COLUNAS */
INSERT INTO CLIENTE(NOME, SEXO, ENDERECO, TELEFONE, CPF) VALUES('JOHN DOE', 'M', 'JOHN DOE HOUSE STREET - NEW YORK - USA', '123456789', 123456789, '123456789');

/* CONSULTAR DADOS */