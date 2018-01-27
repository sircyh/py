import datetime

class IUseRepository:
    def fetch_one_by_user_pwd(self,username,pwd):
        pass
    def fetch_one_by_email_pwd(self,email,pwd):
        pass
    def update_last_login_bu_nid(self,nid,current_date):
        pass


class VipType:
    VIP_TYPE=(
        {"nid":1,"caption":'铜牌'},
        {"nid": 2, "caption": '银牌'},
        {"nid": 3, "caption": '金牌'},
        {"nid": 4, "caption": '铂金'},
    )
    def __init__(self, nid):
        self.nid = nid

    def get_caption(self):
        caption = None
        for item in VipType.VIP_TYPE:
            if item['nid'] == self.nid:
                caption = item['caption']
                break
        return caption

    caption = property(get_caption())

class UserType:
    USER_TYPE=(
        {"nid":1,"caption":'用户'},
        {"nid": 2, "caption": '商户'},
        {"nid": 3, "caption": '管理员'},
    )
    def __init__(self,nid):
        self.nid=nid
    def get_caption(self):
        caption = None
        for item in UserType.USER_TYPE:
            if item['nid']==self.nid:
                caption=item['caption']
                break
        return caption
    caption = property(get_caption())

class User:
    def __init__(self,nid,username,email,last_login,user_type,vip_type):
        self.nid=nid
        self.username=username
        self.email=email
        self.last_login=last_login
        self.user_type=user_type
        self.vip_type=vip_type

class UserService:
    def __init__(self,user_repository):
        self.userRepository = user_repository

    def check_login(self,username=None,email=None,password=None):
        if username:
            user_model = self.userRepository.fetch_one_by_user_pwd(username,password)
        else:
            user_model = self.userRepository.fetch_one_by_email_pwd(email,password)
        if user_model:
            current_date = datetime.datetime.now()
            self.userRepository.update_last_login_bu_nid(user_model.nid,current_date)
        return user_model