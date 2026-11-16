-- MySQL dump 10.13  Distrib 8.4.9, for macos15 (arm64)
--
-- Host: localhost    Database: inventarioAventura
-- ------------------------------------------------------
-- Server version	8.4.9

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `inventarioAventura`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `inventarioAventura` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `inventarioAventura`;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add perfil',7,'add_perfil'),(26,'Can change perfil',7,'change_perfil'),(27,'Can delete perfil',7,'delete_perfil'),(28,'Can view perfil',7,'view_perfil'),(29,'Can add categoria',8,'add_categoria'),(30,'Can change categoria',8,'change_categoria'),(31,'Can delete categoria',8,'delete_categoria'),(32,'Can view categoria',8,'view_categoria'),(33,'Can add experiencia',9,'add_experiencia'),(34,'Can change experiencia',9,'change_experiencia'),(35,'Can delete experiencia',9,'delete_experiencia'),(36,'Can view experiencia',9,'view_experiencia'),(37,'Can add inscripcion',10,'add_inscripcion'),(38,'Can change inscripcion',10,'change_inscripcion'),(39,'Can delete inscripcion',10,'delete_inscripcion'),(40,'Can view inscripcion',10,'view_inscripcion');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$oBDMo1W153FwdlY6oKtsao$NOBWPyPdgEJEHEXTSOoB8iyeBfibgxd47GU6HrMOomg=','2026-11-16 18:59:55.499529',1,'admin','Ana','Administradora','admin@aventurasdelsur.cl',1,1,'2026-11-16 16:16:43.335614'),(2,'pbkdf2_sha256$600000$DaaE1yeuRDFG6s837JWPJe$pnleT4qWgUravYt0F/LfSqaCCi3n9vBSvY+uI9VMwjM=','2026-11-16 18:59:56.343512',0,'guia1','Camila','Rojas','guia1@aventurasdelsur.cl',0,1,'2026-11-16 16:16:43.532764'),(3,'pbkdf2_sha256$600000$sSkFcuXbUOU78LhBTkvIUX$KnWedtlcyTQKg8JQX1hq4VBMzpaJttJ++LyZ4BLugMM=',NULL,0,'guia2','Matías','Fuentes','guia2@aventurasdelsur.cl',0,1,'2026-11-16 16:16:43.723011'),(4,'pbkdf2_sha256$600000$CUKut6ZbYgrqghig3LJmnH$I4L9vZU6FR69uUpI69PmVQiQYf7khaWvZddxehUcrMI=','2026-11-16 18:59:56.105718',0,'turista1','Sofía','Pérez','turista1@aventurasdelsur.cl',0,1,'2026-11-16 16:16:43.911819'),(5,'pbkdf2_sha256$600000$36UNF6psZLXfv9i94MGwpE$Dk6bUtszc78vkVYukGtURWGMU8u3OPspalSIvz8Mfpw=',NULL,0,'turista2','Benjamín','Soto','turista2@aventurasdelsur.cl',0,1,'2026-11-16 16:16:44.110044');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cuentas_perfil`
--

DROP TABLE IF EXISTS `cuentas_perfil`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cuentas_perfil` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rol` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `telefono` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  `usuario_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario_id` (`usuario_id`),
  CONSTRAINT `cuentas_perfil_usuario_id_06f8a1e5_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cuentas_perfil`
--

LOCK TABLES `cuentas_perfil` WRITE;
/*!40000 ALTER TABLE `cuentas_perfil` DISABLE KEYS */;
INSERT INTO `cuentas_perfil` VALUES (1,'ADMIN','',1),(2,'GUIA','',2),(3,'GUIA','',3),(4,'TURISTA','',4),(5,'TURISTA','',5);
/*!40000 ALTER TABLE `cuentas_perfil` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'cuentas','perfil'),(8,'experiencias','categoria'),(9,'experiencias','experiencia'),(10,'experiencias','inscripcion'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2026-11-16 16:16:42.179552'),(2,'auth','0001_initial','2026-11-16 16:16:42.268668'),(3,'admin','0001_initial','2026-11-16 16:16:42.294168'),(4,'admin','0002_logentry_remove_auto_add','2026-11-16 16:16:42.297920'),(5,'admin','0003_logentry_add_action_flag_choices','2026-11-16 16:16:42.301197'),(6,'contenttypes','0002_remove_content_type_name','2026-11-16 16:16:42.378638'),(7,'auth','0002_alter_permission_name_max_length','2026-11-16 16:16:42.417758'),(8,'auth','0003_alter_user_email_max_length','2026-11-16 16:16:42.455767'),(9,'auth','0004_alter_user_username_opts','2026-11-16 16:16:42.474164'),(10,'auth','0005_alter_user_last_login_null','2026-11-16 16:16:42.516108'),(11,'auth','0006_require_contenttypes_0002','2026-11-16 16:16:42.519106'),(12,'auth','0007_alter_validators_add_error_messages','2026-11-16 16:16:42.528439'),(13,'auth','0008_alter_user_username_max_length','2026-11-16 16:16:42.553508'),(14,'auth','0009_alter_user_last_name_max_length','2026-11-16 16:16:42.601940'),(15,'auth','0010_alter_group_name_max_length','2026-11-16 16:16:42.609971'),(16,'auth','0011_update_proxy_permissions','2026-11-16 16:16:42.614192'),(17,'auth','0012_alter_user_first_name_max_length','2026-11-16 16:16:42.633686'),(18,'cuentas','0001_initial','2026-11-16 16:16:42.653027'),(19,'experiencias','0001_initial','2026-11-16 16:16:42.718178'),(20,'sessions','0001_initial','2026-11-16 16:16:42.724368');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `experiencias_categoria`
--

DROP TABLE IF EXISTS `experiencias_categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `experiencias_categoria` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `activo` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `experiencias_categoria`
--

LOCK TABLES `experiencias_categoria` WRITE;
/*!40000 ALTER TABLE `experiencias_categoria` DISABLE KEYS */;
INSERT INTO `experiencias_categoria` VALUES (1,'Trekking','Caminatas guiadas por senderos del bosque nativo.',1),(2,'Canopy','Recorridos en tirolesa sobre el dosel del bosque.',1),(3,'Kayak','Navegación por la laguna y el río.',1),(4,'Arriendo de equipos','Bicicletas, carpas y equipo de camping.',1),(5,'Observación de aves','Temporada cerrada (ejemplo de categoría inactiva).',0);
/*!40000 ALTER TABLE `experiencias_categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `experiencias_experiencia`
--

DROP TABLE IF EXISTS `experiencias_experiencia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `experiencias_experiencia` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `titulo` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `precio` int unsigned NOT NULL,
  `cupo_maximo` int unsigned NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `activa` tinyint(1) NOT NULL,
  `categoria_id` bigint NOT NULL,
  `creador_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `experiencias_experie_categoria_id_b03f452f_fk_experienc` (`categoria_id`),
  KEY `experiencias_experiencia_creador_id_70b19025_fk_auth_user_id` (`creador_id`),
  CONSTRAINT `experiencias_experie_categoria_id_b03f452f_fk_experienc` FOREIGN KEY (`categoria_id`) REFERENCES `experiencias_categoria` (`id`),
  CONSTRAINT `experiencias_experiencia_creador_id_70b19025_fk_auth_user_id` FOREIGN KEY (`creador_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `experiencias_experiencia_chk_1` CHECK ((`precio` >= 0)),
  CONSTRAINT `experiencias_experiencia_chk_2` CHECK ((`cupo_maximo` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `experiencias_experiencia`
--

LOCK TABLES `experiencias_experiencia` WRITE;
/*!40000 ALTER TABLE `experiencias_experiencia` DISABLE KEYS */;
INSERT INTO `experiencias_experiencia` VALUES (1,'Trekking Cerro El Mirador','Trekking Cerro El Mirador: experiencia al aire libre guiada por personal del ecoparque.',15000,12,'2026-11-21 12:00:00.000000',1,1,2),(2,'Sendero Cascadas Escondidas','Sendero Cascadas Escondidas: experiencia al aire libre guiada por personal del ecoparque.',18000,10,'2026-11-25 11:00:00.000000',1,1,2),(3,'Canopy Bosque Nativo','Canopy Bosque Nativo: experiencia al aire libre guiada por personal del ecoparque.',25000,8,'2026-11-28 14:00:00.000000',1,2,2),(4,'Arriendo de bicicletas (día completo)','Arriendo de bicicletas (día completo): experiencia al aire libre guiada por personal del ecoparque.',12000,20,'2026-11-19 13:00:00.000000',1,4,2),(5,'Kayak Laguna Verde','Kayak Laguna Verde: experiencia al aire libre guiada por personal del ecoparque.',22000,6,'2026-11-23 13:00:00.000000',1,3,3),(6,'Kayak nocturno con linternas','Kayak nocturno con linternas: experiencia al aire libre guiada por personal del ecoparque.',28000,6,'2026-11-30 23:00:00.000000',1,3,3),(7,'Canopy Extremo 7 Líneas','Canopy Extremo 7 Líneas: experiencia al aire libre guiada por personal del ecoparque.',32000,10,'2026-11-26 18:00:00.000000',1,2,3),(8,'Arriendo equipo de camping','Arriendo equipo de camping: experiencia al aire libre guiada por personal del ecoparque.',20000,15,'2026-11-20 15:00:00.000000',1,4,3);
/*!40000 ALTER TABLE `experiencias_experiencia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `experiencias_inscripcion`
--

DROP TABLE IF EXISTS `experiencias_inscripcion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `experiencias_inscripcion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fecha_inscripcion` datetime(6) NOT NULL,
  `estado_pago` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `experiencia_id` bigint NOT NULL,
  `usuario_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `inscripcion_unica` (`usuario_id`,`experiencia_id`),
  KEY `experiencias_inscrip_experiencia_id_2fbecc6b_fk_experienc` (`experiencia_id`),
  CONSTRAINT `experiencias_inscrip_experiencia_id_2fbecc6b_fk_experienc` FOREIGN KEY (`experiencia_id`) REFERENCES `experiencias_experiencia` (`id`),
  CONSTRAINT `experiencias_inscripcion_usuario_id_9d6f5da2_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `experiencias_inscripcion`
--

LOCK TABLES `experiencias_inscripcion` WRITE;
/*!40000 ALTER TABLE `experiencias_inscripcion` DISABLE KEYS */;
INSERT INTO `experiencias_inscripcion` VALUES (1,'2026-11-16 16:16:44.315551','CONFIRMADO',1,4),(2,'2026-11-16 16:16:44.316566','PENDIENTE',3,4),(3,'2026-11-16 16:16:44.317521','PENDIENTE',5,4),(4,'2026-11-16 16:16:44.318482','CONFIRMADO',2,5),(5,'2026-11-16 16:16:44.319605','PENDIENTE',5,5),(6,'2026-11-16 16:16:44.320754','PENDIENTE',7,5);
/*!40000 ALTER TABLE `experiencias_inscripcion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'inventarioAventura'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-11-16 16:00:38
