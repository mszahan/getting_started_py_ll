from dataclasses import dataclass


@dataclass(frozen=True) # the frozen parameter make the class immutable
class ImmutableClass:
    value1 : str = 'value 1'
    value2 : int = 0

    ## you can't even modify within the class
    def some_func(self, newval):
        self.value2 = newval

## you can chagne the atribute in intial level
## like during creating the instance
obj = ImmutableClass('another string', 20)

print(obj.value1)

## now you can't change the value of the object atribute
# obj.value1 = 'another value'
# print(obj.value1)


## this function call will also throw an error
# obj.some_func(20)
