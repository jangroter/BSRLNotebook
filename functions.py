import bluesky as bs

def reset_env():
    for acid in bs.traf.id:
        idx = bs.traf.id2idx(acid)
        bs.traf.delete(idx)
    bs.traf.cre('KL001',actype="A320",acalt=3000,acspd=150)
    return get_state()

def do_action(action):
    action = action * 2500
    acid = bs.traf.id[0]
    if -250<action<250:
        bs.stack.stack(f'ALT {acid},{bs.traf.alt[0]},{250}')
    if action > 0:
        bs.stack.stack(f'ALT {acid},45000,{action}')
    if action < 0:
        bs.stack.stack(f'ALT {acid},0,{-action}')

def get_state():
    alt = (bs.traf.alt[0]-1500)/3000
    vs = bs.traf.vs[0]
    dis = (200 - bs.tools.geo.kwikdist(52,4,bs.traf.lat[0],bs.traf.lon[0])*1.852-100)/200

    state = [alt,vs,dis]
    return state

def get_update(state):
    reward, done = get_reward(state)
    state_ = get_state()
    return state_,reward,done

def get_reward(state):
    alt = (state[0]*3000)+1500
    dis = (state[2]*200)+100
    if dis > 0 and alt> 0:
        return abs(3000-alt)*-5/3000, 0
    elif alt <= 0:
        return -10, 1
    elif dis <= 0:
        return abs(100-alt)*-20/3000, 1
        