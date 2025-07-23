status = 200
match(status):     
    case 200:
        print("ok")
    case 404:
        print("not found")
    case 500:
        print("server error")
    case _:
        print("unknown error")
        
#example two
data = ("Alice", 25)
match data:
    case (name, age) if age > 18:
        print(f"{name} is an adult.")
    case (name, age):
        print(f"{name} is a minor.")

comm = input("what is the command Start or stop: ")
command = comm.lower()

match command:
    case "start":
        print("starting..........")
    case "stop" :
        print("stopping............") 
    case _:
        print("unknown command")
    
    