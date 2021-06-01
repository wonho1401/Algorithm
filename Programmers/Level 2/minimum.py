def solution(A,B):
  answer = 0
  A = sorted(A)
  B = sorted(B, reverse = True)

  answer = sum([x*y for x,y in zip(A,B)])
  return answer
