from typing import List

class Merge_sort:
    def merge(self, arr: List[int], arr2: List[int]) -> List[int]:

        firstP, secondP = 0 , 0
        merged = []

        while firstP < len(arr) and secondP < len(arr2):
            if arr[firstP] < arr2[secondP]:
                merged.append(arr[firstP])
                firstP += 1
            else:
                merged.append(arr2[secondP])
                secondP += 1
        
        while firstP < len(arr):
            merged.append(arr[firstP])
            firstP += 1

        while secondP < len(arr2):
            merged.append(arr2[secondP])
            secondP += 1    

        return merged

    def merge_sort(self, arr: List[int]) -> List[int]:
        
        if len(arr) == 1:
            return arr
        
        middlePoint = len(arr) // 2

        left = arr[:middlePoint]
        right = arr[middlePoint:]

        return self.merge(self.merge_sort(left), self.merge_sort(right))
    
def main():
        
        arx = [47, 36, 19, 96, 37, 89]

        print("Original array: ", arx)

        solution = Merge_sort()

        sorted_array = solution.merge_sort(arx)

        print("Sorted array: ", sorted_array)

if __name__ == "__main__":
    main()