from Crypto.Cipher import AES

import SQL.SqlBase as SqlBase

dic_user_id = {}


class EncryptDate:
  def __init__(self, key):
    self.key = key.encode("utf-8")  # 初始化密钥
    self.length = AES.block_size  # 初始化数据块大小
    self.aes = AES.new(self.key, AES.MODE_ECB)  # 初始化AES,ECB模式的实例
    self.un_pad = lambda date: date[0:-ord(date[-1])]

  def pad(self, text):
    """
    #填充函数，使被加密数据的字节码长度是block_size的整数倍
    """
    count = len(text.encode('GB2312'))
    add = self.length - (count % self.length)
    entext = text + (chr(add) * add)
    return entext

  def encrypt(self, encrData):  # 加密函数
    res = self.aes.encrypt(self.pad(encrData).encode("GB2312"))
    print(res.hex())
    return res

  def decrypt(self, decrData, id):  # 解密函数
    try:
      res_bytes = self.aes.decrypt(decrData)
      hex_string = res_bytes.hex().split('0d')[0]
      print(hex_string)
      bytes_obj = bytes.fromhex(hex_string)
      # 尝试使用UTF-8编码解码
      text = bytes_obj.decode('GB2312')
      hex_string = res_bytes.hex()[len(hex_string) + 2:]
      print(hex_string)
      bytes_obj = bytes.fromhex(hex_string)
      msg = bytes_obj.decode("utf8")
      psw = self.un_pad(msg)
      dic_user_id[text] = str(id)
    except:
      pass

  def get_psw(self, decrData):
    try:
      res_bytes = self.aes.decrypt(decrData)
      hex_string = res_bytes.hex().split('0d')[0]
      print(hex_string)
      bytes_obj = bytes.fromhex(hex_string)
      # 尝试使用UTF-8编码解码
      text = bytes_obj.decode('GB2312')
      hex_string = res_bytes.hex()[len(hex_string) + 2:]
      print(hex_string)
      bytes_obj = bytes.fromhex(hex_string)
      msg = bytes_obj.decode("utf8")
      psw = self.un_pad(msg)
      return psw
    except Exception as e:
      pass


eg = EncryptDate("apId>tD8%9)s$sylxc@d27xqkgHROsuk")  # 这里密钥的长度必须是16的倍数


def set_refresh():
  s0 = f"""select ID,UserP from tUrC0_User"""
  df = SqlBase.get_table(s0)
  for i in range(df.shape[0]):
    eg.decrypt(df.iloc[i]["UserP"], df.iloc[i]["ID"])


def get_login(s_username, s_password):
  if s_username not in dic_user_id:
    set_refresh()
    for a, d in dic_user_id.items():
      print(f"{a}:{d}")
  if s_username not in dic_user_id:
    return False
  s0 = f"select UserP from tUrC0_User where ID={dic_user_id[s_username]}"
  aaa = SqlBase.get_rows(s0)
  bb = aaa[0][0]
  print(bb)
  print(type(bb))
  psw = eg.get_psw(bb)
  if psw == s_password:
    return True
  # print(s_username, s_password)
  return False
