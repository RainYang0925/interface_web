/*
Navicat MySQL Data Transfer

Source Server         : tutorial-djangocms
Source Server Version : 50715
Source Host           : localhost:3306
Source Database       : interface_web_test

Target Server Type    : MYSQL
Target Server Version : 50715
File Encoding         : 65001

Date: 2016-10-13 18:30:49
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `group_id` (`group_id`),
  KEY `permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissions_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissions_ibfk_2` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) DEFAULT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `group_id` (`group_id`),
  CONSTRAINT `group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_permissions_ibfk_2` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for directory_tree
-- ----------------------------
DROP TABLE IF EXISTS `directory_tree`;
CREATE TABLE `directory_tree` (
  `id` int(11) NOT NULL COMMENT '左侧的用例树形目录结构',
  `parent_id` int(11) NOT NULL,
  `key` varchar(254) NOT NULL,
  `level` int(11) NOT NULL,
  `project_it` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `project_it` (`project_it`),
  CONSTRAINT `directory_tree_ibfk_1` FOREIGN KEY (`project_it`) REFERENCES `project` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of directory_tree
-- ----------------------------

-- ----------------------------
-- Table structure for it_request_body
-- ----------------------------
DROP TABLE IF EXISTS `it_request_body`;
CREATE TABLE `it_request_body` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `type` int(11) NOT NULL,
  `desc` varchar(254) DEFAULT NULL,
  `value` varchar(254) DEFAULT NULL,
  `it_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `it_id` (`it_id`),
  CONSTRAINT `it_request_body_ibfk_1` FOREIGN KEY (`it_id`) REFERENCES `it_statement` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of it_request_body
-- ----------------------------

-- ----------------------------
-- Table structure for it_request_header
-- ----------------------------
DROP TABLE IF EXISTS `it_request_header`;
CREATE TABLE `it_request_header` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `value` varchar(30) DEFAULT NULL,
  `desc` varchar(254) DEFAULT NULL,
  `it_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `it_id` (`it_id`),
  CONSTRAINT `it_request_header_ibfk_1` FOREIGN KEY (`it_id`) REFERENCES `it_statement` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of it_request_header
-- ----------------------------

-- ----------------------------
-- Table structure for it_respons_body
-- ----------------------------
DROP TABLE IF EXISTS `it_respons_body`;
CREATE TABLE `it_respons_body` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `type` int(11) NOT NULL,
  `desc` varchar(254) DEFAULT NULL,
  `value` varchar(254) DEFAULT NULL,
  `it_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `it_id` (`it_id`),
  CONSTRAINT `it_respons_body_ibfk_1` FOREIGN KEY (`it_id`) REFERENCES `it_statement` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of it_respons_body
-- ----------------------------

-- ----------------------------
-- Table structure for it_respons_header
-- ----------------------------
DROP TABLE IF EXISTS `it_respons_header`;
CREATE TABLE `it_respons_header` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `value` varchar(30) DEFAULT NULL,
  `desc` varchar(254) DEFAULT NULL,
  `it_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `it_id` (`it_id`),
  CONSTRAINT `it_respons_header_ibfk_1` FOREIGN KEY (`it_id`) REFERENCES `it_statement` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of it_respons_header
-- ----------------------------

-- ----------------------------
-- Table structure for it_statement
-- ----------------------------
DROP TABLE IF EXISTS `it_statement`;
CREATE TABLE `it_statement` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `protocol_type` varchar(10) NOT NULL,
  `request_type` varchar(10) NOT NULL,
  `path` varchar(30) DEFAULT NULL,
  `desc` varchar(254) DEFAULT NULL,
  `project_id` int(11) NOT NULL,
  `author` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `project_id` (`project_id`),
  CONSTRAINT `project_id` FOREIGN KEY (`project_id`) REFERENCES `project` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of it_statement
-- ----------------------------

-- ----------------------------
-- Table structure for project
-- ----------------------------
DROP TABLE IF EXISTS `project`;
CREATE TABLE `project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_name` varchar(30) NOT NULL,
  `desc` varchar(254) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `use_id` (`user_id`),
  CONSTRAINT `use_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of project
-- ----------------------------

-- ----------------------------
-- Table structure for testcase
-- ----------------------------
DROP TABLE IF EXISTS `testcase`;
CREATE TABLE `testcase` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `belong_directory` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `belong_directory` (`belong_directory`),
  CONSTRAINT `testcase_ibfk_1` FOREIGN KEY (`belong_directory`) REFERENCES `directory_tree` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of testcase
-- ----------------------------

-- ----------------------------
-- Table structure for testcase_it
-- ----------------------------
DROP TABLE IF EXISTS `testcase_it`;
CREATE TABLE `testcase_it` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `testcase_id` int(11) DEFAULT NULL,
  `it_id` int(11) DEFAULT NULL,
  `index` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `testcase_id` (`testcase_id`),
  KEY `it_id` (`it_id`),
  CONSTRAINT `testcase_it_ibfk_1` FOREIGN KEY (`testcase_id`) REFERENCES `testcase` (`id`),
  CONSTRAINT `testcase_it_ibfk_2` FOREIGN KEY (`it_id`) REFERENCES `it_statement` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of testcase_it
-- ----------------------------
