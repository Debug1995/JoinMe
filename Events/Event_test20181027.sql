-- MySQL dump 10.13  Distrib 8.0.13, for macos10.14 (x86_64)
--
-- Host: localhost    Database: JoinMe
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Event`
--

DROP TABLE IF EXISTS `Event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Event` (
  `EventID` int(11) NOT NULL AUTO_INCREMENT,
  `Title` varchar(50) DEFAULT NULL,
  `Tags` varchar(50) DEFAULT NULL,
  `EventDate` date DEFAULT NULL,
  `Description` varchar(300) DEFAULT NULL,
  `Image` varchar(100) DEFAULT NULL,
  `Location` varchar(50) DEFAULT NULL,
  `ExpireTime` date DEFAULT NULL,
  PRIMARY KEY (`EventID`),
  UNIQUE KEY `EventID_UNIQUE` (`EventID`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Event`
--

LOCK TABLES `Event` WRITE;
/*!40000 ALTER TABLE `Event` DISABLE KEYS */;
INSERT INTO `Event` VALUES (5,'a','b','2017-08-12','c','d','e','2019-08-08'),(9,'this is title','tag1 tag2 tag3','2018-10-27','this is description','this is image url','this is location','2018-10-28'),(10,'this is title','tag1 tag2 tag3','2018-10-27','this is description','this is image url','this is location','2018-10-28'),(11,'this is title','tag1 tag2 tag3','2018-10-27','this is description','this is image url','this is location','2018-10-28'),(13,'this is title','tag13 tag2 tag3','2018-10-27','this is description','this is image url','this is location','2018-10-28'),(14,'this is title','tag1 tag2 tag3','2018-10-27','this is description','this is image url','this is location','2018-10-28'),(15,'this is title','tag1 tag2 tag3','2018-10-27','this is description','this is image url','this is location','2018-10-28'),(16,'this is title','tag1 tag2 tag3','2018-10-27','this is description','this is image url','this is location','2018-10-28'),(17,'this is title','tag1 tag2 tag3','2018-10-27','this is description','this is image url','this is location','2018-10-28'),(27,'this is title','tag1 tag2 tag3','2018-10-27','this is description','this is image url','this is location','2018-10-28'),(28,'this is title','tag1 tag2 tag3','2018-10-27','this is description','this is image url','this is location','2018-10-28'),(29,'this is title','tag1 tag2 tag3','2018-10-27','this is description','this is image url','this is location','2018-10-28'),(30,'this is title','tag1 tag2 tag3','2018-10-27','this is description','this is image url','this is location','2018-10-28'),(31,'this is title','tag1 tag2 tag3','2018-10-27','this is description','this is image url','this is location','2018-10-28'),(32,'this is title','tag1 tag2 tag3','2018-10-27','this is description','this is image url','this is location','2018-10-28'),(35,'this is title','tag13 tag2 tag3','2018-03-27','this is description','this is image url','this is location','2018-04-03'),(36,'this is title','tag13 tag2 tag3','2222-08-27','this is description','this is image url','this is location','2222-09-03'),(37,'this is title','tag13 tag2 tag3','2018-03-27','this is description','this is image url','this is location','2018-04-03'),(38,'this is title','tag13 tag2 tag3','2018-08-27','this is description','this is image url','this is location','2018-09-03');
/*!40000 ALTER TABLE `Event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Host`
--

DROP TABLE IF EXISTS `Host`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Host` (
  `HostID` int(11) NOT NULL,
  `EventID` int(11) NOT NULL,
  PRIMARY KEY (`HostID`,`EventID`),
  KEY `EventID_idx` (`EventID`),
  CONSTRAINT `EventID` FOREIGN KEY (`EventID`) REFERENCES `event` (`eventid`),
  CONSTRAINT `HostID` FOREIGN KEY (`HostID`) REFERENCES `user` (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Host`
--

LOCK TABLES `Host` WRITE;
/*!40000 ALTER TABLE `Host` DISABLE KEYS */;
/*!40000 ALTER TABLE `Host` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `JoinTable`
--

DROP TABLE IF EXISTS `JoinTable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `JoinTable` (
  `JoinID` int(11) NOT NULL,
  `EventID` int(11) NOT NULL,
  PRIMARY KEY (`JoinID`,`EventID`),
  KEY `EventID_idx` (`EventID`),
  CONSTRAINT `JoinEventID` FOREIGN KEY (`EventID`) REFERENCES `event` (`eventid`),
  CONSTRAINT `JoinID` FOREIGN KEY (`JoinID`) REFERENCES `user` (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `JoinTable`
--

LOCK TABLES `JoinTable` WRITE;
/*!40000 ALTER TABLE `JoinTable` DISABLE KEYS */;
INSERT INTO `JoinTable` VALUES (12,35),(13,35),(15,35),(15,37);
/*!40000 ALTER TABLE `JoinTable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `User` (
  `RealName` varchar(20) DEFAULT NULL,
  `NickName` varchar(20) NOT NULL,
  `Gender` varchar(10) DEFAULT NULL,
  `Location` varchar(20) DEFAULT NULL,
  `Email` varchar(40) NOT NULL,
  `Tags` varchar(50) DEFAULT NULL,
  `SelfDescription` varchar(100) DEFAULT NULL,
  `UserID` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`UserID`),
  UNIQUE KEY `Email_UNIQUE` (`Email`),
  UNIQUE KEY `NickName_UNIQUE` (`NickName`),
  UNIQUE KEY `UserID_UNIQUE` (`UserID`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES ('aaa','aaa','aaa','aa','aa','aa','aa',12),('aaa','aab','aaa','aa','ab','aa','aa',13),('aaa','aac','aaa','aa','ac','aa','aa',14),('aaa','aad','aaa','aa','ad','aa','aa',15);
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-27 23:44:16
