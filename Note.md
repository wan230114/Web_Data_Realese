# Django配置

## 环境准备

```bash
conda remove -y -n django --all
conda create -y -n django python=3
conda activate django
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/  django-userena
```

## Django测试
```bash
## django项目 start
django-admin startproject runDataRelease
cd runDataRelease

python3 manage.py startapp login

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py check_permissions

python3 manage.py runserver
```

## APP配置

login/models.py
runDataRelease/settings.py

---
## 参考

参考：
[django入门学习-用户登录_qq_40398826的博客-CSDN博客](https://blog.csdn.net/qq_40398826/article/details/106197354)

无用参考：
[Django 用 userena 做用户注册验证登陆 - 震撼起飞 - 博客园](https://www.cnblogs.com/zhenfei/p/6421424.html)

---
## Django 在线 模板 资源

[Django Package Review -- Episode 1 - Django Allauth_哔哩哔哩 (゜-゜)つロ 干杯~-bilibili](https://www.bilibili.com/video/BV1D64y1M7BC?from=search&seid=8279541351252556615)

[Alex-CodeLab/django-base-template: Project Template for Django2 + Bootstrap3 + pre-configured apps (like Allauth, django_compressor ). Probably the fastest way to start up a complete Django project.](https://github.com/Alex-CodeLab/django-base-template)

```bash
wget https://raw.githubusercontent.com/Alex-CodeLab/django-base-template/master/install.sh
```

* [ ] [Django 2.0 项目实战: 扩展Django自带User模型，实现用户注册与登录](https://mp.weixin.qq.com/s?src=11&timestamp=1603101271&ver=2654&signature=tiT9OsjX78nZ4smOp0QQy6UHttL8YsCeoiNGB*mUZs1f5UHjAKpQgLYONWHstTlroYqwVp*lpco*JgoRDbW*U*GCmFRh6VtXIy0akxtzfYUS1j4T46QleDjBkEInMYIU&new=1)


---
# Docker + ngnix 方案
问题：
- [ ] 后期管理不够灵活，每次释放数据都要去重新开一个账户以及服务。

```bash
cd $workdir
# 进入容器
docker pull nginx
{
    docker run \
        --name nginx_dataRealese \
        -p 127.0.0.1:5000:5000 \
        -dit nginx  /bin/bash
}
docker ps
docker exec -it nginx_dataRealese bash # 登录

# 方式2：  参考 https://www.cnblogs.com/saneri/p/11799865.html
docker run --rm --name nginx-test -p 8080:80 -d nginx

```

