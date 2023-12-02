import json

user_info_path = './data_base/user_info.json'
settings_path = './data_base/settings.json'
# user_info_path = 'user_info.json'
# settings_path = 'settings.json'


def checkAccount(account):
    user_info_file = open(user_info_path, "r", encoding="GBK")
    user_info = json.load(user_info_file)
    user_info_file.close()
    for info in user_info:
        if info['account'] == account:
            return True
    return False


def loginAccount(account, password):
    user_info_file = open(user_info_path, "r", encoding="GBK")
    user_info = json.load(user_info_file)
    user_info_file.close()
    for info in user_info:
        if info['account'] == account and info['password'] == password:
            return True
    return False


def registerAccount(account, password, name, stu_num, per_num):
    new_account = {'account': account, 'password': password, 'name': name,
                   'stu_num': stu_num, 'per_num': per_num}
    user_info_file = open(user_info_path, "r", encoding="GBK")
    user_info = json.load(user_info_file)
    user_info.append(new_account)
    user_info_file = open(user_info_path, "w")
    json.dump(user_info, user_info_file, indent=2, ensure_ascii=False)
    user_info_file.close()


def checkAccountInfo(account, name, stu_num, per_num):
    user_info_file = open(user_info_path, "r", encoding="GBK")
    user_info = json.load(user_info_file)
    user_info_file.close()
    for info in user_info:
        if account != info['account']:
            continue
        if name != info['name']:
            continue
        if stu_num != info['stu_num']:
            continue
        if per_num != info['per_num']:
            continue
        return True
    return False


def resetPassword(account, new_password):
    user_info_file = open(user_info_path, "r", encoding="GBK")
    user_info = json.load(user_info_file)
    user_info_file.close()
    for info in user_info:
        if info['account'] == account:
            info['password'] = new_password
            break
    user_info_file = open(user_info_path, "w")
    json.dump(user_info, user_info_file, indent=2, ensure_ascii=False)
    user_info_file.close()


def settings(setting, check):
    setting_info_file = open(settings_path, "r", encoding='GBK')
    setting_info = json.load(setting_info_file)
    setting_info_file.close()
    setting_info[setting] = check
    if setting == 'reservePassword' and check is False:
        setting_info['password'] = ''
    setting_info_file = open(settings_path, "w", encoding='GBK')
    json.dump(setting_info, setting_info_file, ensure_ascii=False, indent=2)
    setting_info_file.close()


def reservePassword(account, password):
    setting_info_file = open(settings_path, "r", encoding='GBK')
    setting_info = json.load(setting_info_file)
    setting_info_file.close()
    setting_info['accountTmp'] = account
    setting_info['passwordTmp'] = password
    setting_info_file = open(settings_path, "w", encoding='GBK')
    json.dump(setting_info, setting_info_file, ensure_ascii=False, indent=2)
    setting_info_file.close()


def settings_init_check():
    check_list = []
    setting_info_file = open(settings_path, "r", encoding='GBK')
    setting_info = json.load(setting_info_file)
    check_list.append(setting_info['loginAuto'])
    check_list.append(setting_info['reservePassword'])
    setting_info_file.close()
    return check_list


def getAccountTmp():
    setting_info_file = open(settings_path, "r", encoding='GBK')
    setting_info = json.load(setting_info_file)
    account_tmp = setting_info["accountTmp"]
    setting_info_file.close()
    return account_tmp


def getPasswordTmp():
    setting_info_file = open(settings_path, "r", encoding='GBK')
    setting_info = json.load(setting_info_file)
    password_tmp = setting_info["passwordTmp"]
    setting_info_file.close()
    return password_tmp
