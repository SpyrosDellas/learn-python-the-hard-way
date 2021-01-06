class Parent(object):

    def override(self):
        print "PARENT override()"

    def implicit(self):       # This is implicitly inherited by Child
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"


class Child(Parent):

    def override(self):              # overrides Parent.override()
        print "CHILD override()"

    def altered(self):               # alters Parent.altered()
        print "CHILD, before PARENT altered()"
        super(Child, self).altered()
        print "CHILD, after PARENT altered()"


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
