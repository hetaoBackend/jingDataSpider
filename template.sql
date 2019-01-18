-- you should write a create-table sql to create a table
-- ----------------------------
-- Table structure for template
-- ----------------------------
DROP TABLE IF EXISTS `template`;
CREATE TABLE `template` (
  `ID` int(64) auto_increment COMMENT '自动ID',
  `AlbID` int(32) NOT NULL COMMENT '专辑ID',
  `AlbName` varchar(255) NOT NULL COMMENT '专辑名称',
  `ProID` int(32) NOT NULL COMMENT '制作人ID',
  `ProName` varchar(255) NOT NULL COMMENT '制作人名称',
  `School` varchar(255) DEFAULT NULL COMMENT '流派',
  `Language` varchar(255) DEFAULT NULL COMMENT '语种',
  `TimePub` datetime DEFAULT NULL COMMENT '发行时间',
  `Company` varchar(255) DEFAULT NULL COMMENT '发行公司',
  `SalNum` int(32) DEFAULT NULL COMMENT '已售张数',
  `PerPrice` int(11) DEFAULT NULL COMMENT '单价',
  `Intro` mediumtext COMMENT '简介',
  `SelCom` int(32) DEFAULT NULL COMMENT '精选评论数',
  `AllCom` int(32) DEFAULT NULL COMMENT '全部评论数',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
