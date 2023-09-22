def ID() :
    x = float(input('x = '))
    return x

def XY( x ) :
    y = (( 2 * ( x * x )) + ( 2 * x ) + 1 )
    return y

def YA( x, y ) :
    print(f'y = ( 2  * ( {x:.0f} * {x:.0f} )) + ( 2 * {x:.0f} ) + 1')
    print(f'ตอบ : {y:.0f}')

print('-----------------------------')
x = ID()
y = XY( x )
print('-----------------------------')
YA( x, y )
print('-----------------------------')