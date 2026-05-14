#라벨이 없는 경우: - 를 원하는 갯수만큼 찍는다.
def drawOneTickWoL(tickLength):
  for i in range(tickLength):
    print("-", end='')
  print("")

#라벨이 있는 경우: 원하는 갯수만큼 -를 찍고 라벨을 print한다.
def drawOneTickWL(tickLength, tickLabel):
  for i in range(tickLength):
    print("-", end='')
  print(tickLabel)


#재귀 호출을 통해서 자의 눈금을 찍는 코드
def drawTicks(tickLength):
  return

def drawRuler(nInches, majorLength):
  drawOneTickWL(majorLength, 0)
  for i in range(nInches): #0부터 시작
    drawTicks(majorLength)
    drawOneTickWL(majorLength, i+1)


if __name__ == "__main__":
    drawRuler(10,4)