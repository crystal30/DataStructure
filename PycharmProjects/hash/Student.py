# -*- coding: utf-8 -*-
class Student():
    def __init__(self,grade, cls, firstname, lastname):
        self.grade = grade
        self.cls = cls
        self.firstname = firstname
        self.lastname = lastname

    def hashCode(self):
        B = 31
        myhash = 0

        # [self.grade, self.cls, self.firstname.lower(), self.lastname.lower()] 名字不区分大小写
        for e in [self.grade, self.cls, self.firstname, self.lastname]:
            myhash = myhash * B + hash(e)
        return myhash

    def equals(self,o):
        if o == self:
            return True
        if o == None:
            return False
        if type(o) != type(self):
            return False

        return self.grade == o.grade and self.cls == o.cls and \
               self.firstname == o.firstname and self.lastname == o.lastname

if __name__ == '__main__':
    s = Student(3,1,'xiao','ming')
    print(s.hashCode())

    s1 = Student(3,1,'XIAO','MING')
    print(s1.hashCode())
    print(s1.equals(s))


