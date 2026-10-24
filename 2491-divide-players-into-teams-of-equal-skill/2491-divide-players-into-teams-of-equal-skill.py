
class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        total = sum(skill)
        n = len(skill) // 2

        if total % n != 0:
            return -1

        target = total // n
        output = 0
        skill.sort()

        start = 0
        end = len(skill) - 1

        while start < end:
            pair_sum = skill[start] + skill[end]

            if pair_sum != target:
                return -1

            output += skill[start] * skill[end]
            start += 1
            end -= 1

        return output
