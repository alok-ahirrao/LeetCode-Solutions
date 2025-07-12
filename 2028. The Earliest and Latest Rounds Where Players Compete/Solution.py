EXTREMES = [[[[1, 1] for second_i in range(first_i+1, n-first_i)] for first_i in range(n>>1)] for n in range(2, 29)]
def get_from_0(n, first_i, second_i):
    second_from_end = n - 1 - second_i
    used_first_i = second_from_end if first_i > second_from_end else first_i
    return EXTREMES[n-2][used_first_i][second_i-first_i-1]

for n_i, per_size in enumerate(EXTREMES):
    n = n_i + 2
    old_n = (n + 1) >> 1
    for first_i, per_first in enumerate(per_size):
        for betweens in range(len(per_first)-1):
            second_i = first_i + betweens + 1
            second_complement_i = n - 1 - second_i
            earliest_pre = n
            latest_pre = 0
            if second_i <= second_complement_i:
                for keep1 in range(first_i+1):
                    for keep2 in range(betweens+1):
                        old_first_i = keep1
                        old_second_i = old_first_i + keep2 + 1
                        old_earliest, old_latest = get_from_0(old_n, old_first_i, old_second_i)
                        if earliest_pre > old_earliest:
                            earliest_pre = old_earliest
                        if latest_pre < old_latest:
                            latest_pre = old_latest
            else:
                must_keep = (second_i - second_complement_i - 1 + 1) >> 1
                for keep1 in range(first_i+1):
                    for keep2 in range(second_complement_i-first_i):
                        old_first_i = keep1
                        old_second_i = old_first_i + keep2 + must_keep + 1
                        old_earliest, old_latest = get_from_0(old_n, old_first_i, old_second_i)
                        if earliest_pre > old_earliest:
                            earliest_pre = old_earliest
                        if latest_pre < old_latest:
                            latest_pre = old_latest
            per_first[betweens][0] = earliest_pre + 1
            per_first[betweens][1] = latest_pre + 1

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        secondDistFromEnd = n + 1 - secondPlayer
        usedFirstPlayer = secondDistFromEnd if firstPlayer > secondDistFromEnd else firstPlayer
        return EXTREMES[n-2][usedFirstPlayer-1][secondPlayer-firstPlayer-1]