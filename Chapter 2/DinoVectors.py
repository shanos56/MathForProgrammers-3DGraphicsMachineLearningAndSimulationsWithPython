import matplotlib.pyplot as ply;



def getX(xy)
    x = [];
    for point in xy
        x.append(point[0]);
    
    return x;

def getY(xy)
    y = [];
    for point in xy
        y.append(point[1]);
    
    return y;
    

    
def dinosaur (xy)
    x = getX(xy)
    y = getY(xy)

    ply.plot(x,y);
    


    
    
xy = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4), (-5,3), (-5,2),(-2,2), (-5,1), (-4,0),(-2,1),(-1,0),(0,-3),(-1,-4),(1,-4),(2,-3),(1,-2),(3,-1),(5,1)];

dinosaur(xy)
        
