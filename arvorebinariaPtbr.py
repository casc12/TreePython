#1  Definição da arvaroe Binária 

# definição do No ou NODE
class Galho:
  def __init__(self, data):
     self.left = None
     self.right = None
     self.data = data


  def insert(self, data):
     if self.data is None:
	        self.data = data
     else:
         if data < self.data:
          if self.left is None:
            self.left = Galho(data)
          else:
            self.left.insert(data)
         elif data > self.data:
             if self.right is None:
              self.right = Galho(data)
             else:
              self.right.insert(data)
def inOrderPrint(r):
    if r is None:
        return
    else:
        inOrderPrint(r.left)
        print(r.data, end=' ')
        inOrderPrint(r.right)


def preOrderPrint(r):
       if r is None:
           return
       else:
           print(r.data, end=' ')
           preOrderPrint(r.left)
           preOrderPrint(r.right)

def postOrderPrint(r):
       if r is None:
           return
       else:
           print(r.data, end=' ')
           postOrderPrint(r.right)
           postOrderPrint(r.left)

if __name__ == '__main__':
    print("Bem vindo a arvore")
    root = Galho('g')
    root.insert('c')
    root.insert('b')
    root.insert('a')
    root.insert('e')
    root.insert('d')
    root.insert('f')
    root.insert('i')
    root.insert('h')
    root.insert('j')
    root.insert('k')

# 4 . Imprimindo os galhos em ordem 
print("\nimprimindo em ordem")
inOrderPrint(root)
print("\nimprimindo em pre-ordem")
preOrderPrint(root)
print("\nimprimindo em post-ordem")
postOrderPrint(root)
