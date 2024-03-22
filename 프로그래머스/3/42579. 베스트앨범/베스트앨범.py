def solution(genres, plays):
    genre_cnt = {}
    playlist_candidates = []
    for i, (g, p) in enumerate(zip(genres, plays)):
        playlist_candidates.append((g, p, i))
        if g not in genre_cnt:
            genre_cnt[g] = p
        else:
            genre_cnt[g] += p
    playlist_candidates.sort(key= lambda x: (x[0], -x[1], x[2]))
    playlist = []
    for k, v in sorted(genre_cnt.items(), key = lambda x: -x[1]):
        cnt = 0
        for g, _, i in playlist_candidates:
            if k == g:
                cnt += 1
                if cnt > 2:
                    break
                playlist.append(i)
    return playlist
