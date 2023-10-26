class NODE:
  def __init__(self,info):
    self.info = info
    self.left = None
    self.right = None   
  def __str__(self):
    return f"{self.info} => {self.left.info if self.left else None}, {self.right.info if self.right else None}"


class Menu:
  def __init__(self):
    self.head = None
    self.temp = None
  def create(self,num):
    temp = None
    for i in range(num):
      info = int(input(f"Enter info=>{i}: "))
      temp = NODE(info)
      if self.head == None:
        self.head = temp
      else:
        self.insert(self.head,info)

  def insert(self,node,num):
    if(node.info > num):
      if(node.left != None):
        self.insert(node.left,num)
      else:
        node.left = NODE(num)
    else:
      if(node.right != None):
        self.insert(node.right,num)
      else:
        node.right = NODE(num)

  def printNode(self, node):
    if node != None:
      print(f"{node.info}")
      self.printNode(node.left)
      self.printNode(node.right)
    return;        

  def search(self, node, num):
    result = None
    # print(f"{node.info}",end="=> ")
    if node.info == num:
      # print(f"found")
      return True
    elif (node.left == None and node.right == None):
      # print("not found")
      return False
    else:
      if node.left:
        result = self.search(node.left, num)    
      if node.right and not result:
        result = self.search(node.right, num)    
    return result
  
  def min(self,node):
    if node.left != None:
      return self.min(node.left)
    else:
      return node
    # return node
  def max(self,node):
    if node.right != None:
      return self.max(node.right)
    else:
      return node
menu = Menu()
temp = None
while True:
    num = int(input("number: "))
    match num:
        case 1:
            num = int(input("Size: "))
            menu.create(num)
        case 2:
            menu.printNode(menu.head)
        case 3:
            print("found" if menu.search(menu.head,int(input("number to search: "))) else "not found")
        case 4:
            print(menu.min(menu.head))
        case 5:
            print(menu.max(menu.head))
        case default:
            break
