class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        for sandwich in sandwiches:
            fails = 0
            while sandwich != students[0]:
                students.append(students.popleft())
                fails += 1
                if fails >= len(students):
                    return len(students)
            if sandwich == students[0]:
                students.popleft()
        return len(students)