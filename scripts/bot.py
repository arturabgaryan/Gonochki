def choose(x,y,objects):
    for object in objects:
        if object['y']<y:
            break
    if objects == []:
        return None
    if object['y']-y<200:
        if object['x'] < x < object['x']+object['width']:
            if x-object['x'] < object['x']+object['width']-x:
                if object['x']>100:
                    return 'left'
                else:
                    return 'right'
            else:
                if object['x']+object['width'] < 1024:
                    return 'right'
                else:
                    return 'left'
        else:
            return choose(objects[1:-1])

