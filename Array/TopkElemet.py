class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Extract unique elements
        unique_nums = []
        frequencies = []

        for num in nums:
            if num in unique_nums:
                index = unique_nums.index(num)
                frequencies[index] += 1  # Increment frequency
            else:
                unique_nums.append(num)
                frequencies.append(1)  # Initialize frequency

        # Step 2: Sort unique_nums based on frequencies
        for i in range(len(frequencies)):
            for j in range(i + 1, len(frequencies)):
                if frequencies[i] < frequencies[j]:  # Sort in descending order
                    frequencies[i], frequencies[j] = frequencies[j], frequencies[i]
                    unique_nums[i], unique_nums[j] = unique_nums[j], unique_nums[i]

        # Step 3: Return the top k elements
        return unique_nums[:k]  # Take the first k elements