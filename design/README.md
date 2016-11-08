# 数据库修改记录

**2016.11.1**
1. 新增两张表tag（标签），tag_map（记录和testcase的映射关系）
2. 表it_statement和testcase添加了responsible字段（责任人），timestamp字段（记录上次修改时间）
3. 表testcase增加tags字段（标签，多个用“，”隔开）

**2016.11.2**
1. 添加了外键依赖，testcase的responsible参照auth_user，it_statement的responsible和author分别惨遭auth_user
