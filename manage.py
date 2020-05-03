from flask_migrate import MigrateCommand
from flask_script import Manager

from bbs import create_app
from bbs.exts import db

from apps.cms import models as cms_models
from apps.cms.models import CMSUser
from apps.cms.models import CMSRole
from apps.cms.models import CMSPersmission


app = create_app()

manager = Manager(app=app)

manager.add_command('db', MigrateCommand)


@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
@manager.option('-e', '--email', dest='email')
def create_cms_user(username, password, email):
    user = CMSUser(username=username, password=password, email=email)
    db.session.add(user)
    db.session.commit()
    print('CMS 添加用户成功')


@manager.command
def create_role():
    # 1. 访问者(可修改个人角色)
    visitor = CMSRole(name='访问者', desc='只能查看相关数据, 不能修改')
    visitor.permission = CMSPersmission.VISITOR
    # 2. 运营角色(可修改个人角色, 管理帖子, 管理评论, 管理前台人员)
    operator = CMSRole(name='运营', desc='管理帖子,管理评论,管理板块')
    operator.permission = CMSPersmission.VISITOR | CMSPersmission.POSTER | CMSPersmission.COMMENTER | CMSPersmission.BOARDER
    # 3. 管理员()
    admin = CMSRole(name='管理员', desc='拥有本系统所有权限')
    admin.permission = CMSPersmission.VISITOR | CMSPersmission.POSTER | CMSPersmission.COMMENTER | CMSPersmission.BOARDER| CMSPersmission.FRONTUSER | CMSPersmission.CMSUSER 
    # 4. 开发者
    developer = CMSRole(name='开发者', desc='开发人员专用角色')
    developer.permission = CMSPersmission.ALL_PERMISSION

    db.session.add_all([visitor, operator, admin, developer])
    db.session.commit()


@manager.option('-e', '--email', dest='email')
@manager.option('-n', '--name', dest='name')
def add_user_to_role(email, name):
    user = CMSUser.query.filter_by(email=email).first()
    if user:
        role = CMSRole.query.filter_by(name=name).first()
        if role:
            role.users.append(user)
            db.session.commit()
            print('用户添加到角色成功')
        else:
            print('没有这个角色: %s' % name)
        pass
    else:
        print('%s 没有这个用户' % email)


@manager.option('-e', '--email', dest='email')
def test_permission(email):
    user = CMSUser.query.filter_by(email=email).first()
    if user.has_permission(CMSPersmission.VISITOR):
        print('%s 用户有访问者权限' % email)
    else:
        print('%s 没有访问者权限' % email)


if __name__ == '__main__':
    manager.run()