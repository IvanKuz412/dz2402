class Solution:
    def hello(self, name = 'Иван', surname = 'Иванов', years = 14):
        print('Привет, меня зовут', name, surname, 'мне', years, 'лет')
a = Solution()
a.hello('Дима', 'Петров', 20)
a.hello('Дима', 'Петров')
a.hello('Дима')
a.hello()