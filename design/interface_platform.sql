/*
Navicat MySQL Data Transfer

Source Server         : myCon
Source Server Version : 50715
Source Host           : localhost:3306
Source Database       : interface_platform

Target Server Type    : MYSQL
Target Server Version : 50715
File Encoding         : 65001

Date: 2016-11-03 16:01:47
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_58c48ba9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8;

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
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_30a071c9_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_30a071c9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_24702650_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_7cd7acb6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for interface_platform_directorytree
-- ----------------------------
DROP TABLE IF EXISTS `interface_platform_directorytree`;
CREATE TABLE `interface_platform_directorytree` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `parent_id` int(11) NOT NULL,
  `name` varchar(254) NOT NULL,
  `key` varchar(100) NOT NULL,
  `level` int(11) NOT NULL,
  `project_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interface_p_project_id_4855b441_fk_interface_platform_project_id` (`project_id`),
  CONSTRAINT `interface_p_project_id_4855b441_fk_interface_platform_project_id` FOREIGN KEY (`project_id`) REFERENCES `interface_platform_project` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for interface_platform_itbody
-- ----------------------------
DROP TABLE IF EXISTS `interface_platform_itbody`;
CREATE TABLE `interface_platform_itbody` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `type` int(11) NOT NULL,
  `desc` varchar(254) NOT NULL,
  `value` varchar(254) NOT NULL,
  `it_id` int(11) NOT NULL,
  `body_type` smallint(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interface_pl_it_id_2fc68801_fk_interface_platform_itstatement_id` (`it_id`),
  CONSTRAINT `interface_pl_it_id_2fc68801_fk_interface_platform_itstatement_id` FOREIGN KEY (`it_id`) REFERENCES `interface_platform_itstatement` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for interface_platform_itheader
-- ----------------------------
DROP TABLE IF EXISTS `interface_platform_itheader`;
CREATE TABLE `interface_platform_itheader` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `value` varchar(254) NOT NULL,
  `desc` varchar(254) NOT NULL,
  `it_id` int(11) NOT NULL,
  `header_type` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interface_pl_it_id_10388ee4_fk_interface_platform_itstatement_id` (`it_id`),
  CONSTRAINT `interface_pl_it_id_10388ee4_fk_interface_platform_itstatement_id` FOREIGN KEY (`it_id`) REFERENCES `interface_platform_itstatement` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for interface_platform_itlog
-- ----------------------------
DROP TABLE IF EXISTS `interface_platform_itlog`;
CREATE TABLE `interface_platform_itlog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `it_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `timestamp` datetime NOT NULL,
  `log_path` varchar(254) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interface_pl_it_id_10c78f1c_fk_interface_platform_itstatement_id` (`it_id`),
  CONSTRAINT `interface_pl_it_id_10c78f1c_fk_interface_platform_itstatement_id` FOREIGN KEY (`it_id`) REFERENCES `interface_platform_itstatement` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for interface_platform_itstatement
-- ----------------------------
DROP TABLE IF EXISTS `interface_platform_itstatement`;
CREATE TABLE `interface_platform_itstatement` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `protocol_type` varchar(10) NOT NULL,
  `request_type` varchar(10) NOT NULL,
  `path` varchar(200) NOT NULL,
  `desc` varchar(254) NOT NULL,
  `project_id` int(11) NOT NULL,
  `author_id` int(11) NOT NULL,
  `host_id` int(11) NOT NULL,
  `status` smallint(6) NOT NULL,
  `responsible_id` int(11) NOT NULL,
  `timestamp` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interface_p_project_id_168186da_fk_interface_platform_project_id` (`project_id`),
  KEY `interface_platform_itstatemen_author_id_6a2dc7c9_fk_auth_user_id` (`author_id`),
  KEY `interface_platform_itsta_responsible_id_52ff119d_fk_auth_user_id` (`responsible_id`),
  CONSTRAINT `interface_p_project_id_168186da_fk_interface_platform_project_id` FOREIGN KEY (`project_id`) REFERENCES `interface_platform_project` (`id`),
  CONSTRAINT `interface_platform_itsta_responsible_id_52ff119d_fk_auth_user_id` FOREIGN KEY (`responsible_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `interface_platform_itstatemen_author_id_6a2dc7c9_fk_auth_user_id` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for interface_platform_project
-- ----------------------------
DROP TABLE IF EXISTS `interface_platform_project`;
CREATE TABLE `interface_platform_project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `desc` varchar(254) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interface_platform_project_user_id_21aa308e_fk_auth_user_id` (`user_id`),
  CONSTRAINT `interface_platform_project_user_id_21aa308e_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for interface_platform_tag
-- ----------------------------
DROP TABLE IF EXISTS `interface_platform_tag`;
CREATE TABLE `interface_platform_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(254) NOT NULL,
  `num` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for interface_platform_tagmap
-- ----------------------------
DROP TABLE IF EXISTS `interface_platform_tagmap`;
CREATE TABLE `interface_platform_tagmap` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tag_id` int(11) NOT NULL,
  `tc_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interface_platform__tag_id_3076b34e_fk_interface_platform_tag_id` (`tag_id`),
  KEY `interface_platf_tc_id_3c27b8d4_fk_interface_platform_testcase_id` (`tc_id`),
  CONSTRAINT `interface_platf_tc_id_3c27b8d4_fk_interface_platform_testcase_id` FOREIGN KEY (`tc_id`) REFERENCES `interface_platform_testcase` (`id`),
  CONSTRAINT `interface_platform__tag_id_3076b34e_fk_interface_platform_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `interface_platform_tag` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for interface_platform_testcase
-- ----------------------------
DROP TABLE IF EXISTS `interface_platform_testcase`;
CREATE TABLE `interface_platform_testcase` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(254) NOT NULL,
  `belong_id` int(11) NOT NULL,
  `status` smallint(6) NOT NULL,
  `responsible_id` int(11) NOT NULL,
  `timestamp` datetime NOT NULL,
  `tags` varchar(254) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interf_belong_id_7fac4a86_fk_interface_platform_directorytree_id` (`belong_id`),
  KEY `interface_platform_testc_responsible_id_4b1a8fc2_fk_auth_user_id` (`responsible_id`),
  CONSTRAINT `interf_belong_id_7fac4a86_fk_interface_platform_directorytree_id` FOREIGN KEY (`belong_id`) REFERENCES `interface_platform_directorytree` (`id`),
  CONSTRAINT `interface_platform_testc_responsible_id_4b1a8fc2_fk_auth_user_id` FOREIGN KEY (`responsible_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for interface_platform_testcaselog
-- ----------------------------
DROP TABLE IF EXISTS `interface_platform_testcaselog`;
CREATE TABLE `interface_platform_testcaselog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tc_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `timestamp` datetime NOT NULL,
  `log_path` varchar(254) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interface_platf_tc_id_252a5f49_fk_interface_platform_testcase_id` (`tc_id`),
  CONSTRAINT `interface_platf_tc_id_252a5f49_fk_interface_platform_testcase_id` FOREIGN KEY (`tc_id`) REFERENCES `interface_platform_testcase` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for interface_platform_testcasestep
-- ----------------------------
DROP TABLE IF EXISTS `interface_platform_testcasestep`;
CREATE TABLE `interface_platform_testcasestep` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tc_id` int(11) NOT NULL,
  `it_id` int(11) NOT NULL,
  `it_index` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interface_platf_tc_id_4e02a922_fk_interface_platform_testcase_id` (`tc_id`),
  KEY `interface_pl_it_id_2cb03d32_fk_interface_platform_itstatement_id` (`it_id`),
  CONSTRAINT `interface_pl_it_id_2cb03d32_fk_interface_platform_itstatement_id` FOREIGN KEY (`it_id`) REFERENCES `interface_platform_itstatement` (`id`),
  CONSTRAINT `interface_platf_tc_id_4e02a922_fk_interface_platform_testcase_id` FOREIGN KEY (`tc_id`) REFERENCES `interface_platform_testcase` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for interface_platform_variable
-- ----------------------------
DROP TABLE IF EXISTS `interface_platform_variable`;
CREATE TABLE `interface_platform_variable` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `desc` varchar(254) NOT NULL,
  `value` varchar(254) NOT NULL,
  `project_id` int(11) NOT NULL,
  `type` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `interface_pl_project_id_800f4bd_fk_interface_platform_project_id` (`project_id`),
  CONSTRAINT `interface_pl_project_id_800f4bd_fk_interface_platform_project_id` FOREIGN KEY (`project_id`) REFERENCES `interface_platform_project` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
