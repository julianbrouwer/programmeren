def new_password(oldpassword,newpassword):
    if oldpassword != newpassword and len(newpassword) >= 6:
        return True
    else:
        return False

print(new_password('123456','123457'))