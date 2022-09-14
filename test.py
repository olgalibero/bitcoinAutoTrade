import pyupbit

access = "f2rRgzXkXqN6D0OOaVsxZZufhwhvKOEcFjxzMynx"          # 본인 값으로 변경
secret = "x9iZy0mitjjfxvhKYbVVQIIPmTFGhhsO3ySCxKBB"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회