import collections

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        index = key % self.size  # hash값 생성
        # 비어있는 인덱스인 경우 값을 삽입한 후 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        
        p = self.table[index]
        while p:
            if p.key == key:  # 1) 동일한 key값이 존재하는 경우 입력된 값으로 덮어씌우고 함수 종료
                p.value = value
                return
            if p.next is None:  # 2) 연결리스트를 끝까지 다 돌아도 겹치는 값이 없으면 while loop 종료
                break
            p = p.next
        # 입력된 값을 연결리스트 뒤에 붙인다 (위에 2번인 경우에만 실행됨)
        p.next = ListNode(key, value)
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = key % self.size
        if self.table[index].value is None:  # 비어있는 key이면 -1 반환
            return -1
        
        p = self.table[index]
        while p:  # 해당 key에 매칭된 값이 존재할 경우, while loop을 돌면서 입력된 key와 일치하는 Node의 값을 반환
            if p.key == key:
                return p.value
            p = p.next
        return -1
        
        
        
    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        index = key % self.size

        if self.table[index].value is None:
            return
        
        p = self.table[index]
        # 동일한 index에 여러개의 Node가 연결된 경우 key값이 동일한 Node만 제거
        # 연결된 Node가 없을 경우 빈 연결리스트 삽입
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next  
            return
        
        # 첫번째 Node의 키값이 입력된 키값과 같지 않으면 while loop을 돌면서 동일한 키값을 가진 Node를 찾아 삭제한다
        # 연결리스트의 중간의 값을 지우도 다시 연결을 해주는 방식으로 값을 삭제한다
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next  # 삭제한 Node의 앞뒤 Node들을 연결해줌
                return
            prev, p = p, p.next
