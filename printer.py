
def print_header():
      print("Thanks, now I'll print your string reversed, and twice")
      
def print_reversed(s):
    return s[::-1]

def print_twice(s):
    return( s ,s) 

if __name__ == "__main__":
    s = input()
    print_reversed(s)
    print_twice(s)
    print(print_header)
   