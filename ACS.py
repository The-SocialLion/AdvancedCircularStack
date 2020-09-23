class AdvancedCircularStack:
  def __init__(self):
    self.cs=[]
    self.limit=int(input("enter limit"))
    self.top=None
    self.bottom=None
  def isfull(self):
    if len(self.cs) == self.limit:
      return True
    else:
      return False
  def isempty(self):
    if len(self.cs)== 0:
      return True
    else:
      return False
  def push_top(self,ele):
    if self.isfull() :
      print("Advanced circular stack overflow")
    else:
      if self.top==None and self.bottom==None:
        self.top=self.bottom=0
      else:
        self.top=(self.top+1)%self.limit
      self.cs.append(ele)
  def push_bottom(self,ele,n):
    if self.isfull():
      print("Advanced circular stack overflow")
    else:
      if self.top==None and self.bottom==None:
        self.top=self.bottom=0
      else:
        self.bottom=(self.bottom+1)%self.limit
      self.cs.insert(n,ele)
  def pop_top(self):
    if self.isempty():
      print("Advanced circular stack overflow")
    else:
      print(self.cs.pop())
      if self.top == self.bottom:
          self.top=self.bottom=None
      else:
          self.top=(self.top+1)%self.limit
  def pop_bottom(self,n):
    if self.isempty():
      print("Advanced circular stack overflow")
    else:
      print(self.cs.pop(n))
      if self.top == self.bottom:
          self.top=self.bottom=None
      else:
          self.bottom=(self.bottom+1)%self.limit
  def display(self):
    if self.isempty():
      print("Advanced circular stack overflow")
    else:
      for i in self.cs:
        print(i,end=" ")
      print()
  def peek(self):
    if self.isempty():
      print("Advanced circular stack overflow")
    else:
      print(self.cs[-1])
acs=AdvancedCircularStack()
while True:
  print("1.Push_top,2.Push_bottom,3.pop_top")
  print("4.pop_bottom, 5.peek,6.display,7.exit")
  ch=int(input("enter your choice"))
  if ch==1:
    ele=int(input("enter element"))
    acs.push_top(ele)
  elif ch==2:
    n=int(input("enter position"))
    ele=int(input("enter element"))
    acs.push_bottom(ele,n)
  elif ch==3:
    acs.pop_top()
  elif ch==4:
    n=int(input("enter position"))
    acs.pop_bottom(n)
  elif ch==5:
    acs.peek()
  elif ch==6:
    acs.display()
  elif ch==7:
    break
  else:
    print("invalid choice try again")
