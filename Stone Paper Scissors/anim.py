import time
from os import system
welcome=""" 
__    __     _                          
/ / /\ \ \___| | ___ ___  _ __ ___   ___ 
\ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ 
 \  /\  /  __/ | (_| (_) | | | | | |  __/
  \/  \/ \___|_|\___\___/|_| |_| |_|\___|"""

to="""
            _____      
           /__   \___  
            / /\/ _ \ 
           / / | (_) |
           \/   \___/ """

stone="""
                      ▓▓████████████                                    
                  ██████▒▒▒▒▒▒▒▒▒▒████████████                          
            ████████▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓████████████                
          ████▒▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓████████              
        ▓▓██▒▒▒▒░░░░░░▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓████████▓▓        
        ██▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓████        
      ████▒▒░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓████      
    ██▒▒▒▒▒▒░░░░░░▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓██████  
  ██▒▒▒▒▒▒▒▒░░░░▒▒▒▒░░░░░░░░  ░░░░░░▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓██████  
  ██▓▓▒▒▒▒░░░░░░░░░░░░░░░░    ░░░░░░░░░░░░▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓██████  
  ██▓▓▒▒░░░░░░░░░░░░░░░░      ░░░░░░░░░░░░▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓████████  
████▓▓▒▒▒▒▓▓▓▓░░░░░░░░░░    ░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓██████    
████▓▓▓▓▒▒▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▒▒▓▓▓▓██████████
  ██▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓██████
  ██▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░▒▒░░▒▒▒▒▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓██████
  ████▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓████████
    ████▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓████████
      ████▓▓▓▓██▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░▒▒▒▒▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓██████  
        ████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████    
              ██▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▓▓██▓▓▓▓▓▓▓▓████████      
              ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓██████████      
                ██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓██████████        
                      ████████████████████▓▓██████████████████          
                          ████████████████████████████████              
                                        ████████████████                

"""

not_potato="""
                      ▓▓████████████                                    
                  ██████▒▒▒▒▒▒▒▒▒▒████████████                          
            ████████▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓████████████                
          ████▒▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓████████              
        ▓▓██▒▒▒▒░░░░░░▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓████████▓▓        
        ██▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓████        
      ████▒▒░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓████      
    ██▒▒▒▒▒▒░░░░░░▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓██████  
  ██▒▒▒▒▒▒▒▒░░░░▒▒▒▒░░░░░░░░  ░░░░░░▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓██████  
  ██▓▓▒▒▒▒░░░░░░░░░░░░░░░░    ░░░░░░░░░░░░▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓██████  
  ██▓▓▒▒░░░░░░░░░░░░░░░░      ░░░░░░░░░░░░▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓████████  
                        It's stone not potato  
████▓▓▓▓▒▒▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▒▒▓▓▓▓██████████
  ██▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓██████
  ██▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░▒▒░░▒▒▒▒▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓██████
  ████▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓████████
    ████▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓████████
      ████▓▓▓▓██▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░▒▒▒▒▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓██████  
        ████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████    
              ██▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▓▓██▓▓▓▓▓▓▓▓████████      
              ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓██████████      
                ██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓██████████        
                      ████████████████████▓▓██████████████████          
                          ████████████████████████████████              
                                        ████████████████                

"""
Paper="""
    ▓▓▓▓▓▓        ▓▓▓▓▓▓      ▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓    
░░▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▓▓  
░░▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓  
░░▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓  
░░▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓  
    ▓▓▒▒░░░░░░░░██████░░░░░░████░░░░░░██████░░░░░░██████░░░░░░▒▒▓▓▓▓
    ▓▓▒▒░░░░░░░░░░░░████████░░██████████░░██████████░░░░░░░░░░▒▒▓▓▓▓
    ▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓  
░░▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓  
░░▓▓▒▒░░░░░░░░████████░░░░░░░░░░░░░░████░░░░██░░░░░░░░██░░░░░░▒▒▓▓▓▓
░░▓▓▒▒░░░░░░░░░░░░░░████████░░████████████████░░░░██████░░░░░░░░▒▒▓▓
░░▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓
    ▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓
    ▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓
    ▓▓▒▒░░░░░░░░████████░░░░██████░░████░░░░██░░████████░░░░░░▒▒▓▓  
    ▓▓▓▓▒▒░░░░░░░░░░░░████████░░██████░░░░░░██████░░░░░░░░░░░░▒▒▓▓  
      ▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓  
    ▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓
    ▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓
    ▓▓▒▒░░░░░░██████████░░██████░░██████░░░░████████████░░░░░░░░▒▒▓▓
    ▓▓▒▒░░░░░░░░░░░░░░██████░░██████░░░░░░░░░░░░░░░░░░██░░░░░░░░▒▒▓▓
    ▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓
    ▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓
    ▓▓▒▒░░░░░░░░░░░░░░████████░░░░░░░░░░░░░░██░░░░██████░░░░░░▒▒▒▒  
    ▓▓▒▒░░░░░░░░████████░░░░██████████░░░░░░████████░░████░░░░▒▒▒▒  
░░▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒  
░░▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓  
░░▓▓▓▓▒▒░░░░░░░░██░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░▒▒▓▓▓▓
    ▓▓▒▒░░░░░░░░██████░░████████░░████░░░░████████████░░██░░░░░░▒▒▓▓
    ▓▓▒▒░░░░░░░░░░░░██████░░░░██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓
░░▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓
░░▓▓▓▓▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▓▓
    ▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓  
          ▓▓▓▓▓▓        ▓▓▓▓▓▓    ▓▓▓▓▓▓      ▓▓▓▓      ▓▓▓▓▓▓▓▓▓▓  
"""
scissors="""                              
                                                          ▒▒▒▒▒▒                
                                                      ▒▒▒▒░░░░▒▒                
                                                    ▒▒░░░░░░▒▒                  
                  ██▓▓██▓▓▓▓                      ▒▒░░░░░░▒▒                    
                ██▒▒▒▒░░▒▒░░██                  ▒▒░░░░░░▒▒                      
              ██▒▒▒▒██████▒▒▒▒██              ▒▒░░░░░░▒▒                        
            ▓▓░░▒▒██      ██▒▒░░██          ▒▒░░░░░░▒▒                          
            ██░░▒▒██        ██▒▒░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒          
            ██▒▒▒▒▒▒██▓▓██▓▓▒▒░░▒▒░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒          
              ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▓▓░░██░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒            
                ██████████████████████░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                
                              ████▒▒░░██░░▒▒                                    
                            ██▒▒░░▒▒░░░░██                                      
                          ██▒▒▒▒████▒▒▒▒██                                      
                        ██▒▒▒▒▓▓    ██░░██                                      
                      ██▒▒▒▒██      ██▒▒██                                      
                    ██▒▒▒▒██      ▓▓▒▒▒▒██                                      
                    ██▒▒██      ██░░▒▒██                                        
                    ▓▓▒▒▒▒▓▓▓▓▓▓░░░░▓▓                                          
                      ██▒▒░░▒▒░░▒▒▓▓                                            
                        ████████▓▓                                                                                                                         
"""

hand_movement=["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)""",
"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""]

# print(welcome)
# time.sleep(.5)
# print(to)
# time.sleep(1)
# _ = system('cls')
# print(stone)
# time.sleep(.5)
# _ = system('cls')
# print(not_potato)
# time.sleep(1.4)
# _ = system('cls')
# print(Paper)
# time.sleep(1.4)
# _ = system('cls')
# print(scissors)
print(hand_movement)
