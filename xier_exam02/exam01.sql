/*
SQLyog Community v13.1.7 (64 bit)
MySQL - 8.0.30 : Database - fzuxier
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`fzuxier` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `fzuxier`;

/*Table structure for table `exam01` */

DROP TABLE IF EXISTS `exam01`;

CREATE TABLE `exam01` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `notifier` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `title` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `date` varchar(30) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `link` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=181 DEFAULT CHARSET=utf8mb3;

/*Data for the table `exam01` */

insert  into `exam01`(`id`,`notifier`,`title`,`date`,`link`) values 
(121,'【实践科】\r\n             ','关于做好国家、省级大学生创新创业训练计划项目结题工作的通知','\r\n2023-05-18\r\n         ','https://jwch.fzu.edu.cn/../info/1039/12774.htm'),
(122,'【教材中心】\r\n             ','关于做好2023-2024学年第一学期教材选用及征订工作的通知','\r\n2023-05-18\r\n         ','https://jwch.fzu.edu.cn/../info/1042/12773.htm'),
(123,'【注册中心】\r\n             ','关于2022-2023学年第二学期《近现代史纲要》课程期末考试安排的通知','\r\n2023-05-17\r\n         ','https://jwch.fzu.edu.cn/../info/1036/12771.htm'),
(124,'【教研教改】\r\n             ','福州大学关于公布2021级数理综合班专业分流学生名单及学科导师名单的通知','\r\n2023-05-17\r\n         ','https://jwch.fzu.edu.cn/../info/1037/12770.htm'),
(125,'【实践科】\r\n             ','关于公布福州大学第七届网络信息安全竞赛获奖名单的通知','\r\n2023-05-17\r\n         ','https://jwch.fzu.edu.cn/../info/1039/12769.htm'),
(126,'【质量办】\r\n             ','关于举办福州大学第四十一场“教学有道”研讨活动的通知','\r\n2023-05-16\r\n         ','https://jwch.fzu.edu.cn/../info/1040/12768.htm'),
(127,'【注册中心】\r\n             ','关于2024届预计毕业生核对电子注册学历信息的通知','\r\n2023-05-16\r\n         ','https://jwch.fzu.edu.cn/../info/1036/12765.htm'),
(128,'【计划科】\r\n             ','关于组织申报2023-2024学年第一学期通识教育选修课的通知','\r\n2023-05-15\r\n         ','https://jwch.fzu.edu.cn/../info/1038/12762.htm'),
(129,'【注册中心】\r\n             ','关于2022-2023学年第二学期计算机语言类课程期末考试安排的通知','\r\n2023-05-12\r\n         ','https://jwch.fzu.edu.cn/../info/1036/12761.htm'),
(130,'【质量办】\r\n             ','关于举办福州大学第四十场“教学有道”研讨活动的通知','\r\n2023-05-12\r\n         ','https://jwch.fzu.edu.cn/../info/1040/12760.htm'),
(131,'【质量办】\r\n             ','关于开展2023届本科毕业生座谈会的通知','\r\n2023-05-12\r\n         ','https://jwch.fzu.edu.cn/../info/1040/12759.htm'),
(132,'【实践科】\r\n             ','关于公布福州大学第九届“汇仟杯”测量大赛获奖名单的通知','\r\n2023-05-08\r\n         ','https://jwch.fzu.edu.cn/../info/1039/12750.htm'),
(133,'【计划科】\r\n             ','2022-2023学年第二学期在校学生申请辅修专业的通知','\r\n2023-05-08\r\n         ','https://jwch.fzu.edu.cn/../info/1038/12749.htm'),
(134,'【教研教改】\r\n             ','福州大学关于开展2022-2023学年本科教学优秀奖评选工作的通知','\r\n2023-05-05\r\n         ','https://jwch.fzu.edu.cn/../info/1037/12747.htm'),
(135,'【质量办】\r\n             ','关于举办福州大学第三十九场“教学有道”研讨活动的通知','\r\n2023-05-05\r\n         ','https://jwch.fzu.edu.cn/../info/1040/12746.htm'),
(136,'【实践科】\r\n             ','关于组织申报2023年本科生开放探索性实验项目（课程）的通知','\r\n2023-05-05\r\n         ','https://jwch.fzu.edu.cn/../info/1039/12745.htm'),
(137,'【实践科】\r\n             ','关于开展2023届本科毕业设计（论文）抽检送审工作的通知','\r\n2023-04-26\r\n         ','https://jwch.fzu.edu.cn/../info/1039/12723.htm'),
(138,'【实践科】\r\n             ','关于对2023届本科毕业设计（论文）进行查重检测的通知','\r\n2023-04-26\r\n         ','https://jwch.fzu.edu.cn/../info/1039/12722.htm'),
(139,'【实践科】\r\n             ','关于试用本科毕业设计（论文）管理模块的通知','\r\n2023-04-26\r\n         ','https://jwch.fzu.edu.cn/../info/1039/12721.htm'),
(140,'【注册中心】\r\n             ','关于2022-2023学年第二学期《工程制图E》课程期末考试安排的通知','\r\n2023-04-25\r\n         ','https://jwch.fzu.edu.cn/../info/1036/12718.htm'),
(141,'【计划科】\r\n             ','关于公布2023-2024学年第一学期修读辅修专业学生名单的通知','\r\n2023-06-12\r\n         ','https://jwch.fzu.edu.cn/../info/1038/12829.htm'),
(142,'【注册中心】\r\n             ','关于2022-2023学年第二学期《大学英语（二）、（三）、（四）》课程期末考试安排的通知','\r\n2023-06-09\r\n         ','https://jwch.fzu.edu.cn/../info/1036/12828.htm'),
(143,'【注册中心】\r\n             ','关于2022-2023学年第二学期《工程制图A（下）、C（下）、D、F》课程期末考试安排的通知','\r\n2023-06-09\r\n         ','https://jwch.fzu.edu.cn/../info/1036/12827.htm'),
(144,'【综合科】\r\n             ','关于转发12306手机客户端提供学生优惠资质在线核验服务的通知','\r\n2023-06-07\r\n         ','https://jwch.fzu.edu.cn/../info/1035/12821.htm'),
(145,'【计划科】\r\n             ','关于2023-2024学年第一学期修读辅修专业学生名单的公示','\r\n2023-06-05\r\n         ','https://jwch.fzu.edu.cn/../info/1038/12808.htm'),
(146,'【注册中心】\r\n             ','关于2022-2023学年第二学期《概率论与数理统计》课程期末考试安排的通知','\r\n2023-06-01\r\n         ','https://jwch.fzu.edu.cn/../info/1036/12807.htm'),
(147,'【实践科】\r\n             ','关于公布第二十九期本科生科研训练计划立项项目的通知','\r\n2023-05-31\r\n         ','https://jwch.fzu.edu.cn/../info/1039/12805.htm'),
(148,'【实践科】\r\n             ','关于公布2023年本科生创新创业实践与素质拓展学分认定结果的通知','\r\n2023-05-30\r\n         ','https://jwch.fzu.edu.cn/../info/1039/12804.htm'),
(149,'【实践科】\r\n             ','关于公布福州大学第九届桥梁设计大赛获奖名单的通知','\r\n2023-05-30\r\n         ','https://jwch.fzu.edu.cn/../info/1039/12803.htm'),
(150,'【实践科】\r\n             ','关于公布福州大学第十三届大学生节能减排社会实践与科技竞赛暨第九届材料创新、设计及应用竞赛获奖名单的通知','\r\n2023-05-30\r\n         ','https://jwch.fzu.edu.cn/../info/1039/12802.htm'),
(151,'【实践科】\r\n             ','关于公布福州大学第三届大学生先进成图技术与产品信息建模创新大赛获奖名单的通知','\r\n2023-05-30\r\n         ','https://jwch.fzu.edu.cn/../info/1039/12801.htm'),
(152,'【注册中心】\r\n             ','关于2022-2023学年第二学期《思想道德与法治》课程期末考试安排的通知','\r\n2023-05-26\r\n         ','https://jwch.fzu.edu.cn/../info/1036/12798.htm'),
(153,'【注册中心】\r\n             ','关于2022-2023学年第二学期《毛泽东思想和中国特色社会主义理论体系概论》课程期末考试安排的通知','\r\n2023-05-26\r\n         ','https://jwch.fzu.edu.cn/../info/1036/12797.htm'),
(154,'【注册中心】\r\n             ','关于2022-2023学年第二学期《马克思主义基本原理》课程期末考试安排的通知','\r\n2023-05-26\r\n         ','https://jwch.fzu.edu.cn/../info/1036/12796.htm'),
(155,'【注册中心】\r\n             ','关于2022-2023学年第二学期《高等数学A（中）、B（下）、C（下）》课程期末考试安排的通知','\r\n2023-05-26\r\n         ','https://jwch.fzu.edu.cn/../info/1036/12794.htm'),
(156,'【注册中心】\r\n             ','关于2022-2023学年第二学期《线性代数》、《线性代数与解析几何》课程期末考试安排的通知','\r\n2023-05-24\r\n         ','https://jwch.fzu.edu.cn/../info/1036/12783.htm'),
(157,'【教研教改】\r\n             ','福州大学关于开展第七届远志创业实验班招生工作的通知','\r\n2023-05-22\r\n         ','https://jwch.fzu.edu.cn/../info/1037/12779.htm'),
(158,'【质量办】\r\n             ','关于举办福州大学第四十二场“教学有道”研讨活动的通知','\r\n2023-05-22\r\n         ','https://jwch.fzu.edu.cn/../info/1040/12778.htm'),
(159,'【综合科】\r\n             ','关于2022-2023学年第二学期再次开放本科生学生证和火车票优惠卡补办及火车票优惠卡更改区间的通知','\r\n2023-05-22\r\n         ','https://jwch.fzu.edu.cn/../info/1035/12776.htm'),
(160,'【实践科】\r\n             ','关于做好第二十七期、二十八期本科生科研训练计划项目结题工作的通知','\r\n2023-05-18\r\n         ','https://jwch.fzu.edu.cn/../info/1039/12775.htm'),
(161,'【综合科】\r\n             ','教务处关于2023年暑假用印安排的通知','\r\n2023-07-08\r\n         ','https://jwch.fzu.edu.cn/../info/1035/12884.htm'),
(162,'【实践科】\r\n             ','关于公布福州大学2023届本科生优秀毕业设计（论文）名单的通知','\r\n2023-07-05\r\n         ','https://jwch.fzu.edu.cn/../info/1039/12881.htm'),
(163,'【综合科】\r\n             ','关于召开2022-2023学年春季学期期末本科教育教学工作会议的通知','\r\n2023-07-03\r\n         ','https://jwch.fzu.edu.cn/../info/1035/12874.htm'),
(164,'【注册中心】\r\n             ','关于做好期末复习考试及下学期开学等工作的通知','\r\n2023-06-30\r\n         ','https://jwch.fzu.edu.cn/../info/1036/12870.htm'),
(165,'【质量办】\r\n             ','关于举办福州大学第四十四场“教学有道”研讨活动的通知','\r\n2023-06-30\r\n         ','https://jwch.fzu.edu.cn/../info/1040/12868.htm'),
(166,'【实践科】\r\n             ','关于参加“2023高教社杯全国大学生数学建模竞赛”报名与集训的通知','\r\n2023-06-29\r\n         ','https://jwch.fzu.edu.cn/../info/1039/12867.htm'),
(167,'【计划科】\r\n             ','关于核对2023-2024学年第一学期通识教育选修课开课信息的有关通知','\r\n2023-06-27\r\n         ','https://jwch.fzu.edu.cn/../info/1038/12863.htm'),
(168,'【实践科】\r\n             ','关于公布2023年国家级、省级大学生创新创业训练计划推荐立项项目的通知','\r\n2023-06-26\r\n         ','https://jwch.fzu.edu.cn/../info/1039/12862.htm'),
(169,'【注册中心】\r\n             ','关于2022-2023学年第二学期大学英语拓展课程期末考试安排的通知','\r\n2023-06-21\r\n         ','https://jwch.fzu.edu.cn/../info/1036/12850.htm'),
(170,'【注册中心】\r\n             ','关于2022-2023学年第二学期《大学物理A（上）、B（上）、C》课程期末考试安排的通知','\r\n2023-06-21\r\n         ','https://jwch.fzu.edu.cn/../info/1036/12848.htm'),
(171,'【实践科】\r\n             ','关于举办2023年福州大学大学生工程实践与创新能力大赛暨2023年福建省大学生工程实践与创新能力大赛福州大学分区赛的通知','\r\n2023-06-20\r\n         ','https://jwch.fzu.edu.cn/../info/1039/12847.htm'),
(172,'【实践科】\r\n             ','关于公布第十四届企业经营模拟沙盘对抗赛获奖名单的通知','\r\n2023-06-20\r\n         ','https://jwch.fzu.edu.cn/../info/1039/12846.htm'),
(173,'【实践科】\r\n             ','关于公布2023年大学生电子设计竞赛暨全国大学生电子设计竞赛选拔赛获奖名单的通知','\r\n2023-06-20\r\n         ','https://jwch.fzu.edu.cn/../info/1039/12845.htm'),
(174,'【实践科】\r\n             ','关于公布第二十届程序设计竞赛获奖名单的通知','\r\n2023-06-20\r\n         ','https://jwch.fzu.edu.cn/../info/1039/12844.htm'),
(175,'【实践科】\r\n             ','关于公布2023年第二十三届数学竞赛获奖名单的通知','\r\n2023-06-20\r\n         ','https://jwch.fzu.edu.cn/../info/1039/12843.htm'),
(176,'【注册中心】\r\n             ','关于2023年端午节放假课程调整的通知','\r\n2023-06-19\r\n         ','https://jwch.fzu.edu.cn/../info/1036/12842.htm'),
(177,'【注册中心】\r\n             ','关于2023-2024学年第一学期本科生学期选课的通知','\r\n2023-06-19\r\n         ','https://jwch.fzu.edu.cn/../info/1036/12841.htm'),
(178,'【质量办】\r\n             ','关于举办福州大学第四十三场“教学有道”研讨活动的通知','\r\n2023-06-15\r\n         ','https://jwch.fzu.edu.cn/../info/1040/12835.htm'),
(179,'【教研教改】\r\n             ','福州大学关于开展2023年省级一流本科课程申报推荐工作的通知','\r\n2023-06-14\r\n         ','https://jwch.fzu.edu.cn/../info/1037/12832.htm'),
(180,'【教研教改】\r\n             ','福州大学关于公布2021级数理金融实验班学生主辅修专业及导师名单的通知','\r\n2023-06-13\r\n         ','https://jwch.fzu.edu.cn/../info/1037/12830.htm');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
