import menu

if __name__ == "__main__":
    m = menu.Menu()
    
    while True:
        m.display()
        
        print()
        print('Press Q to quit, or any other key to continue: ')
        
        ans = input()
        if ans.upper() == 'Q': break

        print('='*60)
        print('='*60)
    
    

