for i in range(int(input())):
    width, height = map(int, input().split())
    bots, cmds = map(int, input().split())

    grid = [[0]*width for _ in range(height)]

    botlook = {}
    for i in range(1,bots+1):
        x,y,dir = input().split()
        x,y = int(x), int(y)
        botlook[i] = (x,y)
        grid[y-1][x-1] = (dir,i)
    
    # for asdf in grid:
    #     print(asdf)
    
    foundWreck = False
    for i in range(cmds):
        bot, act, rep = input().split()
        bot, rep = int(bot), int(rep)

        if foundWreck:
            continue

        x,y = botlook[bot]

        dir, _ = grid[y-1][x-1]

        if act == "L":
            tmp = "NWSE"
            dir = tmp[(tmp.index(dir)+rep) % 4]
            grid[y-1][x-1] = (dir,bot)
        elif act == "R":
            tmp = "NESW"
            dir = tmp[(tmp.index(dir)+rep) % 4]
            grid[y-1][x-1] = (dir,bot)
        else:
            if dir == "N":
                move = (0,1)
            elif dir == "S":
                move = (0,-1)
            elif dir == "E":
                move = (1,0)
            else:
                move = (-1,0)
            
            for _ in range(rep):
                nx = x+move[0]
                ny = y+move[1]
                if nx <= 0 or nx >= width+1:
                    print(f"Robot {bot} crashes into the wall")
                    foundWreck = True
                    break
                elif ny <= 0 or ny >= height+1:
                    print(f"Robot {bot} crashes into the wall")
                    foundWreck = True
                    break
                elif grid[ny-1][nx-1] != 0:
                    _, next_bot = grid[ny-1][nx-1]
                    print(f"Robot {bot} crashes into Robot {next_bot}")
                    foundWreck = True
                    break
                else:
                    grid[y-1][x-1] = 0
                    x, y = nx, ny
                    grid[y-1][x-1] = (dir,bot)
                    botlook[bot] = x,y
            
        
    if not foundWreck:
        print("OK")




                



