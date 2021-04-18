  def hasCycle(head: ListNode) -> bool:      
      if head is None:
          return False

      walker = head
      runner = head

      while runner and runner.next:
          walker = walker.next
          runner = runner.next.next

          if walker == runner:
              return True

      return False
