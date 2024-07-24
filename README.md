# HarukaBot——优雅的 B 站推送 QQ 机器人

HarukaBot-Re

## 简介

一款将哔哩哔哩 UP 主的直播与动态信息推送至 QQ 的机器人。

重制版希望解决352问题，并且仍然是onebot标准。

目前只是增加了cookie功能，但是效果不理想。

## 特色功能

HarukaBot 针对不同的推送场景（粉丝群、娱乐群、直播通知群），提供了个性化设置：

- 自定义推送内容，每位 UP 主可限制仅动态、仅直播。
- 群内开启权限限制，仅管理员以上可以使用机器人。
- 指定推送内容@全体成员，次数用光自动忽略。
- 同时连接多个 QQ 号，避免@全体成员次数不够。

## 开发

使用poetry作为包管理器
```
# 创建虚拟环境
poetry env use python
# 安装依赖
poetry install
# 启动机器人
poetry run python bot.py
```

## 许可证
本项目使用 [GNU AGPLv3](https://choosealicense.com/licenses/agpl-3.0/) 作为开源许可证。
