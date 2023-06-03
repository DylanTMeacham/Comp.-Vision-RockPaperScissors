
from Visions import Visions

def _in_Robot():
    Visions()
    
def Robot():
    try:
        while True:
            _in_Robot()
    except StopIteration:
        pass
        
if __name__ == "__main__":
    Robot()