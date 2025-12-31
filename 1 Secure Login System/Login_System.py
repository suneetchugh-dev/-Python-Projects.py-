def verify(username, password, filepath):
    try:
        password += "\n"
        
        with open(filepath, 'r') as file:
            lines = file.readlines()
        for line in lines:
            field = line.split(',')
            
            if(field[0]==username, field[1]==password):
                return True
            else:
                return False
    except Exception:
        print(Exception)
    
print(verify("SuneetChugh", "chughsahabh", "data.txt"))