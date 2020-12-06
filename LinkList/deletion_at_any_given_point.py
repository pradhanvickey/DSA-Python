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
  
  def delete_at_any_given_point(self, pos):
    if pos == 0:
      self.head = self.head.next
    else:
      count = 1
      temp = self.head
      for i in range(1, pos):
        if temp.next is None:
          print("Position doesn't exist")
          count = 0
          break
        temp = temp.next
      if count:
        if temp.next.next is None:
          temp.next = None
        else:
          temp.next = temp.next.next


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
  for i in range(1, 11):
    l1.insert_at_end(i)
  print("Original LinkList:")
  l1.print_element()
  print("\nAfter deleting First Node:")
  l1.delete_at_any_given_point(0)
  l1.print_element()
  print("\nAfter deleting last  Node:")
  l1.delete_at_any_given_point(3)
  l1.print_element()
  print("\nAfter deleting any Node:")
  l1.delete_at_any_given_point(2)
  l1.print_element()
  print("\nAfter deleting the Node that doesnot exists:")
  l1.delete_at_any_given_point(11)
  l1.print_element()
