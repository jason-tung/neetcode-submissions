class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count_student = Counter(students)
        for k in sandwiches:
            if count_student[k] <= 0:
                return sum(count_student.values())
            count_student[k]-=1
        return sum(count_student.values())