def play_song_helper_2(instruments: dict, beat: float) -> dict:
    """"""
    play_dict = {}
    for instrument in instruments:
        play_dict[instrument] = []
        lst = []
        remain = 0
        val = 0
        for note in instruments[instrument]:
            if len(note) != 0:
                argument_list = note.strip().split(':')
                amp = 1
                if argument_list[0] == 'rest':
                    phrase = 'rest'
                    sample_duration = float(argument_list[1]) * beat
                else:
                    phrase = str(argument_list[0]) + ':' + str(argument_list[1])
                    sample_duration = float(argument_list[3]) * beat
                    amp = float(argument_list[2])
                remain += sample_duration
                dur = sample_duration
                if remain > 1:
                    val = round(remain - 1, 2)
                    remain = 1
                    dur = round(sample_duration - val, 2)
                if remain == 1:
                    if dur != 0:
                        lst.append((phrase, amp, dur))
                    play_dict[instrument].append(lst)
                    remain += val
                    lst = []
                elif remain < 1 and dur != 0:
                    lst.append((phrase, amp, dur))
                if remain >= 1:
                    remain -= 1
                    while remain >= 1:
                        play_dict[instrument].append([(phrase, amp, 1)])
                        remain -= 1
                    if remain != 0:
                        lst.append((phrase, amp, round(remain, 2)))
                    val = 0
            if (instruments[instrument].index(note) ==
                    len(instruments[instrument]) - 1) and remain != 0:
                lst.append(('rest', 1, round(1 - remain, 2)))
                play_dict[instrument].append(lst)
    return play_dict














# play_dict = {}
#     for instrument in instruments:
#         play_dict[instrument] = []
#         lst = []
#         remain = 0
#         val = 0
#         for note in instruments[instrument]:
#             if len(note) != 0:
#                 argument_list = note.strip().split(':')
#                 amp = 1
#                 if argument_list[0] == 'rest':
#                     phrase = 'rest'
#                     sample_duration = float(argument_list[1]) * beat
#                 else:
#                     phrase = str(argument_list[0]) + ':' + str(argument_list[1])
#                     sample_duration = float(argument_list[3]) * beat
#                     amp = float(argument_list[2])
#                 remain += sample_duration
#                 dur = round(sample_duration, 2)
#                 if remain > 1:
#                     val = round(remain - 1, 2)
#                     remain = 1
#                     dur = round(sample_duration - val, 2)
#                 if remain == 1:
#                     if dur != 0:
#                         lst.append((phrase, amp, dur))
#                     play_dict[instrument].append(lst)
#                     remain += val
#                     lst = []
#                 elif remain < 1 and dur != 0:
#                     lst.append((phrase, amp, dur))
#                 if remain >= 1:
#                     remain -= 1
#                     while remain >= 1:
#                         play_dict[instrument].append([(phrase, amp, 1)])
#                         remain -= 1
#                     if remain != 0:
#                         lst.append((phrase, amp, round(remain)))
#                     val = 0
#             if (instruments[instrument].index(note) ==
#                     len(instruments[instrument]) - 1) and remain != 0:
#                 lst.append(('rest', 1, round(1 - remain, 2)))
#                 play_dict[instrument].append(lst)
#     return play_dict
