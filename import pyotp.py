import pyotp
import qrcode

print(pyotp.random_base32())

cle = "L6UGBKHYTL36DWZ557FRLH7O7GU2RVJK"

uri = pyotp.totp.TOTP(cle).provisioning_uri("")