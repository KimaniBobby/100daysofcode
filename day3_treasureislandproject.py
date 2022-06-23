print('''
                       |
                  \_            /;              _.._
                  `\~--.._     //'            ,(+=\\\\
                   `//////\  \\/;'             /~ (\\\\
                     ~/////\~\`)'             /;   ))))
                         `~'  |              ((`~/((((\
                         ;'_\'\             /'))   )))))
                        /~/ '" "'     _.  /'/\_ /^\`((( \
                       `\/'       _.-~/--/ (  =(   | ,  |
                               _/~\_)_}___/^\/~`\.__\|==|
                              /uUUU)        )        |  |
                             (   / |      _-=o|\__ /'/~ \
                             ' /'  |     /(((((\`\(  |~\/
                             /'    |   /' )))))"`\`\|/_/---.._,$$,
                       .,ssS$$$Sss|._/_..-((('    )\)>>>      ~\$
                    ,sS$$$$$$$$$$$|$$$$$$$  |/    //'~`o        `\
                  ,$$$$$$$$$$$$$$|$$S$$$$'  (    /                \
                ,$$$$$$$$$$$$S$$|$$$$$$$'   |   /              ,s$$$
              s$$$$$S$$$$$$$$$S|$$$$$$$$    |  /              $$$$$$
            _~,$S""''     ``"S|$$S$$$$$"    (_,`\,          ,$$$$$$$;
          /~ ,"'             / 'S$$$$$"      \_./|        s$$$$$$$$$$
       (~'      _,  \==~~)  /     """         \  |       $$$$$$$$$$$$
        (0\   /0/     \-' /'                   \ |  |  ,$$$$$$$$$$$$$,
        `/'  '         _-~                     |= \_-\ $$$$$$$$$$$$$$s
        (~~~)      _.-~_-   \             \  ,s|= |   `"$$$$$$$$$$$$$$$
       ( `-'  )/>-~  _/-__   |            |,$$$|_/,      `"$$$$$$$$$$$$
       /V^^^^V~/' _/~/~~  ~~-|            |$$$$$$$$         "$$$$$$$$$$,
      /  (^^^^),/' /'        )           /S$$$$$$$;         ,$$$$$$$$$$$,
    ,$$_  `~~~'.,/'         /     _-ss, /(/-(/-(/'        ,s$$$$$$$$$$$$$
  ,s$$$$$ssSS$$$'         ,$'.s$$$$$$$$'                  (/-(/-(/-(/-(/'
 S$$$$$$$$$$$$$$        ,$$$$$$$$$$$$$'
(/-(/-(/-(/-(/'      _s$$$$$$$$$$$$$$
                    (/-(/-(/-(/-(/-'
''')
print("******************************************************************************")
print("Welcome to Treasure island")
print("******************************************************************************")

path =(str(input("You have been involved in an accident in the middle of nowhere, a cabin is seen up a hill with two paths leading there. Which path do you choose right or left?\n"))).lower()

if path == "right":
    print("Fall into a hole.GAME OVER!!!!")
elif path == "left":
        up_down=(str(input("climb or wait for help?"))).lower()
        if up_down == "climb":
            door =(str(input("You have reached the cabin safely but it has three doors. Red, Yellow,Blue. Which do you choose?\n"))).lower()
        elif up_down == "wait":
                print("Attacked by grizzly bear and her 10 cubs. GAMEOVER!!!")
        if door == "red":
            print("You fall into a VAT of acid.GAME OVER!!!")
        
        elif door == "yellow":
            print("You win")
        elif door == "blue":
            print("Eaten by a pack of  hungry wolves")
        else:
            print("GAME OVER YOU SORE LOSER!!!!")






