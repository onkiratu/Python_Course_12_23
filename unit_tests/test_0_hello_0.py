from hello_0 import hello

def test_default(): 
   assert hello() == "hello, world" 

def test_argument ():
   assert hello("Onesmus") == "hello, Onesmus"    
