-- MySQL dump 10.13  Distrib 5.5.50, for Win32 (x86)
--
-- Host: localhost    Database: my_travel_db
-- ------------------------------------------------------
-- Server version	5.5.50

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `pwd` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'mr','pbkdf2:sha256:260000$cZEDq6Hnqdi4G0Zr$87a4ac78ba41ff0ca80c7df2f50b3ccd950cc22f6b954f5be2a6b502bbd39094');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `adminlog`
--

DROP TABLE IF EXISTS `adminlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `adminlog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `admin_id` int(11) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_adminlog_addtime` (`addtime`),
  KEY `admin_id` (`admin_id`)
) ENGINE=MyISAM AUTO_INCREMENT=50 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adminlog`
--

LOCK TABLES `adminlog` WRITE;
/*!40000 ALTER TABLE `adminlog` DISABLE KEYS */;
INSERT INTO `adminlog` VALUES (1,1,'127.0.0.1','2020-01-24 09:26:24'),(3,1,'127.0.0.1','2020-03-24 09:29:42'),(4,1,'127.0.0.1','2021-02-03 14:00:58'),(5,1,'127.0.0.1','2023-03-22 20:15:24'),(6,1,'127.0.0.1','2023-03-22 20:23:45'),(7,1,'127.0.0.1','2023-03-22 20:37:28'),(8,1,'127.0.0.1','2023-03-24 20:33:00'),(9,1,'127.0.0.1','2023-03-24 20:46:31'),(10,1,'127.0.0.1','2023-03-24 21:02:49'),(11,1,'127.0.0.1','2023-03-24 21:15:35'),(12,1,'127.0.0.1','2023-03-24 22:02:57'),(13,1,'127.0.0.1','2023-03-24 22:03:50'),(14,1,'127.0.0.1','2023-03-27 17:47:47'),(15,1,'127.0.0.1','2023-03-27 18:13:21'),(16,1,'127.0.0.1','2023-03-27 18:30:46'),(17,1,'127.0.0.1','2023-03-27 18:33:37'),(18,1,'127.0.0.1','2023-03-27 18:58:17'),(19,1,'127.0.0.1','2023-03-27 18:59:33'),(20,1,'127.0.0.1','2023-03-27 19:03:28'),(21,1,'127.0.0.1','2023-03-27 19:04:43'),(22,1,'127.0.0.1','2023-03-27 19:06:15'),(23,1,'127.0.0.1','2023-03-27 19:38:08'),(24,1,'127.0.0.1','2023-03-29 21:48:07'),(25,1,'127.0.0.1','2023-03-29 22:09:12'),(26,1,'127.0.0.1','2023-03-29 22:23:18'),(27,1,'127.0.0.1','2023-03-29 23:40:21'),(28,1,'127.0.0.1','2023-03-29 23:49:08'),(29,1,'127.0.0.1','2023-03-30 01:03:46'),(30,1,'127.0.0.1','2023-03-30 17:09:13'),(31,1,'127.0.0.1','2023-03-31 10:18:56'),(32,1,'127.0.0.1','2023-03-31 12:12:28'),(33,1,'127.0.0.1','2023-03-31 12:31:27'),(34,1,'127.0.0.1','2023-03-31 19:18:10'),(35,1,'127.0.0.1','2023-03-31 19:53:33'),(36,1,'127.0.0.1','2023-03-31 22:38:27'),(37,1,'127.0.0.1','2023-04-01 01:52:04'),(38,1,'127.0.0.1','2023-04-01 12:50:41'),(39,1,'127.0.0.1','2023-04-01 13:22:27'),(40,1,'127.0.0.1','2023-04-01 13:47:03'),(41,1,'127.0.0.1','2023-04-01 16:20:27'),(42,1,'127.0.0.1','2023-04-01 16:41:15'),(43,1,'127.0.0.1','2023-04-01 16:53:54'),(44,1,'127.0.0.1','2023-04-01 20:33:04'),(45,1,'127.0.0.1','2023-04-01 21:04:17'),(46,1,'127.0.0.1','2023-04-02 21:00:31'),(47,1,'127.0.0.1','2023-04-02 21:47:02'),(48,1,'127.0.0.1','2023-04-03 07:18:05'),(49,1,'127.0.0.1','2023-04-04 01:34:53');
/*!40000 ALTER TABLE `adminlog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('2a49ef890f33');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `area`
--

DROP TABLE IF EXISTS `area`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `area` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(70) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  `is_recommended` tinyint(1) DEFAULT NULL,
  `introduction` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `ix_area_addtime` (`addtime`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `area`
--

LOCK TABLES `area` WRITE;
/*!40000 ALTER TABLE `area` DISABLE KEYS */;
INSERT INTO `area` VALUES (1,'北京','2021-03-22 10:45:33',1,'今日的北京，已发展成为一座现代化的大都市：北京大学、清华大学、中国科学院等教育和科研机构座落于北京市区；金融街是中国金融监管机构办公地点和金融业聚集地；北京商务中心区是北京经济的象征；798艺术区是世界知名的当代艺术中心；此外，中国国家大剧院、北京首都国际机场3号航站楼、中央电视台总部大楼、“鸟巢”、“水立方”、中国尊等具有现代风格的建筑成为古老北京新的名片。每年有超过1亿4700万人到北京旅游。'),(2,'长春','2021-03-22 11:40:13',0,'长春，被誉为“北国春城”，绿化率居于亚洲大城市前列，中国四大园林城市之一；连续十次蝉联“中国最具幸福感城市”；“中国制造2025”试点城市；“首批全国城市设计试点城市”；位列《2015中国自然指数》中国十大科研城市第六位。'),(9,'南昌','2023-04-04 17:06:39',1,'发达发');
/*!40000 ALTER TABLE `area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `collect`
--

DROP TABLE IF EXISTS `collect`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `collect` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `scenic_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_collect_addtime` (`addtime`),
  KEY `scenic_id` (`scenic_id`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=85 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `collect`
--

LOCK TABLES `collect` WRITE;
/*!40000 ALTER TABLE `collect` DISABLE KEYS */;
INSERT INTO `collect` VALUES (17,5,10,'2023-03-16 22:13:57'),(15,3,10,'2023-03-16 22:04:32'),(14,1,10,'2023-03-16 22:04:24'),(18,4,10,'2023-03-16 22:20:39'),(82,28,9,'2023-04-03 22:30:20'),(80,1,9,'2023-04-03 20:33:29'),(83,36,9,'2023-04-03 22:30:29'),(81,3,9,'2023-04-03 20:33:33'),(84,4,9,'2023-04-03 22:31:01');
/*!40000 ALTER TABLE `collect` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `email_captcha_model`
--

DROP TABLE IF EXISTS `email_captcha_model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `email_captcha_model` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `captcha` varchar(10) NOT NULL,
  `tag` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `email_captcha_model`
--

LOCK TABLES `email_captcha_model` WRITE;
/*!40000 ALTER TABLE `email_captcha_model` DISABLE KEYS */;
/*!40000 ALTER TABLE `email_captcha_model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oplog`
--

DROP TABLE IF EXISTS `oplog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oplog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `admin_id` int(11) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `reason` varchar(600) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_oplog_addtime` (`addtime`),
  KEY `admin_id` (`admin_id`)
) ENGINE=MyISAM AUTO_INCREMENT=92 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oplog`
--

LOCK TABLES `oplog` WRITE;
/*!40000 ALTER TABLE `oplog` DISABLE KEYS */;
INSERT INTO `oplog` VALUES (1,1,'127.0.0.1','添加景区八达岭长城','2021-03-24 11:19:05'),(2,1,'127.0.0.1','添加地区天津','2021-03-24 11:23:57'),(3,1,'127.0.0.1','添加景区颐和园','2021-03-24 13:01:27'),(4,1,'127.0.0.1','添加景区净月潭国家森林公园','2021-03-24 13:05:54'),(5,1,'127.0.0.1','添加景区伪满皇宫博物院','2021-03-24 13:10:08'),(6,1,'127.0.0.1','添加游记最轻松愉快的方式游览故宫','2021-03-24 13:24:56'),(19,1,'127.0.0.1','添加景区上高花园','2023-03-31 23:39:39'),(20,1,'127.0.0.1','添加景区上高花园1','2023-04-01 00:16:40'),(21,1,'127.0.0.1','添加景区上高花园3','2023-04-01 00:27:40'),(22,1,'127.0.0.1','添加景区上高花园111111','2023-04-01 00:56:52'),(23,1,'127.0.0.1','添加景区上高花园11','2023-04-01 01:11:18'),(24,1,'127.0.0.1','添加景区上高花园112','2023-04-01 01:26:57'),(25,1,'127.0.0.1','添加景区故宫博物院111','2023-04-01 01:45:58'),(26,1,'127.0.0.1','添加景区上高花园','2023-04-01 16:51:36'),(27,1,'127.0.0.1','添加景区上高花园dafd','2023-04-02 00:08:02'),(28,1,'127.0.0.1','删除景区八达岭长城','2023-04-02 00:28:23'),(29,1,'127.0.0.1','删除景区上高花园dafd','2023-04-02 00:28:35'),(30,1,'127.0.0.1','删除景区上高花园','2023-04-02 00:28:39'),(31,1,'127.0.0.1','删除景区故宫博物院111','2023-04-02 00:28:41'),(32,1,'127.0.0.1','删除景区上高花园112','2023-04-02 00:28:44'),(33,1,'127.0.0.1','删除景区上高花园11','2023-04-02 00:28:46'),(34,1,'127.0.0.1','添加景区上高花园','2023-04-02 00:49:30'),(35,1,'127.0.0.1','删除景区上高花园','2023-04-02 00:49:44'),(36,1,'127.0.0.1','添加景区上高花园','2023-04-02 00:50:38'),(37,1,'127.0.0.1','添加景区上高花园dd ','2023-04-03 01:08:43'),(38,1,'127.0.0.1','添加地区宜春','2023-04-03 07:34:09'),(39,1,'127.0.0.1','添加地区南昌','2023-04-03 08:50:09'),(40,1,'127.0.0.1','修改地区哈哈哈','2023-04-03 08:58:12'),(41,1,'127.0.0.1','修改地区哈哈','2023-04-03 09:04:58'),(42,1,'127.0.0.1','删除地区哈哈','2023-04-03 09:14:33'),(43,1,'127.0.0.1','添加景区滕王阁','2023-04-03 09:19:35'),(44,1,'127.0.0.1','修改地区南昌','2023-04-03 09:21:00'),(45,1,'127.0.0.1','删除地区南昌','2023-04-03 09:21:10'),(46,1,'127.0.0.1','删除景区上高花园','2023-04-03 10:17:41'),(47,1,'127.0.0.1','修改景区滕王阁','2023-04-03 17:09:08'),(48,1,'127.0.0.1','修改景区滕王阁','2023-04-03 17:16:46'),(49,1,'127.0.0.1','修改景区滕王阁','2023-04-03 17:18:33'),(50,1,'127.0.0.1','修改景区滕王阁','2023-04-03 17:22:34'),(51,1,'127.0.0.1','添加景区上高花园','2023-04-03 17:34:47'),(52,1,'127.0.0.1','添加景区上高花园','2023-04-03 17:38:28'),(53,1,'127.0.0.1','添加景区上高花园111','2023-04-03 17:41:23'),(54,1,'127.0.0.1','添加景区上高花园','2023-04-03 17:43:23'),(55,1,'127.0.0.1','添加景区上高花园啊打发','2023-04-03 17:46:26'),(56,1,'127.0.0.1','添加景区上高花园得分','2023-04-03 17:48:37'),(57,1,'127.0.0.1','修改景区上高花园得分','2023-04-03 18:17:04'),(58,1,'127.0.0.1','修改景区上高花园得分','2023-04-03 18:18:15'),(59,1,'127.0.0.1','修改景区上高花园得分','2023-04-03 18:26:43'),(60,1,'127.0.0.1','修改景区上高花园得分','2023-04-03 18:36:04'),(61,1,'127.0.0.1','添加景区上高花园','2023-04-03 18:36:35'),(62,1,'127.0.0.1','删除游记最轻松愉快的方式游览故宫','2023-04-03 19:45:42'),(63,1,'127.0.0.1','添加游记上高花园一游','2023-04-03 19:57:19'),(64,1,'127.0.0.1','添加游记明月山一游','2023-04-03 20:35:52'),(65,1,'127.0.0.1','删除游记明月山一游','2023-04-03 20:36:20'),(66,1,'127.0.0.1','修改景区上高花园','2023-04-03 21:03:47'),(67,1,'127.0.0.1','修改景区上高花园','2023-04-03 21:04:37'),(68,1,'127.0.0.1','修改景区上高花园','2023-04-03 21:05:06'),(69,1,'127.0.0.1','删除地区宜春','2023-04-03 21:05:23'),(70,1,'127.0.0.1','删除地区天津','2023-04-03 21:11:17'),(71,1,'127.0.0.1','添加地区宜春','2023-04-03 21:13:33'),(72,1,'127.0.0.1','修改景区长乐山庄','2023-04-03 21:14:03'),(73,1,'127.0.0.1','修改景区上高花园','2023-04-03 21:14:41'),(74,1,'127.0.0.1','删除地区宜春','2023-04-03 21:15:05'),(75,1,'127.0.0.1','删除景区上高花园','2023-04-03 21:32:57'),(76,1,'127.0.0.1','添加游记上高花园一日游','2023-04-03 21:41:47'),(77,1,'127.0.0.1','添加游记上高花园三日游','2023-04-03 21:42:42'),(78,1,'127.0.0.1','删除意见建议','2023-04-04 16:39:31'),(79,1,'127.0.0.1','删除意见建议','2023-04-04 16:39:33'),(80,1,'127.0.0.1','删除意见建议','2023-04-04 16:39:39'),(81,1,'127.0.0.1','删除意见建议','2023-04-04 16:39:41'),(82,1,'127.0.0.1','删除意见建议','2023-04-04 16:39:42'),(83,1,'127.0.0.1','删除意见建议','2023-04-04 16:39:43'),(84,1,'127.0.0.1','添加地区南昌','2023-04-04 17:00:49'),(85,1,'127.0.0.1','添加景区滕王阁','2023-04-04 17:02:49'),(86,1,'127.0.0.1','添加游记滕王阁一游','2023-04-04 17:03:31'),(87,1,'127.0.0.1','删除地区南昌','2023-04-04 17:05:00'),(88,1,'127.0.0.1','添加地区南昌','2023-04-04 17:06:39'),(89,1,'127.0.0.1','修改景区滕王阁','2023-04-04 17:06:57'),(90,1,'127.0.0.1','修改景区长乐山庄','2023-04-04 17:07:23'),(91,1,'127.0.0.1','修改景区上高花园得分','2023-04-04 17:07:45');
/*!40000 ALTER TABLE `oplog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scenic`
--

DROP TABLE IF EXISTS `scenic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scenic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) DEFAULT NULL,
  `star` int(11) DEFAULT NULL,
  `logo` varchar(200) DEFAULT NULL,
  `introduction` text,
  `content` text,
  `address` text,
  `is_hot` tinyint(1) DEFAULT NULL,
  `is_recommended` tinyint(1) DEFAULT NULL,
  `area_id` int(11) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `logo` (`logo`),
  KEY `ix_scenic_addtime` (`addtime`),
  KEY `area_id` (`area_id`)
) ENGINE=MyISAM AUTO_INCREMENT=39 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scenic`
--

LOCK TABLES `scenic` WRITE;
/*!40000 ALTER TABLE `scenic` DISABLE KEYS */;
INSERT INTO `scenic` VALUES (1,'故宫博物院',4,'20180324132557f9503c2174574a5a84c4bb57ff60ee17.jpg','故宫又名紫禁城，是中国乃至世界上保存最完整，规模最大的木质结构古建筑群，被誉为“世界五大宫之首”。\r\n故宫由永乐帝朱棣下令建造，依据其布局与功用分为“外朝”与“内廷”两大部分。以乾清门为界，乾清门以南为外朝，以北为内廷。\r\n外朝也称为“前朝”，以太和殿(金銮殿)、中和殿、保和殿三大殿为中心，是封建皇帝行使权力、举行盛典的地方。\r\n内廷以乾清宫、交泰殿、坤宁宫后三宫为中心，以及东西两侧的东六宫和西六宫，是封建帝王与后妃居住之所，也就是俗称的“三宫六院”。\r\n故宫内珍藏有大量珍贵文物，据统计有上百万件，占全国文物总数的六分之一。钟表馆每天11点和14点有钟表演示，不可错过。','<p>北京故宫是中国明清两代的皇家宫殿，旧称为紫禁城，位于北京中轴线的中心，是中国古代宫廷建筑之精华。北京故宫以三大殿为中心，占地面积72万平方米，建筑面积约15万平方米，有大小宫殿七十多座，房屋九千余间。是世界上现存规模最大、保存最为完整的木质结构古建筑之一。<br />\r\n北京故宫于明成祖永乐四年（1406年）开始建设，以南京故宫为蓝本营建，到永乐十八年（1420年）建成。它是一座长方形城池，南北长961米，东西宽753米，四面围有高10米的城墙，城外有宽52米的护城河。紫禁城内的建筑分为外朝和内廷两部分。外朝的中心为太和殿、中和殿、保和殿，统称三大殿，是国家举行大典礼的地方。内廷的中心是乾清宫、交泰殿、坤宁宫，统称后三宫，是皇帝和皇后居住的正宫。<br />\r\n北京故宫被誉为世界五大宫之首（北京故宫、法国凡尔赛宫、英国白金汉宫、美国白宫、俄罗斯克里姆林宫），是国家AAAAA级旅游景区， 1961年被列为第一批全国重点文物保护单位，1987年被列为世界文化遗产。</p>\r\n\r\n<p><img alt=\"\" src=\"/static/uploads/ckeditor/201803240935436d8289e1792e4a7ca38dbb90855404dd.jpg\" style=\"height:454px; width:1258px\" /></p>\r\n\r\n<blockquote>\r\n<h2><strong>旅游须知：</strong></h2>\r\n\r\n<p><big>电话：010-85007421</big></p>\r\n\r\n<p><big>网址：<a href=\"http://www.dpm.org.cn/\" target=\"_blank\">http://www.dpm.org.cn</a></big></p>\r\n\r\n<p><big>开放时间：除法定节假日和暑期（每年7月1日至8月31日）外，故宫博物院全年实行周一全天闭馆的措施。</big></p>\r\n\r\n<p><big>门票：（1）每年4月1日至10月31日为旺季，大门票60元/人；<br />\r\n（2）每年11月1日至次年3月31日为淡季，大门票40元/人。</big></p>\r\n</blockquote>\r\n','北京市东城区景山前街4号',1,1,1,'2021-03-22 12:48:16'),(3,'颐和园',4,'20180324130127eb365ba129fb4636a8f033e111c8efa2.jpg','颐和园坐落于北京西郊，是中国古典园林之首，总面积约290公顷，由万寿山和昆明湖组成。全园分3个区域：以仁寿殿为中心的政治活动区；以玉澜堂、乐寿堂为主体的帝后生活区；以万寿山和昆明湖组成的风景旅游区。全园以西山群峰为背景，加之建筑群与园内山湖形势融为一体，使景色变幻无穷。1998年12月2日列入《世界遗产名录》。','<p>颐和园以万寿山和昆明湖为主，昆明湖占颐和园总面积的四分之三。除了湖山，还有殿堂景区、耕织图景区。重要建筑集中在万寿山南北中轴线上。万寿山分为前山、后山两部分，前山自东向西有养云轩、无尽意轩、介寿堂、排云殿、清华轩、宝云阁、共一楼、听鹂馆、画中游等知名景观。后山南北中轴线为规模宏大的汉藏风格寺庙殿宇，包括四大部洲、须弥灵境、香岩宗印之阁等等，周围点缀以数座小型山间园林，有苏州街、寅辉城关、花承阁、赅春园、绘芳堂等建筑。昆明湖中有三座岛屿，分别名为南湖岛、藻鉴堂岛、治镜阁岛。昆明湖由一条西堤将大湖一分为二，光绪时建立围墙，修筑起了东堤。<br />\r\n颐和园的主要区域可包括六个部分，分别是殿堂景区（是帝后料理朝政和住宿所在）、万寿山景区、昆明湖景区、耕织图景区（独特的农牧色彩）、长廊景区和中轴景区（起于前山云辉玉宇牌楼，止于后山慈福慧因牌楼）。作为一座知名园林博物馆，拥有丰富制式的园林建筑和景观营造手法，涵盖了中国传统名著中的亭台楼阁，轩榭台堂。</p>\r\n\r\n<p><img alt=\"\" src=\"/static/uploads/ckeditor/20180324130057a797628bce3446ebae3b149d8c6e5358.jpeg\" style=\"height:370px; width:690px\" /></p>\r\n','北京市海淀区新建宫门路19号',1,1,1,'2021-03-24 13:01:27'),(4,'净月潭国家森林公园',5,'20180324130554b0efff8d6f114c34802ee773dbe996e2.jpeg','净月潭因其弯月状而得名，被誉为台湾日月潭的姊妹潭。公园内树木茂盛、空气清新，处处皆景致，四季貌不同。\r\n地貌呈低山丘陵状，有大小山峰119座，其中海拔高于200米的就有近120座，而独以潭北的山色为最。这里有86座山岭自北向南延伸至潭边，不仅沟壑纵横，层峦叠嶂，而且可以登山鸟瞰潭水全景。\r\n整座山仿佛巨蟒蜿蜒，其中犹以大架山海拔最高，是绝佳的度假胜地。此外，园内植物格局模拟长白山植物垂地分布特征，有山花、药用植物等千余种。','<p>净月潭景区位于吉林省长春市东南部长春净月经济开发区，距市中心人民广场仅18公里，景区面积为96.38平方公里，其中水域面积为5.3平方公里，森林覆盖率达到96%以上。净月潭因形似弯月状而得名，与台湾日月潭互为姊妹潭。<br />\r\n净月潭是在1934年由人工修建的第一座为长春市城区供水的水源地，在沦陷时期称&rdquo;水源地&ldquo;或&rdquo;贮水池&ldquo;。净月潭的名字是由&rdquo;满洲国总理大臣&ldquo;郑孝胥的二儿子，时任&rdquo;满洲国国都建设局局长&ldquo;的郑禹所起。景区内的森林为人工建造，含有30个树种的完整森林生态体系，得天独厚的区位优势，使之成为&ldquo;喧嚣都市中的一块净土&rdquo;，有&ldquo;亚洲第一大人工林海&rdquo;、&ldquo;绿海明珠&rdquo;、&ldquo;都市氧吧&rdquo;之美誉，是长春市的生态绿核和城市名片。<br />\r\n净月潭景区处处皆景致，四季貌不同。亚洲最大的人工森林与山、水相依的生态景象构成了净月潭四季变幻的风情画卷。净月潭已然成为春踏青、夏避暑、秋赏景、冬玩冰雪的理想去处。<br />\r\n净月潭不仅是生态休闲中心，更是体育健身的中心，作为长春市消夏节和长春冰雪节的主场地，相继开展了净月潭瓦萨国际滑雪节、净月潭森林马拉松、净月潭森林定向赛、净月潭自行车马拉松、青少年阳光体育大会、龙舟赛、旅游大集等赛事和活动，致力于倡导健康、时尚、休闲的生活方式，打造国际知名旅游文化活动的聚集地。</p>\r\n\r\n<p><img alt=\"\" src=\"/static/uploads/ckeditor/2018032413055096c1be099bdf427d8cdd3e985d76cae0.jpg\" style=\"height:125px; width:402px\" /></p>\r\n','吉林省长春市净月开发区',1,1,2,'2021-03-24 13:05:54'),(5,'伪满皇宫博物院',5,'20180324131008f4e5802528d847279cdfb84d8974cdc1.jpeg','伪满皇宫博物院的主要建筑有勤民楼、缉熙楼、怀远楼、嘉乐殿、同德殿、书画库、莱薰门、保康门、兴运门、建国神庙遗迹和御用防空洞等，对游客开放的还有跑马场和东北沦陷史陈列馆。','<p>1931年九一八事变后，日本扶植清朝末代皇帝爱新觉罗&middot;溥仪建立满洲国，以此控制中国东北。当时的中华民国及1949年成立的中华人民共和国均不承认满洲国，所以称其为&ldquo;伪满洲国&rdquo;或&ldquo;伪满&rdquo;。1932年3月9日溥仪就任满洲国执政，4月3日执政府迁入原吉黑榷运局官署（民国时期管理吉林、黑龙江两省盐务）旧址。1934年3月1日溥仪称帝，执政府机关改为宫内府。因日本天皇的宫廷叫皇宫，溥仪的这个宫廷就只能对外称为&ldquo;帝宫&rdquo;。至1945年8月日本投降前，满洲国帝宫一直作为溥仪办公和生活的地方，其宫廷区域分为用于政务办公的外廷和帝室生活的内廷两个部分，建筑风格东西合璧。1945年满洲国解体以后，帝宫建筑毁损严重。<br />\r\n1962年在满洲国帝宫旧址上成立伪皇宫陈列馆，1964年与吉林省博物馆合署办公，1982年恢复建制，1984年正式对外开放。2000年7月1日划归长春市管理，2001年2月8日改名为伪满皇宫博物院；现已全面整修，基本恢复旧貌。2013年，中华人民共和国国务院将之以伪满皇宫及日伪军政机构旧址之名列入第七批全国重点文物保护单位（近现代重要史迹及代表性建筑）。<br />\r\n2017年，伪满皇宫博物院被中国博物馆协会评为第三批国家一级博物馆。</p>\r\n\r\n<p><img alt=\"\" src=\"/static/uploads/ckeditor/201803241309567f4e4bffb6f04a8498ff137b9a3558d6.jpg\" style=\"height:498px; width:750px\" /></p>\r\n','吉林省长春市宽城区光复北路5号',1,1,2,'2021-03-24 13:10:08'),(28,'长乐山庄',3,'20230402225442_85.png','景区测试用的','<p>山区消费好吗？</p>\r\n\r\n<p><img alt=\"\" src=\"/static/uploads/ckeditor/202304022255080b8d6c920ed54d79b414c6a94d84a84d.png\" style=\"height:281px; width:365px\" /></p>\r\n','长春市东城区景山前街1号',1,1,2,'2023-04-02 00:50:38'),(36,'上高花园得分',3,'202304031748375e8194967f874924a6e26ab520db7de3.png','d发额','<p>dfadf发的</p>\r\n','灌灌灌灌',0,0,NULL,'2023-04-03 17:48:37'),(38,'滕王阁',4,'2023040417024967c339c103944011b19c8894f50e410c.png','四大古楼之一，值得一游。','<p>景区优美。<img alt=\"\" src=\"/static/uploads/ckeditor/2023040417024356a7ba31fe1c488ca0614a0a812ad985.png\" style=\"height:33px; width:52px\" /></p>\r\n','南昌市2号线xx站23号',1,1,9,'2023-04-04 17:02:49');
/*!40000 ALTER TABLE `scenic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suggestion`
--

DROP TABLE IF EXISTS `suggestion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `suggestion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `content` text,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_suggestion_addtime` (`addtime`)
) ENGINE=MyISAM AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suggestion`
--

LOCK TABLES `suggestion` WRITE;
/*!40000 ALTER TABLE `suggestion` DISABLE KEYS */;
INSERT INTO `suggestion` VALUES (1,'andy','andy@qq.com','haha','2021-03-22 14:56:05'),(2,'andy','andy@qq.com','haha','2021-03-22 14:58:57'),(3,'andy','andy@qq.com','haha','2021-03-22 14:59:55'),(4,'andy','andy@qq.com','haha','2021-03-22 14:59:59'),(5,'andy','andy@qq.com','haha','2021-03-22 15:00:03'),(6,'andy','andy@qq.com','haha','2021-03-22 15:00:43'),(26,'范达尔','2276234553@qq.com','f打发打发','2023-04-04 16:52:13'),(27,'发得分','12345678@qq.com','d发的','2023-04-04 16:54:08'),(28,'mr','12345678@qq.com','d发达发','2023-04-04 16:59:23'),(29,'mr','2276234553@qq.com','发达发达发','2023-04-04 17:04:11');
/*!40000 ALTER TABLE `suggestion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `travels`
--

DROP TABLE IF EXISTS `travels`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `travels` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) DEFAULT NULL,
  `author` varchar(70) DEFAULT NULL,
  `content` text,
  `scenic_id` int(11) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  KEY `ix_travels_addtime` (`addtime`),
  KEY `scenic_id` (`scenic_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `travels`
--

LOCK TABLES `travels` WRITE;
/*!40000 ALTER TABLE `travels` DISABLE KEYS */;
INSERT INTO `travels` VALUES (1,'北京不得不去的地方——故宫一日游','老冯','<p>【关于门票】<br />\r\n故宫门票价格：成人旺季60元，淡季40元，学生票全年20元。珍宝馆和钟表馆另外收费10元/人，学生证半价。<br />\r\n我们去的时候故宫还可以现场售票，回来以后就实行全网络售票参观了。<br />\r\n门票提前10天在网上预售，售完为止，一张身份证每个入院日限购一张门票。和其它博物馆一样，故宫博物院也是周一闭馆。<br />\r\n去之前建议关注一下故宫博物院的官网：http://gugong.228.com.cn/，尤其是跟我们一样自由行的游客，除了可以看到余票和购买门票，还能看到最新的一些消息公告，比如哪里闭馆哪里修缮（虽然有些宫殿临时维修不在官网通告，但有总好过无嘛），对规划路线有很大的帮助。<br />\r\n我们是在美团上提前买的大门票和珍宝馆的门票，刷身份证就可以入园。<br />\r\n【没什么用的讲解器】<br />\r\n过了安检就能看到讲解器服务处。<br />\r\n自助讲解器租赁价格：汉语、粤语、闽南语版20.00元/台，其他语种40.00元/台，免押金，参观完毕在出院前将讲解器归还即可。<br />\r\n我和泡泡一人租了一台，使用下来的感受是缺点多过优点，可以不租。<br />\r\n虽说它是自动感应的，走到哪里讲到哪里，讲解的内容也挺不错，有多个版本，我们听的是王刚老师讲的故事版，生动有趣。但是它的缺点也很明显。<br />\r\n1、因为是单耳佩戴，所以在环境嘈杂的地方，即使声音开的很大，也经常听不清楚说了什么。<br />\r\n2、走到一些建筑密集的地方，讲解器会错乱崩溃。比如我们在珍妃井附近转了很久，它始终就识别不到我们所在的位置。比如我们到了宁寿宫，它却讲的是皇极殿的内容。泡泡一度以为是不是讲解器坏了，还跑到服务处换了一个，工作人员倒是很耿直，说这个就是这样的，不是很灵，到了不放他们也没办法。因为是自动定位讲解，又不能选择自己想听的地方，所以就导致我们很多地方到最后也没能听到讲解。<br />\r\n3、所有内容只讲一次，如果你没听得清，或者中途不小心耳机掉下来，漏听了，也只能自认倒霉。<br />\r\n其实故宫只要不闭馆，根本不可能有人少的时候，一个又一个旅行团，你想不听导游的讲解都很难。当然，这只是我们的看法，讲解器本身不贵，想要的话也可以租一个备用，权当地图用也行。<br />\r\n我和泡泡在故宫走了一整天。从早上的人头攒动待到晚上的人去楼空。<br />\r\n很多人说故宫没意思，就是看看长的差不多的房子。我倒觉得这一趟来的超值。<br />\r\n我建议对历史，尤其是明清史感兴趣的亲们，可以多预留一些时间给这座紫禁城，它会还你无限惊喜。</p>\r\n\r\n<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<img alt=\"\" class=\"left\" src=\"/static/uploads/ckeditor/2018032411373051faede1c35748c7b2347dc0c6397e29.png\" style=\"height:296px; width:660px\" /></p>\r\n',1,'2018-03-22 13:49:32'),(3,'上高花园一游','老李','<p>开源快乐！<img alt=\"\" src=\"/static/uploads/ckeditor/2023040319565795dd98bdb75c40d49e86cebdb40a42b7.png\" style=\"height:149px; width:150px\" /></p>\r\n',NULL,'2023-04-03 19:57:19'),(5,'上高花园一日游','老李头','<p>快乐dota</p>\r\n\r\n<p>&nbsp;</p>\r\n',36,'2023-04-03 21:41:47'),(6,'上高花园三日游','老白','<p>没景区了都。</p>\r\n',NULL,'2023-04-03 21:42:42'),(7,'滕王阁一游','老李头','<p>真是有意思的一次游玩</p>\r\n',38,'2023-04-04 17:03:31');
/*!40000 ALTER TABLE `travels` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pwd` varchar(300) NOT NULL,
  `email` varchar(50) NOT NULL,
  `addtime` datetime DEFAULT NULL,
  `username` varchar(70) NOT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `info` text,
  `face` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `face` (`face`),
  UNIQUE KEY `phone` (`phone`),
  KEY `ix_user_addtime` (`addtime`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (9,'pbkdf2:sha256:260000$mLYBMKANi3Abjwn7$ba247e0b792a2cb696fba1d6b427a97ae0a96d20c11f945834631bfd54472b3c','2276234553@qq.com','2023-03-10 18:06:37','user',NULL,NULL,NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userlog`
--

DROP TABLE IF EXISTS `userlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userlog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_userlog_addtime` (`addtime`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=40 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userlog`
--

LOCK TABLES `userlog` WRITE;
/*!40000 ALTER TABLE `userlog` DISABLE KEYS */;
INSERT INTO `userlog` VALUES (1,1,'127.0.0.1','2021-01-23 10:06:15'),(2,4,'127.0.0.1','2021-01-23 14:28:54'),(3,5,'127.0.0.1','2021-02-03 13:12:06'),(4,6,'127.0.0.1','2023-03-08 17:39:58'),(5,6,'127.0.0.1','2023-03-08 17:45:49'),(6,6,'127.0.0.1','2023-03-08 17:49:37'),(7,6,'127.0.0.1','2023-03-08 17:49:42'),(8,6,'127.0.0.1','2023-03-08 17:51:12'),(9,6,'127.0.0.1','2023-03-08 17:52:07'),(10,6,'127.0.0.1','2023-03-08 18:16:08'),(11,6,'127.0.0.1','2023-03-08 18:16:22'),(12,6,'127.0.0.1','2023-03-08 18:16:28'),(13,6,'127.0.0.1','2023-03-08 18:17:48'),(14,6,'127.0.0.1','2023-03-09 10:39:13'),(15,9,'127.0.0.1','2023-03-10 18:07:07'),(16,9,'127.0.0.1','2023-03-14 20:53:35'),(17,9,'192.168.43.1','2023-03-15 00:14:03'),(18,9,'192.168.43.1','2023-03-15 00:21:20'),(19,9,'192.168.43.1','2023-03-15 00:21:20'),(20,9,'192.168.43.1','2023-03-15 00:21:20'),(21,9,'127.0.0.1','2023-03-16 15:34:25'),(22,9,'127.0.0.1','2023-03-16 19:03:58'),(23,9,'127.0.0.1','2023-03-16 20:49:04'),(24,9,'127.0.0.1','2023-03-16 21:49:01'),(25,9,'192.168.43.150','2023-03-16 22:03:09'),(26,10,'192.168.43.150','2023-03-16 22:04:16'),(27,10,'192.168.43.1','2023-03-16 22:13:11'),(28,10,'192.168.43.150','2023-03-16 22:13:22'),(29,9,'127.0.0.1','2023-03-17 11:04:17'),(30,9,'127.0.0.1','2023-03-17 12:41:19'),(31,9,'127.0.0.1','2023-03-17 13:26:28'),(32,9,'127.0.0.1','2023-03-17 15:23:53'),(33,9,'192.168.43.1','2023-03-17 15:28:49'),(34,9,'127.0.0.1','2023-03-18 17:34:40'),(35,9,'127.0.0.1','2023-03-29 18:15:07'),(36,9,'127.0.0.1','2023-03-29 18:15:31'),(37,9,'127.0.0.1','2023-04-01 20:42:30'),(38,9,'127.0.0.1','2023-04-02 23:00:24'),(39,9,'127.0.0.1','2023-04-03 10:18:03');
/*!40000 ALTER TABLE `userlog` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-04 17:43:27
