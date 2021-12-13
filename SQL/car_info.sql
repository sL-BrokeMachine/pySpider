/*
 Navicat Premium Data Transfer

 Source Server         : local_wamp_mysql_5.5.20
 Source Server Type    : MySQL
 Source Server Version : 80027
 Source Host           : localhost:3306
 Source Schema         : dongchedi

 Target Server Type    : MySQL
 Target Server Version : 80027
 File Encoding         : 65001

 Date: 13/12/2021 13:42:27
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for car_info
-- ----------------------------
DROP TABLE IF EXISTS `car_info`;
CREATE TABLE `car_info`  (
  `id` int(0) NOT NULL AUTO_INCREMENT COMMENT '唯一标识id主键',
  `series_id` int(0) NOT NULL COMMENT '汽车系列号',
  `brand_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '汽车品牌名称',
  `series_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '汽车名称',
  `min_price` decimal(5, 2) NULL DEFAULT NULL COMMENT '经销商最低指导价格',
  `max_price` decimal(5, 2) NOT NULL COMMENT '经销商最高指导价格',
  `count` int(0) NOT NULL COMMENT '汽车销量',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
