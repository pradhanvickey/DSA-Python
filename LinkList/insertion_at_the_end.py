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
  #inserting element in LinkList
  for i in range(1, 5):
    l1.insert_at_end(i)
  #printing element in LinkList
  l1.print_element()
