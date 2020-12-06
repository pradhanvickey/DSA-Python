class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkList:
  def __init__(self):
    self.head = None

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      temp = self.head
      while temp.next is not None:
        temp = temp.next
      temp.next = new_node

  def insert_at_any_given_point(self, data, pos):
    new_node = Node(data)
    temp = self.head
    for i in range(0, pos-1):
      temp = temp.next
    temp.next, new_node.next = new_node, temp.next
  
  def print_element(self):
    temp = self.head
    while temp is not None:
      end_str = " => "
      if temp.next is None:
        end_str = "\n"        
      print(temp.data, end=end_str)
      temp = temp.next

if __name__ == '__main__':
  l1 = LinkList()
  for i in range(1, 5):
    l1.insert_at_end(i)
  print("LinkList Before Insertion: ")
  l1.print_element()
  l1.insert_at_any_given_point(10, 2)
  print("\nLinkList After Insertion: ")
  l1.print_element()
