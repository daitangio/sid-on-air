print("Testing I2C Sid addr 23")
import time
import machine

i2c = machine.I2C(scl=machine.Pin(13),sda=machine.Pin(12))
while True:
    r=i2c.scan()
    print(str(r))
    if( 23 in r ):
        print("Sid found!")
        break
    time.sleep(1)

def setRegister(sidReg,value):
    buf = bytearray(2)
    buf[0]=sidReg
    buf[1]=value
    i2c.writeto(23,buf)
    
def play(voice,freq):
  low = freq & 0x00FF;
  high= freq >>8;
  setRegister(0,low)
  setRegister(1,high)
  print("Sent:"+str(freq))
  #set_register(voice+0,low);
  #set_register(voice+1,high);
    


print("Trying very simple music setup")
for x in range(60,64):
    play(1,x)
    time.sleep(1)
play(1,0)

