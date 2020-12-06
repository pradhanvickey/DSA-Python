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

  def delete_at_start(self):
    self.head = self.head.next

  def delete_at_end(self):
    temp = self.head
    while temp.next.next is not None:
      temp = temp.next
    temp.next = None

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
  l1.delete_at_start()
  l1.print_element()
