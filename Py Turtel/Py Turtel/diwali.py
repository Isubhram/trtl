
import time
from random import randint


for i in range(1,45):

    print('*')
    
    space= ''
    for i in range(1,1000):
        count = randint (1,100)
        while ( count > 0):
            count-=1
            space +=' '
            if ( i%10==0):
                print( space + 'HAPPY DIWALI 2022')
                
            else:

                print(space + '*')
                space=''
                time.sleep(0.1)