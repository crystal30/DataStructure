class Solution:
    def __init__(self):
        self.res = set()
        self.h_dict = dict()
    def readBinaryWatch(self, num):
        time = ['a', 'b', 'c', 'd', 1, 2, 4, 8, 16, 32]
        self.h_dict['a'] = 1
        self.h_dict['b'] = 2
        self.h_dict['c'] = 4
        self.h_dict['d'] = 8
        length_time = len(time)
        self._read_binary_watch(time, length_time, 0, num, [])
        if '' in self.res:
            self.res.remove('')
        return list(self.res)

    def _read_binary_watch(self, time, length_time, start, num, sub_time):
        if len(sub_time) == num:
            self.res.add(self.gengrate_time(sub_time, self.h_dict))
            return

        for i in range(start, length_time):
            sub_time.append(time[i])
            self._read_binary_watch(time, length_time, i+1, num, sub_time)
            sub_time.pop()
        return

    def gengrate_time(self, sub_time, h_dict):
        h = 0
        m = 0
        for e in sub_time:
            e_h = h_dict.setdefault(e, False)
            if e_h:
                h += e_h
            else:
                m += e

        if m >= 60:
            return ''

        if m <= 9:
            m = '0' + str(m)
        else:
            m = str(m)

        if h >= 12:
            return ''


        return '{0}:{1}'.format(h, m)

if __name__ == "__main__":
    so = Solution()
    num = 4
    re = so.readBinaryWatch(num)

    aa = ["0:15","0:23","0:27","0:29","0:30","0:39","0:43","0:45","0:46","0:51","0:53","0:54","0:57","0:58","1:07","1:11","1:13","1:14","1:19","1:21","1:22","1:25","1:26","1:28","1:35","1:37","1:38","1:41","1:42","1:44","1:49","1:50","1:52","1:56","2:07","2:11","2:13","2:14","2:19","2:21","2:22","2:25","2:26","2:28","2:35","2:37","2:38","2:41","2:42","2:44","2:49","2:50","2:52","2:56","3:03","3:05","3:06","3:09","3:10","3:12","3:17","3:18","3:20","3:24","3:33","3:34","3:36","3:40","3:48","4:07","4:11","4:13","4:14","4:19","4:21","4:22","4:25","4:26","4:28","4:35","4:37","4:38","4:41","4:42","4:44","4:49","4:50","4:52","4:56","5:03","5:05","5:06","5:09","5:10","5:12","5:17","5:18","5:20","5:24","5:33","5:34","5:36","5:40","5:48","6:03","6:05","6:06","6:09","6:10","6:12","6:17","6:18","6:20","6:24","6:33","6:34","6:36","6:40","6:48","7:01","7:02","7:04","7:08","7:16","7:32","8:07","8:11","8:13","8:14","8:19","8:21","8:22","8:25","8:26","8:28","8:35","8:37","8:38","8:41","8:42","8:44","8:49","8:50"]
    aa_set = set(aa)
    re_set = set(re)
    if len(re_set) != len(re):
        print('len(re_set) != len(re)')

    if re_set == aa_set:
        print('aa')
    else:
        print(re_set.difference(aa_set))
        print(aa_set.difference(re_set))
    print(re)