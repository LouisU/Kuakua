from django.db import models

# Create your models here.


class Person(models.Model):
  # id
  # 微信名
  # 性别
  # 微信uuid
  # 是否注册成功
  pass


class Room(models.Model):
  # id
  # 房间名称
  # 房间属性
  # 房间是否成型
  pass


class RoomPersion(models.Model):
  # room id(FK)
  # person id(FK)
  pass


class VerificationCode(models.Model):
  # id
  # 用户手机或者uuid或者邮件
  # verification code
  # 过期时间
  pass


class Event(models.Model):
  # id
  # Event description
  # Event 分值
  # Event 发生时间
  # Event 依据: 来自rules的具体依据(可能是一条或者多条)
  # Room id(FK)
  # Persion id(KF)
  pass


class Rule(models.Model):
  # id
  # rule description
  # rule 分值
  # 有效期
  pass


class RuleEvent(models.Model):
  # id
  # rule id (FK)
  # event id (FK)
  # rule命中次数
  # rule出现次数在event中占比
  # update time
  pass


# 当创建rule的时候 只是添加了rule记录
# 当创建event的时候 需要添加Event和RuleEvent的记录，也需要重新计算个人总分。
#     其中RuleEvent需要重新计算命中次数和占比


class PersonStatic(models.Model):
  # id
  # persion id
  # event 总分
  # 更新时间 （每天凌晨计算，每天清晨4点更新，故更新时间应该为每天清晨4点）
  pass


class RoomStatic(models.Model):
  # id
  # room id
  # event 总分
  # 更新时间 （每天凌晨计算，每天清晨4点更新，故更新时间应该为每天清晨4点）
  pass

# RoomStatic的计算是基于PersonStatic的结果再计算
# 第二阶段：
#     根据PersonStatic和RoomStatic形成线图展示 7天 月 季 年。


class ImpressiveDate(models.Model):
  # id
  # date
  # date description
  # update time
  # Room id(FK)
  # remind
  # remind start date
  # remind cycle
  pass

# celery work 根据remind=true的记录 根基remind date remind cycle 决定是否发送提醒。默认提前三天提醒，三天内每天提醒一次。

