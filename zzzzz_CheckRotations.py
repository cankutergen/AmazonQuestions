  def isRotation(s1, s2):

      if s1 == s2:
          return True

      if len(s1) != len(s2):
          return False

      for i in range(len(s1)):
          s1 = s1[1:] + s1[:1]

          if s1 == s2:
              return True

      return False
