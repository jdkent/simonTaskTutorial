if expInfo['counterbalance'] == '0':
    bindings = {'X': 'm', 'O': 'z'}
    if thisTrial['condition'] == 'incongruent':
        if thisTrial['stim'] == 'X':
            left_stim_text = thisTrial['stim']
            right_stim_text = ''
            ans = 'm'
        elif thisTrial['stim'] == 'O':
            left_stim_text = ''
            right_stim_text = thisTrial['stim']
            ans = 'z'
    elif thisTrial['condition'] == 'congruent':
        if thisTrial['stim'] == 'X':
            left_stim_text = ''
            right_stim_text = thisTrial['stim']
            ans = 'm'
        elif thisTrial['stim'] == 'O':
            left_stim_text = thisTrial['stim']
            right_stim_text = ''
            ans='z'
elif expInfo['counterbalance'] == '1':
    bindings = {'O': 'm', 'X': 'z'}
    if thisTrial['condition'] == 'incongruent':
        if thisTrial['stim'] == 'X':
            left_stim_text = ''
            right_stim_text = thisTrial['stim']
            ans = 'z'
        elif thisTrial['stim'] == 'O':
            left_stim_text = thisTrial['stim']
            right_stim_text = ''
            ans = 'm'
    elif thisTrial['condition'] == 'congruent':
        if thisTrial['stim'] == 'X':
            left_stim_text = thisTrial['stim']
            right_stim_text = ''
            ans = 'z'
        elif thisTrial['stim'] == 'O':
            left_stim_text = ''
            right_stim_text = thisTrial['stim']
            ans = 'm'
