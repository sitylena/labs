import pandas

data = pandas.read_csv('students.txt', sep=',')
list_of_series =[ pandas.Series(['Васильеве Олеге Алексеевиче', 'g2', None, None, 5, None, None], index=data.columns),
                  pandas.Series(['Ловцове Александре Николаевиче', 'g2', None, 4, 5, None, 7], index=data.columns)]
data = data.append(list_of_series, ignore_index=True)
print(data)
