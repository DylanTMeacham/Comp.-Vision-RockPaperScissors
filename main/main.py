
from robot import Robot

def _in_main():
   Robot()
    
def main():
    try:
        while True:
            _in_main()
    except StopIteration:
        pass
    
if __name__ == "__main__":
    main()