#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

row_output = ''

for row in picture:
  for column in row:
    if column == 0:
      row_output = row_output + ' '
    else:
      row_output = row_output + '*'
  print(row_output)
  row_output = ''
  