print("Enter numbers, separated by ',': input_list: ['1', '5', '6', '8', '33', '57', '78', '3', '1', '54', '3', '23', '51', '8', '9']
value_list: [1, 5, 6, 8, 33, 57, 78, 3, 1, 54, 3, 23, 51, 8, 9]
array: [1, 5, 6, 8, 33, 57, 78, 3, 1, 54, 3, 23, 51, 8, 9]
m: 7
array: [1, 5, 6, 8, 33, 57, 78]
m: 3
array: [1, 5, 6]
m: 1
array: [1]
array: [5, 6]
m: 1
array: [5]
array: [6]
Merging...
left: [5]
right: [6]
merged: [5, 6]
Merging...
left: [1]
right: [5, 6]
merged: [1, 5, 6]
array: [8, 33, 57, 78]
m: 2
array: [8, 33]
m: 1
array: [8]
array: [33]
Merging...
left: [8]
right: [33]
merged: [8, 33]
array: [57, 78]
m: 1
array: [57]
array: [78]
Merging...
left: [57]
right: [78]
merged: [57, 78]
Merging...
left: [8, 33]
right: [57, 78]
merged: [8, 33, 57, 78]
Merging...
left: [1, 5, 6]
right: [8, 33, 57, 78]
merged: [1, 5, 6, 8, 33, 57, 78]
array: [3, 1, 54, 3, 23, 51, 8, 9]
m: 4
array: [3, 1, 54, 3]
m: 2
array: [3, 1]
m: 1
array: [3]
array: [1]
Merging...
left: [3]
right: [1]
merged: [1, 3]
array: [54, 3]
m: 1
array: [54]
array: [3]
Merging...
left: [54]
right: [3]
merged: [3, 54]
Merging...
left: [1, 3]
right: [3, 54]
merged: [1, 3, 3, 54]
array: [23, 51, 8, 9]
m: 2
array: [23, 51]
m: 1
array: [23]
array: [51]
Merging...
left: [23]
right: [51]
merged: [23, 51]
array: [8, 9]
m: 1
array: [8]
array: [9]
Merging...
left: [8]
right: [9]
merged: [8, 9]
Merging...
left: [23, 51]
right: [8, 9]
merged: [8, 9, 23, 51]
Merging...
left: [1, 3, 3, 54]
right: [8, 9, 23, 51]
merged: [1, 3, 3, 8, 9, 23, 51, 54]
Merging...
left: [1, 5, 6, 8, 33, 57, 78]
right: [1, 3, 3, 8, 9, 23, 51, 54]
merged: [1, 1, 3, 3, 5, 6, 8, 8, 9, 23, 33, 51, 54, 57, 78]
[1, 1, 3, 3, 5, 6, 8, 8, 9, 23, 33, 51, 54, 57, 78]
")
